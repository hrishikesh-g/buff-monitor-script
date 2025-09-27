pipeline {
    agent any

    environment {
        // safe to show static values
        APP_ENV = 'production'
        // pull the three secrets from Jenkins credentials store
        BUFF_API_TOKEN = credentials('BUFF_API_TOKEN')
        TELEGRAM_BOT_TOKEN = credentials('TELEGRAM_BOT_TOKEN')
        TELEGRAM_CHAT_ID = credentials('TELEGRAM_CHAT_ID')
    }

    stages {
        stage('Checkout') {
            steps {
                // automatically clones your repo Jenkins is building
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                  echo "Installing Python requirements..."
                  python3 -m venv venv
                  . venv/bin/activate
                  pip install --upgrade pip
                  pip install -r requirements.txt
                '''
            }
        }

        stage('Run Script') {
            steps {
                sh '''
                  echo "Running buff-monitor-script with secrets..."
                  . venv/bin/activate
                  # export the secrets so your Python script can read them
                  export BUFF_API_TOKEN=$BUFF_API_TOKEN
                  export TELEGRAM_BOT_TOKEN=$TELEGRAM_BOT_TOKEN
                  export SECRET_KEY_3=$SECRET_KEY_3

                  # now run your script
                  python3 buff_script.py
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}
