pipeline {
    agent any

    environment {
        APP_NAME = 'Jenkins-CI-Demo'
    }

    parameters {
        string(name: 'DEPLOY_ENV', defaultValue: 'Staging', description: 'Target environment for deployment (e.g., Staging, Production)')
    }

    stages {
        stage('Build') {
            steps {
                echo "Building the application: ${env.APP_NAME}..."
            }
        }
        stage('Test') {
            steps {
                echo 'Running automated verification test suites...'
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying ${env.APP_NAME} to the ${params.DEPLOY_ENV} environment..."
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