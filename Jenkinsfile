pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "docker-kaizen"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Wisam2198/Docker_Kaizen.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Ajouter le numéro de build au tag Docker
                    sh 'docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Exécuter les tests dans le conteneur avec un volume pour les rapports
                    sh '''
                    mkdir -p reports
                    docker run --rm \
                        -v $(pwd)/reports:/app/reports \
                        ${DOCKER_IMAGE}:${BUILD_NUMBER} \
                        pytest --junitxml=/app/reports/results.xml tests/
                    '''
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
        success {
            echo 'Build réussi !'
        }
        failure {
            echo 'Échec du pipeline.'
        }
    }
}
