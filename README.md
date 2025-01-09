# Custom CloudQuery Plugin Prerequisites

This repository contains a script to automate the installation of prerequisites for setting up your custom CloudQuery plugin development environment. It ensures all necessary tools and dependencies are installed, configured, and ready to use.

---

## **What This Script Does**
1. Updates **Homebrew** and **Python 3** (if already installed).
2. Installs or upgrades:
   - **GitHub CLI** (`gh`)
   - **CloudQuery CLI**
   - **CloudQuery Python SDK**
3. Sets up an **SSH key** for twilio-internal GitHub (if required).
   - The script will automatically check if the SSH key id_rsa_twilio_internal exists on your Twilio work laptop.
   - If the key is missing, it generates a new one and uploads it to GitHub using the GitHub CLI.

---

## **Usage**

### **Scenario 1: For Users WITHOUT Homebrew or Python Already Installed**
Install Homebrew and Python:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && brew install python && curl -fsSL https://raw.githubusercontent.com/markgraziano-twlo/cloudquery_plugin_prereqs/refs/heads/main/setup.py | python3
```
Authenticate GitHub CLI:
```bash
gh auth login -s admin:public_key
```

Install all remaining prerequisites and add GitHub SSH key:
```bash
curl -fsSL https://raw.githubusercontent.com/markgraziano-twlo/cloudquery_plugin_prereqs/refs/heads/main/setup.py | python3
```

### **Scenario 2: For Users WITH Homebrew and Python Already Installed**
Authenticate GitHub CLI:
```bash
gh auth login -s admin:public_key
```

Install all remaining prerequisites and add GitHub SSH key:
```bash
curl -fsSL https://raw.githubusercontent.com/markgraziano-twlo/cloudquery_plugin_prereqs/refs/heads/main/setup.py | python3
