pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Wisam2198/Docker_Kaizen.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Construire l'image Docker en utilisant le Dockerfile
                    sh 'docker build -t docker-kaizen .'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Exécuter les tests à l'intérieur du conteneur Docker
                    sh 'docker run --rm docker-kaizen pytest --junitxml=reports/results.xml tests/'
                }
            }
        }
    }
    post {
        always {
            // Publier les résultats des tests
            junit 'reports/results.xml'
            archiveArtifacts artifacts: 'reports/results.xml', allowEmptyArchive: true
        }
    }
}
