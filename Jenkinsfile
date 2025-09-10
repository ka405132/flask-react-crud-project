pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/ka405132/flask-react-crud-project.git',
                    credentialsId: 'github-token'
            }
        }

        stage('Build') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose up -d'
            }
        }

        stage('Smoke Test') {
            steps {
                sh 'sleep 10 && curl -f http://localhost:5000/items'
            }
        }
    }
}

