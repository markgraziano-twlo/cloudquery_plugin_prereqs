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
   - The script will automatically check if the SSH key id_rsa_twilio_internal exists.
   - If the key is missing, it generates a new one and uploads it to GitHub using the GitHub CLI.

---

## **Usage**

### **Scenario 1: For Users WITHOUT Homebrew or Python Already Installed**
Run the following single-line command to install Homebrew, Python, and all other prerequisites:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && brew install python && curl -fsSL https://raw.githubusercontent.com/markgraziano-twlo/cloudquery_plugin_prereqs/refs/heads/main/setup.py | python3
```
## **Scenario 2: For Users WITH Homebrew and Python Already Installed**
Run this command to install all remaining prerequisites:

```bash
curl -fsSL https://raw.githubusercontent.com/markgraziano-twlo/cloudquery_plugin_prereqs/refs/heads/main/setup.py | python3
