# Buff Monitor Script 🛍️

---

## Buff Marketplace Monitor

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/your-username/your-repo/run_script.yml?branch=main)

---

## Overview

The **Buff Marketplace Monitor** is an **automated Python script** that monitors items on the [Buff](https://buff.game) PC marketplace and sends real-time notifications to Telegram. It's designed to be fully **GitHub Actions-ready**, allowing the script to run automatically on a set schedule without any manual intervention.

---

## Features

- ✅ Fetches the latest 100 items from both the Regular and Premium Buff Marketplaces.
- ✅ Sends **Telegram notifications** containing essential item details like its name, price, and current stock status.
- ✅ **Fully automated** using GitHub Actions for hands-free operation.
- ✅ **Easy to configure** by securely storing API tokens in GitHub Secrets.

---

## Architecture

1.  **Python Script (`buff-script.py`)**: The core of the tool, responsible for fetching marketplace data and sending messages to Telegram.
2.  **GitHub Actions Workflow**: A YAML file that schedules the script to run automatically. By default, it runs every minute, though this can be adjusted.
3.  **Secrets Management**: API tokens for both Buff and Telegram are stored securely as **GitHub Secrets**, preventing them from being exposed in the code.

```mermaid
graph TD
    A[GitHub Actions] --> B(Runs buff-script.py on schedule);
    B --> C[Python Script];
    C --> D[Fetches Buff marketplace items];
    D --> E[Sends Telegram notifications];

## Setup Instructions

1.  **Fork or Clone the repository**:

    ```bash
    git clone [https://github.com/](https://github.com/)<your-username>/<your-repo>.git
    cd <your-repo>
    ```

2.  **Add GitHub Secrets**:

    Navigate to **`Settings` → `Secrets and variables` → `Actions`** in your repository and add the following new repository secrets:

    | Name | Value |
    | :--- | :--- |
    | `BUFF_API_TOKEN` | Your Buff API Bearer token |
    | `TELEGRAM_BOT_TOKEN`| Your Telegram Bot token |
    | `TELEGRAM_CHAT_ID` | Your Telegram chat ID |

3.  **Modify the schedule (Optional)**:

    You can change how often the script runs by opening the `.github/workflows/run_script.yml` file and editing the cron schedule. The minimum interval for GitHub Actions is **one minute**.

---

## Usage

Once you've configured the secrets, the script will run automatically according to the GitHub Actions schedule. You will receive Telegram notifications for every new item fetched.

### To Run Locally (for testing):

1.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

2.  Execute the script:

    ```bash
    python buff-script.py
    ```

---

## Requirements

-   **Python 3.x**
-   **Python Packages**: `requests`, `urllib3`
-   **GitHub Actions** (for automation)

---

## Notes

-   GitHub Actions workflows cannot run more frequently than **every 5 minutes**. For sub-minute execution (e.g., every 30 seconds), consider deploying the script on a dedicated **VM** or using a service like **Azure Functions**.
-   The MIT License governs this project, meaning it's free to use, modify, and share.

---

Made with ❤️ and a little Python magic ✨
