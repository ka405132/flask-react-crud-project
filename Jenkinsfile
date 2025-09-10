pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        echo "Building docker images..."
        sh 'docker compose build --no-cache'
      }
    }

    stage('Deploy') {
      steps {
        echo "Starting containers..."
        sh 'docker compose down || true'
        sh 'docker compose up -d'
      }
    }

    stage('Smoke Test') {
      steps {
        echo "Running smoke test..."
        sh '''
          sleep 5
          if ! curl -f http://localhost:5000/items; then
            echo "Smoke test failed"
            exit 1
          fi
        '''
      }
    }
  }

  post {
    success { echo '✅ Pipeline finished successfully' }
    failure { echo '❌ Pipeline failed — check console output' }
  }
}

