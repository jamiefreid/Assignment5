pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
            }
        }
        stage('Test') {
            steps {
                echo 'Running automated verification test suites...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
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