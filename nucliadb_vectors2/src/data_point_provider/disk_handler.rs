// Copyright (C) 2021 Bosutech XXI S.L.
//
// nucliadb is offered under the AGPL v3.0 and as commercial software.
// For commercial licensing, contact us at info@nuclia.com.
//
// AGPL:
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as
// published by the Free Software Foundation, either version 3 of the
// License, or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU Affero General Public License for more details.
//
// You should have received a copy of the GNU Affero General Public License
// along with this program. If not, see <http://www.gnu.org/licenses/>.
//

use std::fs::{File, OpenOptions};
use std::io;
use std::path::{Path, PathBuf};
use std::time::SystemTime;

use fs2::FileExt;

use super::{State, VectorR};

mod names {
    pub const LOCK: &str = "lk.lock";
    pub const STATE: &str = "state.bincode";
}

#[derive(Clone, Copy, Debug, PartialEq, Eq, PartialOrd, Ord)]
pub struct Version(SystemTime);

fn write_state(path: &Path, state: &State) -> VectorR<()> {
    let mut file = OpenOptions::new()
        .create(true)
        .write(true)
        .truncate(true)
        .open(path.join(names::STATE))?;
    bincode::serialize_into(&mut file, state)?;
    Ok(())
}

fn read_state(path: &Path) -> VectorR<State> {
    let mut file = OpenOptions::new()
        .read(true)
        .open(path.join(names::STATE))?;
    Ok(bincode::deserialize_from(&mut file)?)
}

fn initialize_disk(path: &Path) -> VectorR<()> {
    if !path.join(names::STATE).is_file() {
        write_state(path, &State::new(path.to_path_buf()))?;
    }
    Ok(())
}

pub(super) fn exclusive_lock(path: &Path) -> VectorR<ELock> {
    initialize_disk(path)?;
    Ok(ELock::new(path)?)
}
pub(super) fn shared_lock(path: &Path) -> VectorR<SLock> {
    initialize_disk(path)?;
    Ok(SLock::new(path)?)
}

pub(super) fn persist_state(lock: &ELock, state: &State) -> VectorR<()> {
    write_state(lock.as_ref(), state)
}

pub(super) fn load_state(lock: &Lock) -> VectorR<State> {
    read_state(lock.as_ref())
}
pub(super) fn crnt_version(lock: &Lock) -> VectorR<Version> {
    let meta = std::fs::metadata(lock.path.join(names::STATE))?;
    Ok(Version(meta.modified()?))
}

pub struct Lock {
    path: PathBuf,
    #[allow(unused)]
    lock: File,
}
impl Lock {
    fn open_lock(path: &Path) -> io::Result<File> {
        let file = OpenOptions::new()
            .read(true)
            .write(true)
            .create(true)
            .open(path.join(names::LOCK))?;
        Ok(file)
    }
    fn exclusive(path: &Path) -> io::Result<Lock> {
        let path = path.to_path_buf();
        let lock = Lock::open_lock(&path)?;
        lock.lock_exclusive()?;
        Ok(Lock { lock, path })
    }
    fn shared(path: &Path) -> io::Result<Lock> {
        let path = path.to_path_buf();
        let lock = Lock::open_lock(&path)?;
        lock.lock_shared()?;
        Ok(Lock { lock, path })
    }
}
impl AsRef<Path> for Lock {
    fn as_ref(&self) -> &Path {
        &self.path
    }
}

pub struct ELock(Lock);
impl ELock {
    pub(super) fn new(path: &Path) -> io::Result<ELock> {
        Lock::exclusive(path).map(ELock)
    }
}
impl std::ops::Deref for ELock {
    type Target = Lock;
    fn deref(&self) -> &Self::Target {
        &self.0
    }
}
impl AsRef<Path> for ELock {
    fn as_ref(&self) -> &Path {
        self.0.as_ref()
    }
}

pub struct SLock(Lock);
impl SLock {
    pub fn new(path: &Path) -> io::Result<SLock> {
        Lock::shared(path).map(SLock)
    }
}
impl std::ops::Deref for SLock {
    type Target = Lock;
    fn deref(&self) -> &Self::Target {
        &self.0
    }
}
impl AsRef<Path> for SLock {
    fn as_ref(&self) -> &Path {
        self.0.as_ref()
    }
}

#[cfg(test)]
mod tests {
    use tempfile::TempDir;

    use super::*;
    #[test]
    fn test() {
        let dir = TempDir::new().unwrap();
        let lock = exclusive_lock(dir.path()).unwrap();
        assert!(dir.path().join(names::STATE).is_file());
        assert!(dir.path().join(names::LOCK).is_file());
        let v0 = crnt_version(&lock).unwrap();
        std::mem::drop(lock);
        let lock = exclusive_lock(dir.path()).unwrap();
        assert!(dir.path().join(names::STATE).is_file());
        assert!(dir.path().join(names::LOCK).is_file());
        assert_eq!(v0, crnt_version(&lock).unwrap());
        write_state(dir.path(), &State::new(dir.path().to_path_buf())).unwrap();
        let new_version = crnt_version(&lock).unwrap();
        assert!(v0 < new_version);
    }
}