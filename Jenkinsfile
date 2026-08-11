pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                    cd backend
                    python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    cd backend
                    python3 -m pytest
                '''
            }
        }

        stage('Docker Build') {
    steps {
        sh '''
            export PATH="/usr/local/bin:$PATH"
            docker compose build
        '''
    }
}

stage('Docker Run & API Test') {
    steps {
        sh '''
            export PATH="/usr/local/bin:$PATH"

            docker compose up -d

            sleep 5

           curl -f http://localhost:5001/tasks

            docker compose down
        '''
    }
}
    }
}