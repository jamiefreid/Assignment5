pipeline {
    agent any

    environment {
        AWS_REGION = "us-east-1" 
        ECR_REPO_URI = "524843733539.dkr.ecr.us-east-1.amazonaws.com/assignment5"
        IMAGE_NAME = "assignment5"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/jamiefreid/Assignment5.git'
            }
        }
        stage('Test') {
            steps {
                echo 'Running automated verification test suites...'
                bat 'pip install -r requirements.txt'
                bat 'python -m unittest test_app.py'
            }
        }
        stage('Build and Tag Image') {
            steps {
                // Build the image locally
                bat "docker build -t ${env.IMAGE_NAME}:latest ."
                // Tag the image specifically for the AWS ECR repository
                bat "docker tag ${env.IMAGE_NAME}:latest ${env.ECR_REPO_URI}:latest"
            }
        }
        stage('Push to AWS ECR') {
            steps {
                withAWS(region: "${env.AWS_REGION}", credentials: 'aws-creds') {
                    // Fetch the ECR credentials
                    bat "aws ecr get-login-password --region ${env.AWS_REGION}| docker login --username AWS --password-stdin ${env.ECR_REPO_URI}"
                    
                    // Push the tagged image
                    bat "docker push ${env.ECR_REPO_URI}:latest"
                    
                    // Securely log out
                    bat "docker logout ${env.ECR_REPO_URI}"
                }
            }
        }
    }
    post {
        success {
            bat 'echo BUILD SUCCESSFUL: Pushed to AWS ECR.'
        }
        failure {
            bat 'echo BUILD FAILED: Check the logs for errors.'
        }
    }
}