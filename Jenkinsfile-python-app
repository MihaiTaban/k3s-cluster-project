pipeline {
    agent any

    environment {
        APP_NAME = "python-test-app"
        CHART_PATH = "./charts/python-app-chart"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Docker Build') {
            steps {
                echo "Construim imaginea Docker..."
                sh "docker build -t ${APP_NAME}:latest ."
            }
        }

        stage('Helm Deploy') {
            steps {
                echo "Lansăm aplicația în Kubernetes folosind Helm..."
                // Folosim upgrade --install ca să meargă și la prima rulare și la următoarele
                sh "helm upgrade --install ${APP_NAME} ${CHART_PATH} --set image.tag=latest"
            }
        }

        stage('Verify') {
            steps {
                echo "Verificăm statusul resurselor..."
                sh "kubectl get pods -l app.kubernetes.io/name=python-app-chart"
                sh "kubectl get svc ${APP_NAME}-python-app-chart"
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executat cu succes! Aplicația e sus.'
        }
        failure {
            echo 'Ceva nu a mers bine. Verifică logurile de Docker sau Helm.'
        }
    }
}
