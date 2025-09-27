#!/bin/bash

APP_DIR="/home/ubuntu/buff-bot"

cd "$APP_DIR" || exit 1

# activate virtualenv if exists
if [ -f "venv/bin/activate" ]; then
  source venv/bin/activate
fi

# loop forever, run script every 120 seconds
while true; do
  echo "$(date) - Starting buff_script.py"
  python3 buff_script.py
  echo "$(date) - Finished. Sleeping for 120 seconds..."
  sleep 120
done
