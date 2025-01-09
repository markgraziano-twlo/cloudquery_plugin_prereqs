import os
import subprocess

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def run_command(command, description):
    """Runs a shell command and provides feedback."""
    print(f"Starting: {description}")
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"{GREEN}✔ {description} completed successfully.{RESET}\n")
    except subprocess.CalledProcessError:
        print(f"{RED}✖ {description} failed. Please check your setup.{RESET}\n")

def is_homebrew_installed():
    """Check if Homebrew is installed."""
    return subprocess.run("which brew", shell=True, stdout=subprocess.PIPE).returncode == 0

def is_git_installed():
    """Check if Git is installed."""
    result = subprocess.run("git --version", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def is_python3_installed():
    """Check if Python 3 is installed."""
    result = subprocess.run("python3 --version", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def is_cloudquery_installed():
    """Check if CloudQuery CLI is installed."""
    result = subprocess.run("cloudquery --version", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def upgrade_pip():
    """Upgrade pip to the latest version."""
    print("Upgrading pip to the latest version...")
    try:
        subprocess.run("pip install --upgrade pip", shell=True, check=True)
        print(f"{GREEN}✔ pip upgraded successfully.{RESET}\n")
    except subprocess.CalledProcessError:
        print(f"{RED}✖ Failed to upgrade pip. Please check your setup.{RESET}\n")

def is_python_package_installed(package_name):
    """Check if a Python package is installed."""
    result = subprocess.run(f"pip show {package_name}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def main():
    # Install Homebrew
    if not is_homebrew_installed():
        run_command(
            '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',
            "Installing Homebrew"
        )
    else:
        print(f"{GREEN}✔ Homebrew is already installed.{RESET}\n")

    # Install Git
    if not is_git_installed():
        run_command("brew install git", "Installing Git")
    else:
        print(f"{GREEN}✔ Git is already installed.{RESET}\n")

    # Install Python
    if not is_python3_installed():
        run_command("brew install python", "Installing Python")
    else:
        print(f"{GREEN}✔ Python 3 is already installed.{RESET}\n")

    # Upgrade pip
    upgrade_pip()

    # Install CloudQuery CLI
    if not is_cloudquery_installed():
        run_command("brew install cloudquery/tap/cloudquery", "Installing CloudQuery CLI")
    else:
        print(f"{GREEN}✔ CloudQuery CLI is already installed.{RESET}\n")

    # Install Python packages
    if not is_python_package_installed("cloudquery-plugin-sdk"):
        run_command("pip install cloudquery-plugin-sdk", "Installing CloudQuery Python SDK")
    else:
        print(f"{GREEN}✔ CloudQuery Python SDK is already installed.{RESET}\n")

if __name__ == "__main__":
    main()
