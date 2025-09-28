# Buff Bot Automation

## Overview

**Buff Bot** is an automated monitoring and notification tool deployed on an **Azure VM**.
It leverages **Jenkins CI/CD** for automated deployments, **systemd** for continuous execution, and integrates with **Telegram Bot API** to send real-time alerts.

This project ensures seamless automation from code commit to deployment without manual intervention.

---

## Features

-   **Automated Deployment:** Pulls code from GitHub and deploys on Azure VM automatically.
-   **Secrets Management:** Securely handles API tokens via Jenkins credentials.
-   **Continuous Execution:** Python script runs every 2 minutes through systemd service.
-   **Notifications:** Sends updates and alerts to a Telegram chat.
-   **Environment Isolation:** Uses Python virtual environments to avoid dependency conflicts.

---

## Architecture

This diagram illustrates the core components and flow of the Buff Bot system:

    ```mermaid
    graph LR
        A[GitHub Repo] -- Git Push --> B(Jenkins Pipeline);
        B -- Deploy --> C[Azure VM];
        C --> D(systemd Buff Bot);
        D --> E[Telegram API];

## Flow

1.  Developer pushes code to **GitHub**.
2.  **Webhook** triggers **Jenkins pipeline**.
3.  Jenkins deploys code to **Azure VM** and sets environment variables.
4.  **Systemd** starts the bot script in a loop.
5.  Bot interacts with **Telegram API** and sends notifications.

---

## Pipeline Flow

The deployment process is fully automated via this pipeline:

    ```mermaid
    sequenceDiagram
        participant D as Developer
        participant G as GitHub
        participant J as Jenkins
        participant V as Azure VM
        participant S as systemd
        participant T as Telegram
    
        D->>G: Code Commit (Push)
        G->>J: Webhook Trigger
        J->>V: Clone Repo & Rsync to /home/ubuntu/buff-bot
        J->>V: Write .env Secrets
        J->>V: Make Scripts Executable
        J->>S: systemd Reload & Restart buff-bot.service
        S->>V: Buff Bot Script Runs (Every 120s)
        V->>T: Sends Notifications/Alerts

## Detailed Pipeline Steps

1.  **Code Commit** triggers Jenkins via **GitHub webhook**.
2.  Jenkins clones the repository to the workspace.
3.  Code is deployed to `/home/ubuntu/buff-bot` on the VM using **rsync**.
4.  Scripts are made executable.
5.  **Systemd service reloads and restarts `buff-bot.service`**.
6.  Buff Bot script runs continuously every **120 seconds**.
7.  Telegram receives updates.

---

## Tech Stack

| Category | Tool/Technology |
| :--- | :--- |
| **CI/CD** | Jenkins Pipeline |
| **Cloud** | Azure VM |
| **Scripting** | Bash + Python3 |
| **Automation** | systemd, rsync |
| **Secrets Management** | Jenkins credentials |
| **Messaging API** | Telegram Bot API |

---

## Setup & Deployment

1.  **Azure VM Setup:** Create Ubuntu VM with Python 3 and Jenkins installed.
2.  **Jenkins Setup:** Configure pipeline with secrets (`BUFF_API_TOKEN`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`).
3.  **Systemd Service:** Create `buff-bot.service` to run `start_buff.sh` in loop.
4.  **Pipeline Deployment:** Jenkins will clone repo, deploy scripts, write secrets to `.env`, set permissions, and restart service.

---

## Usage

-   Deployment triggers: **GitHub webhook** or **manual Jenkins run**.
-   Script execution: runs every **120 seconds** automatically.
-   Notifications: sent to configured **Telegram chat**.

---

## Security

-   `.env` is **not stored in GitHub**; secrets are handled via **Jenkins credentials**.
-   Deployment ensures `.env` file is written securely on the VM only.
-   Scripts run with proper execution permissions using `chmod`.
---
