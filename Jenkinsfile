pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'echo Building...'
                bat 'python main.py Building...'
            }
        }
        stage('Test') {
            steps {
                bat 'echo Testing...'
                bat 'python main.py Testing...'
                bat 'nosetests'
            }
        }
        stage('Deploy') {
            steps {
                bat 'echo Deploying...'
                bat 'python main.py Deploying...'
            }
        }
    }
}
