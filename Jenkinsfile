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
                sh 'pip install pytest'  // Installer pytest
            }
        }
        stage('Run tests') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
    post {
        always {
            junit 'tests/*.xml'
            archiveArtifacts artifacts: '**/target/*.jar', allowEmptyArchive: true
        }
    }
}
