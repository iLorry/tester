pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'echo Building...'
                bat 'pipenv run python src/main.py Building...'
            }
        }
        stage('Test') {
            steps {
                bat 'echo Testing...'
                bat 'pipenv run python src/main.py Testing...'
                bat 'pipenv run python src/test_main.py'
            }
        }
        stage('Deploy') {
            steps {
                bat 'echo Deploying...'
                bat 'pipenv run python src/main.py Deploying...'
            }
        }
    }
}
