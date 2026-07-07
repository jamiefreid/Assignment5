pipeline {
    agent any

    environment {
        IMAGE_NAME = "jamiefreid/jenkins-flask-app" 
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/jamiefreid/Assignment5'
            }
        }
        stage('Test') {
            steps {
                echo 'Running automated verification test suites...'
                bat 'pip install -r requirements.txt'
                bat 'python -m unittest test_app.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat "docker build -t ${env.IMAGE_NAME}:latest ."
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                    bat """
                    echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                    docker push ${env.IMAGE_NAME}:latest
                    docker logout
                    """
                }
            }
        }
    }
    post {
        success {
            bat 'echo BUILD SUCCESSFUL: The pipeline executed without errors.'
        }
        failure {
            bat 'echo BUILD FAILED: An error occurred during execution.'
        }
    }
}