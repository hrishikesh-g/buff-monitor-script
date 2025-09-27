pipeline {
    agent any  // run on the Jenkins master itself
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/hrishikesh-g/buff-monitor-script.git'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh '. venv/bin/activate && pytest'
            }
        }
        stage('Deploy') {
            steps {
                // Example: copy files to /home/ubuntu/buff-bot-live
                sh 'rsync -avz . /home/ubuntu/buff-bot-live/'
                // or run a systemctl restart your-app
            }
        }
    }
}
