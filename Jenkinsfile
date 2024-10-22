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
                // S'assurer que le bon environnement Python est utilisé
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                // Exécuter les tests avec le rapport au format JUnit
                sh 'pytest --junitxml=reports/results.xml tests/'
            }
        }
    }
    post {
        always {
            // Publier les résultats des tests JUnit
            junit 'reports/results.xml'  // Vérifier que le chemin est correct
            // Archiver d'autres artefacts si nécessaire, ajuster selon tes besoins
            archiveArtifacts artifacts: '**/*.py', allowEmptyArchive: true  // Exemple pour archiver tous les fichiers Python
        }
    }
}
