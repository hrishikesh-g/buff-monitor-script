# buff-monitor-script

# Buff Marketplace Monitor

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/<your-username>/<your-repo>/run_script.yml?branch=main)

## Overview

**Buff Marketplace Monitor** is an automated Python script that monitors items on the [Buff](https://buff.game) PC marketplace and sends real-time notifications to Telegram.  
This repo is fully GitHub Actions-ready, so the script runs automatically on a schedule without any manual intervention.

---

## Features

- ✅ Fetches the latest 100 items from Buff Marketplace (Regular & Premium)  
- ✅ Sends Telegram notifications with item details (Name, Price, Stock Status)  
- ✅ Fully automated using GitHub Actions  
- ✅ Easy to configure using GitHub Secrets for API tokens  

---

## Architecture

1. **Python Script (`buff-script.py`)**: Fetches items and posts messages to Telegram.  
2. **GitHub Actions Workflow**: Runs the script every minute (adjustable in `.github/workflows/run_script.yml`).  
3. **Secrets Management**: API tokens stored securely in GitHub Secrets.  

GitHub Actions
└─ Runs buff-script.py on schedule
Python Script
└─ Fetches Buff marketplace items → Sends Telegram notifications

## Setup Instructions

1. **Fork/Clone the repo**  

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

2. **Add GitHub Secrets**

Go to Settings → Secrets and variables → Actions → New repository secret and add:

Name	Value
BUFF_API_TOKEN	Your Buff API Bearer token
TELEGRAM_BOT_TOKEN	Your Telegram Bot token
TELEGRAM_CHAT_ID	Your Telegram chat ID

3. **Modify schedule (optional)**

Open .github/workflows/run_script.yml and change the cron schedule. Minimum interval is 1 minute.

## Usage

Once secrets are configured:

The script runs automatically according to the GitHub Actions schedule.

You will receive Telegram notifications for every new item fetched.

To run locally (for testing):

pip install -r requirements.txt
python buff-script.py

## Requirements

Python 3.x

Packages: requests, urllib3

GitHub Actions (for automation)

## Notes

GitHub Actions cannot run workflows more frequently than every 5 minutes.

For sub-minute execution (like 30 seconds), consider deploying on a VM or Azure Function.

## License

MIT License. Free to use, modify, and share.

Made with ❤️ and a little Python magic ✨
