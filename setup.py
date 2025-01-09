import os
import subprocess
from ssh_setup import setup_ssh_key  # Import SSH setup functionality

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

def is_python3_installed():
    """Check if Python 3 is installed."""
    result = subprocess.run("python3 --version", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def upgrade_homebrew():
    """Upgrade Homebrew to the latest version."""
    if is_homebrew_installed():
        run_command("brew update", "Updating Homebrew")
    else:
        print(f"{RED}✖ Homebrew is not installed. Please install Homebrew manually if needed.{RESET}\n")

def upgrade_python():
    """Upgrade Python to the latest version."""
    if is_python3_installed():
        run_command("brew upgrade python", "Upgrading Python")
    else:
        print(f"{RED}✖ Python 3 is not installed. Please install Python 3 manually if needed.{RESET}\n")

def main():
    # Upgrade Homebrew
    upgrade_homebrew()

    # Upgrade Python
    upgrade_python()

    # Install or Upgrade GitHub CLI
    run_command("brew install gh || brew upgrade gh", "Installing or upgrading GitHub CLI")

    # Install CloudQuery CLI
    run_command("brew install cloudquery/tap/cloudquery || brew upgrade cloudquery", "Installing or upgrading CloudQuery CLI")

    # Install Python packages
    run_command("pip install --upgrade cloudquery-plugin-sdk", "Installing or upgrading CloudQuery Python SDK")

    # SSH Key Setup
    setup_ssh_key()  # Call the SSH setup function

if __name__ == "__main__":
    main()
