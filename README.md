# CloudQuery Prerequisites

This repository contains a standalone executable that automates the setup of your CloudQuery plugin development environment. The tool ensures all necessary tools and dependencies are installed, configured, and ready to use, eliminating the need for manual installations or scripts.

---
## Manual Administrative Tasks
Before proceeding with the script, please ensure you have completed the following manual tasks: 
1. Request Access to CloudQuery in [#help-operational-insights](https://twilio.slack.com/app_redirect?channel=help-operational-insights)
2. Request Just-In-Time access to the `cloudquery-twilio` AWS Account by following the steps [here](https://internal-product-docs.twilio.com/docs/amazon-web-services/aws-access-management/aws-jit-access/?q=jit+access#request-aws-jit-access) 
3. Request Access to GitHub Copilot by submitting a ticket [here](https://twilio.service-now.com/sp?id=sc_cat_item&sys_id=035b188a87b2d55061197b9acebb3566).
    - Organization: Twilio
    - Application: GitHub Copilot License
4. Set up your GitHub Copilot IDE following [these instructions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot). *For more details see Twilio’s [Internal Product Docs](https://internal-product-docs.twilio.com/docs/operational-insights/guides/how-to-create-a-custom-cloudquery-plugin)*

---

## **What This Tool Does**
1. Updates **Homebrew** and **Python 3** (if already installed).
2. Installs or upgrades:
   - **GitHub CLI** (`gh`)
   - **CloudQuery CLI**
   - **CloudQuery Python SDK**
3. Sets up an **SSH key** for twilio-internal GitHub (if required).
   - The tool automatically checks if the SSH key `id_rsa_twilio_internal` exists on your Twilio work laptop.
   - If the key is missing, it generates a new one, adds it to the SSH agent, and uploads it to GitHub using the GitHub CLI.
   - 🚨 You must manually authorize your newly added SSH key for SAML SSO. The tool will automatically open the browser for you to perform that step. 🌐

---

## **Usage**

### **Quick Start**
To get started, run the following command in your terminal:

```bash
curl -LJO https://github.com/markgraziano-twlo/cloudquery_plugin_prereqs/releases/latest/download/cloudquery-prereqs && chmod +x cloudquery-prereqs && ./cloudquery-prereqs
```

### **What to Expect During Execution:**
1. **Homebrew Installation/Update:**
   - The tool installs or updates Homebrew automatically.

2. **Python Installation/Update:**
   - Ensures Python 3 is installed and up to date.

3. **GitHub CLI Installation and Authentication:**
   - Installs or updates the GitHub CLI.
   - Prompts you to authenticate with GitHub using the `admin:public_key` scope.

4. **SSH Key Configuration:**
   - If the `id_rsa_twilio_internal` key does not exist, it will be created and added to GitHub.
   - The tool opens the GitHub SSH settings page for you to authorize the key for SAML SSO.

5. **CloudQuery CLI and SDK Installation:**
   - Installs or upgrades the CloudQuery CLI and Python SDK.

---

### Post-Setup Steps
After completing the setup, you’ll need to manually:
- Authorize your SSH key for SAML SSO by clicking the **Configure SSO** button on the GitHub SSH settings page.

Once all steps are complete, you’re ready to start developing with CloudQuery!

---

## Additional Information
If you encounter issues during setup or require additional access, please review the following steps:

- **Request Access to CloudQuery:**
  - Reach out in the `#help-operational-insights` Slack channel.

- **Request Just-In-Time Access to the `cloudquery-twilio` AWS Account:**
  - Follow the steps in Twilio’s internal documentation.

- **Request Access to GitHub Copilot:**
  - Submit a ticket with the following details:
    - **Organization:** Twilio
    - **Application:** GitHub Copilot License

- **Set Up GitHub Copilot in Your IDE:**
  - Follow the instructions in Twilio’s internal product documentation.

---

## Troubleshooting
If you encounter issues with the tool or setup process:
1. Ensure your macOS version supports the tool.
2. Verify network connectivity, as the tool downloads several dependencies.
3. For Gatekeeper warnings, right-click the executable, select **Open**, and confirm the prompt.

---

## Contributing
Contributions to this repository are welcome. Please submit a pull request or raise an issue for any improvements or bug fixes.

