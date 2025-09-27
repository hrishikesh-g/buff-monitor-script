pipeline {
    agent any

    environment {
        // these are still available to your buff_bot.sh or python script if needed
        APP_ENV = 'production'
        BUFF_API_TOKEN = credentials('BUFF_API_TOKEN')
        TELEGRAM_BOT_TOKEN = credentials('TELEGRAM_BOT_TOKEN')
        TELEGRAM_CHAT_ID = credentials('TELEGRAM_CHAT_ID')
    }

    stages {
        stage('Checkout') {
            steps {
                // clones your repo to Jenkins workspace
                checkout scm
            }
        }

        stage('Deploy & Restart Service') {
            steps {
                sh '''
                    echo "Deploying new code to /home/ubuntu/buff-bot..."
                    # copy the repo to your live folder
                    sudo rsync -av --delete . /home/ubuntu/buff-bot/

                    # make scripts executable
                    sudo chmod +x /home/ubuntu/buff-bot/start_buff.sh
                    sudo chmod +x /home/ubuntu/buff-bot/buff_script.py

                    echo "Reloading & restarting buff-bot service..."
                    sudo systemctl daemon-reload
                    sudo systemctl restart buff-bot.service
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
