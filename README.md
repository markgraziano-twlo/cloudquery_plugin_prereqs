# Custom CloudQuery Plugin Prerequisites

This repository contains a script to automate the installation of prerequisites for setting up your custom CloudQuery plugin development environment. It ensures all necessary tools and dependencies are installed, configured, and ready to use.

---
## Manual Administrative Tasks
Before proceeding with the script, please ensure you have completd the following manual tasks: 
1. Request Access to CloudQuery in [#help-operational-insights](https://twilio.slack.com/app_redirect?channel=help-operational-insights)
2. Request Just-In-Time access to the `cloudquery-twilio` AWS Account by following the steps [here](https://internal-product-docs.twilio.com/docs/amazon-web-services/aws-access-management/aws-jit-access/?q=jit+access#request-aws-jit-access) 
3. Request Access to GitHub Copilot by submitting a ticket [here](https://twilio.service-now.com/sp?id=sc_cat_item&sys_id=035b188a87b2d55061197b9acebb3566).
    - Organization: Twilio
    - Application: GitHub Copilot License
4. Set up your GitHub Copilot IDE following [these instructions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot). *For more details see Twilio’s [Internal Product Docs](https://internal-product-docs.twilio.com/docs/operational-insights/guides/how-to-create-a-custom-cloudquery-plugin)*

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
#### Install Homebrew and Python:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && brew install python && curl -fsSL https://raw.githubusercontent.com/markgraziano-twlo/cloudquery_plugin_prereqs/refs/heads/main/setup.py | python3
```
#### Authenticate GitHub CLI:
```bash
gh auth login -s admin:public_key
```
Follow these steps during the gh auth login process:

- Where do you use GitHub?: Choose GitHub.com.
- What is your preferred protocol?: Choose HTTPS.
- Authenticate Git with your GitHub credentials?: Answer Y.
- How would you like to authenticate GitHub CLI?: Choose Login with a web browser.
  - Copy the one-time code provided in the terminal
  - Hit Enter in the termainal to launch your browser.
  - Select the account you want to authenticate (your twilio-internal account) 
  - Paste the one-time code into the browser prompt and click Authorize GitHub.
  - Return to the terminal once authentication is complete.

#### Install all remaining prerequisites and add GitHub SSH key:
```bash
curl -fsSL https://raw.githubusercontent.com/markgraziano-twlo/cloudquery_plugin_prereqs/refs/heads/main/setup.py | python3
```

### **Scenario 2: For Users WITH Homebrew and Python Already Installed**
#### Authenticate GitHub CLI:
```bash
gh auth login -s admin:public_key
```

#### Install all remaining prerequisites and add GitHub SSH key:
```bash
curl -fsSL https://raw.githubusercontent.com/markgraziano-twlo/cloudquery_plugin_prereqs/refs/heads/main/setup.py | python3
