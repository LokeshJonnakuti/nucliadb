{{ define "curator.cronjob" }}
kind: CronJob
apiVersion: batch/v1beta1
metadata:
  name: "{{ .cronname }}"
  labels:
    app: "{{ .Chart.Name }}"
    version: "{{ .Values.hash }}"
    chart: "{{ .Chart.Name }}"
    release: "{{ .Release.Name }}"
    heritage: "{{ .Release.Service }}"
spec:
  schedule: "{{ .schedule }}"
  jobTemplate:
    metadata:
      name: "{{ .cronname }}"
      annotations:
        sidecar.istio.io/inject: "false"
      labels:
        app: {{ .Chart.Name }}
        role: cronjobs
        version: "{{ .Values.hash }}"
        chart: "{{ .Chart.Name }}"
        release: "{{ .Release.Name }}"
    spec:
      backoffLimit: 0
      template:
        metadata:
          labels:
            app: "{{ .Chart.Name }}"
            role: cronjobs
            version: "{{ .Values.hash }}"
            release: "{{ .Release.Name }}"
          annotations:
            sidecar.istio.io/inject: "false"
        spec:
          nodeSelector:
{{ toYaml .Values.nodeSelector | indent 12 }}
          affinity:
{{ toYaml .Values.affinity | indent 12 }}
          tolerations:
{{ toYaml .Values.tolerations | indent 12 }}
          dnsPolicy: ClusterFirst
          restartPolicy: Never
          containers:
          - name: "{{ .cronname }}"
            image: "{{ .Values.image }}"
            envFrom:
            - configMapRef:
                name: nucliadb-config
            - configMapRef:
                name: {{ .Release.Name }}-config
            imagePullPolicy: Always
            command: ["{{ .command }}"]
            volumeMounts:
            - mountPath: /cache
              name: cache-volume
{{- if .Values.nats.secretName }}
            volumeMounts:
            - name: nats-creds
              readOnly: true
              mountPath: /appsecrets
{{- end }}
          volumes:
{{- if .Values.nats.secretName }}
          - name: nats-creds
            secret:
              secretName: {{ .Values.nats.secretName }}
{{- end }}
          - name: cache-volume
            emptyDir: {}
{{ end }}