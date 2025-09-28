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

```mermaid
graph LR
    A[GitHub Repo] -- Git Push --> B(Jenkins Pipeline);
    B -- Deploy --> C[Azure VM];
    C --> D(systemd Buff Bot);
    D --> E[Telegram API];
