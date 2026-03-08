pipeline {
  agent {
    kubernetes {
      yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: helm
    image: alpine/helm:3.12.0
    command: ["sleep"]
    args: ["infinity"]
'''
    }
  }
  stages {
    stage('Install Micro Monitoring') {
      steps {
        container('helm') {
          sh '''
          helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
          helm repo update
          # Atenție: folosim chart-ul "prometheus", nu "kube-prometheus-stack"
          helm upgrade --install prometheus-lite prometheus-community/prometheus \
              --namespace monitoring --create-namespace \
              -f charts/prometheus/values.yaml
          '''
        }
      }
    }
  }
}
