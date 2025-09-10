pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ka405132/flask-react-crud-project.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker compose up -d'
            }
        }

        stage('Verify Services') {
            steps {
                sh 'docker ps'
                sh 'curl -f http://localhost:5000 || exit 1'
                sh 'curl -f http://localhost:3000 || exit 1'
            }
        }
    }

    post {
        success {
            echo '🚀 Deployment successful! Flask & React are up.'
        }
        failure {
            echo '❌ Build failed. Check logs.'
        }
    }
}

