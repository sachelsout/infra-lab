# Day 30 – Deploying FastAPI File Upload App on Kubernetes using Helm

As part of Day 30 of my Infrastructure Engineering journey, I created a **custom Helm chart** to deploy the FastAPI file upload application (from Day 27) on Kubernetes. Helm helps in managing complex Kubernetes applications with reusable and configurable templates.

---

## 📦 Project Structure

```plaintext
helm-fastapi-app/
├── app/
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
├── charts/
│   └── fileupload/
│       ├── Chart.yaml
│       ├── values.yaml
│       ├── templates/
│       │   ├── deployment.yaml
│       │   ├── service.yaml
│       │   └── _helpers.tpl
├── .helmignore
```

---

## ⚙️ Step-by-Step Process

### 1. ✅ Created Helm Chart

```bash
helm create charts/fileupload
```

This scaffolded a Helm chart with templated Kubernetes manifests inside `charts/fileupload`.

### 2. ✏️ Edited Key Files

#### 📌 `Chart.yaml`

Updated app metadata:

```yaml
apiVersion: v2
name: fileupload
description: A Helm chart for deploying the FastAPI file upload app
version: 0.1.0
appVersion: "1.0"
```

#### 📌 `values.yaml`

Basic app configuration:

```yaml
image:
  repository: fileupload-app
  tag: v1
  imagePullPolicy: Never

service:
  type: ClusterIP
  port: 80

containerPort: 8000
```

#### 📌 `templates/deployment.yaml`

Templated the Kubernetes Deployment using Helm syntax:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "fileupload.fullname" . }}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ include "fileupload.name" . }}
  template:
    metadata:
      labels:
        app: {{ include "fileupload.name" . }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          ports:
            - containerPort: {{ .Values.containerPort }}
```

#### 📌 `templates/service.yaml`

Defined how to expose the app:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ include "fileupload.fullname" . }}
spec:
  type: {{ .Values.service.type }}
  selector:
    app: {{ include "fileupload.name" . }}
  ports:
    - port: {{ .Values.service.port }}
      targetPort: {{ .Values.containerPort }}
```

#### 📌 `templates/_helpers.tpl`

Added helper functions (required for full chart rendering):

```yaml
{{/*
Expand the name of the chart.
*/}}
{{- define "fileupload.name" -}}
{{- .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{/*
Create a default fully qualified app name.
*/}}
{{- define "fileupload.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{/*
Common labels
*/}}
{{- define "fileupload.labels" -}}
app.kubernetes.io/name: {{ include "fileupload.name" . }}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}
```

### 3. 🐳 Built Docker Image

```bash
docker build -t fileupload-app ./app
```

### 4. 📦 Installed Helm Chart

```bash
helm install fileupload charts/fileupload
```

Successfully deployed the app via Helm!

### 5. 🌐 Accessed the App

If the service was `ClusterIP`, used port-forwarding:

```bash
kubectl port-forward service/fileupload 8000:80
```

Then accessed: http://localhost:8000

## 📸 Outcome

The FastAPI app is now running on Kubernetes, managed via a Helm chart. This setup improves maintainability, scalability, and version control of deployments.

## ✅ Key Takeaways

- Helm simplifies K8s app deployment via templated charts.

- A clean `values.yaml` allows customization without editing raw manifests.

- Helper templates enable reusable naming and structure.

- Kubernetes + Helm = production-ready infrastructure tooling.

## 🔗 Related Days

- Day 27: Added readiness/liveness probes to the FastAPI app.

- Day 28: Explored Kubernetes Dashboard for cluster monitoring.