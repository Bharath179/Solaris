pipeline {
    agent any

//     triggers {
//         pollSCM('H/5 * * * *')
//     }

    options {
        disableConcurrentBuilds()
        timeout(time: 30, unit: 'MINUTES')
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Bharath179/Solaris.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\python.exe -m pytest -s -v test_cases/dashboard.py --browser=chrome --html=reports\\test_report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', fingerprint: true

            emailext (
                to: 'bharathkn179@gmail.com',
                subject: "${env.JOB_NAME} - Build #${env.BUILD_NUMBER} - ${currentBuild.currentResult}",
                body: """
                    <p>Build <b>${env.JOB_NAME} #${env.BUILD_NUMBER}</b> finished with status: <b>${currentBuild.currentResult}</b>.</p>
                    <p>Check details at: <a href='${env.BUILD_URL}'>Build Link</a></p>
                """,
                mimeType: 'text/html'
            )
        }
    }
}
