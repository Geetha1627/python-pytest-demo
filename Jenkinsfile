
pipeline {
    agent any

    stages {
        stage('Check Python') {
            steps {
                bat '"C:\\Users\\Geetha M R\\AppData\\Local\\Programs\\Python\\Python315\\python.exe" --version'
            }
        }

        stage('Install Pytest') {
            steps {
                bat '"C:\\Users\\Geetha M R\\AppData\\Local\\Programs\\Python\\Python315\\python.exe" -m pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\Geetha M R\\AppData\\Local\\Programs\\Python\\Python315\\python.exe" -m pytest -v'
            }
        }
    }
}
