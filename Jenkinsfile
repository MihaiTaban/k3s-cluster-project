pipeline {
    agent any
    stages {
        stage('Install Prometheus Stack') {
            steps {
                sh '''
                helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
                helm repo update
                helm upgrade --install prometheus-stack prometheus-community/kube-prometheus-stack \
                    --namespace monitoring --create-namespace \
                    -f charts/prometheus/values.yaml
                '''
            }
        }
    }
}
