pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/bharanidar/task-manager.git'
            }
        }

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
                sh 'docker build -t task-manager-backend ./backend'
            }
        }
    }
}