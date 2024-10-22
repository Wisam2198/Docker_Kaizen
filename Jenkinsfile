pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Wisam2198/Docker_Kaizen.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                // Exécute les tests et génère le rapport dans le dossier reports
                sh 'pytest --junitxml=reports/results.xml tests/'
            }
        }
    }
    post {
        always {
            // Met à jour le chemin pour pointer vers le dossier reports
            junit 'reports/results.xml'
            archiveArtifacts artifacts: '**/target/*.jar', allowEmptyArchive: true
        }
    }
}
