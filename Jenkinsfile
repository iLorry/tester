pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'echo Building...'
                bat 'pipenv install'
                bat 'pipenv run python src/main.py Building...'
                bat 'sonar-scanner.bat'
            }
        }
        stage('Test') {
            steps {
                bat 'echo Testing...'
                bat 'pipenv install'
                bat 'pipenv run python src/main.py Testing...'
                bat 'python src/test_main.py'
            }
        }
        stage('Deploy') {
            steps {
                bat 'echo Deploying...'
                bat 'pipenv install'
                bat 'pipenv run python src/main.py Deploying...'
            }
        }
    }
}
