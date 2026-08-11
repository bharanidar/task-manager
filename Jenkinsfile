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
                    docker compose build
                '''
            }
        }
    }
}