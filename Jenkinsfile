pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Bharath179/Solaris.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                 bat 'pytest -s -v test_cases/dashboard1.py --browser=chrome --html=reports\\test_report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', fingerprint: true
        }
    }
}
