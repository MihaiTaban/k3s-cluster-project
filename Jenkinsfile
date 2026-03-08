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
    command:
    - sleep
    args:
    - infinity
'''
    }
  }
  stages {
    stage('Install Prometheus Stack') {
      steps {
        container('helm') {
          sh '''
          helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
          helm repo update
          # Am adăugat --atomic pentru a da rollback automat dacă eșuează
          helm upgrade --install prometheus-stack prometheus-community/kube-prometheus-stack               --namespace monitoring --create-namespace               -f charts/prometheus/values.yaml               --atomic --timeout 10m
          '''
        }
      }
    }
  }
}
