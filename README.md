# Custom CloudQuery Plugin Prerequisites

This repository contains a script to automate the installation of prerequisites for setting up your custom CloudQuery plugin development environment. It ensures all necessary tools and dependencies are installed, configured, and ready to use.

---

## **What This Script Does**
1. Installs **Homebrew** (if not already installed).
2. Installs **Git** (if not already installed).
3. Installs the latest stable version of **Python 3** via Homebrew.
4. Ensures **pip** (Python's package manager) is up-to-date.
5. Installs the **CloudQuery Python SDK** (`cloudquery-plugin-sdk`).
6. Installs the **CloudQuery CLI**

Additionally:
- Checks for existing installations of these tools to avoid unnecessary installations.
- Upgrades outdated versions of `pip`.

---

## **Usage**

Run the following command in your terminal to install all prerequisites:

```bash
curl -fsSL https://raw.githubusercontent.com/markgraziano-twlo/cloudquery_plugin_prereqs/refs/heads/main/setup.py | python3
