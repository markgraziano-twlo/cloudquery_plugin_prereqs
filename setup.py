import os
import subprocess

def run_command(command, description):
    """Runs a shell command and provides feedback."""
    print(f"Starting: {description}")
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"✔ {description} completed successfully.\n")
    except subprocess.CalledProcessError:
        print(f"✖ {description} failed. Please check your setup.\n")

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

def upgrade_pip():
    """Upgrade pip to the latest version."""
    print("Upgrading pip to the latest version...")
    try:
        subprocess.run("pip install --upgrade pip", shell=True, check=True)
        print("✔ pip upgraded successfully.\n")
    except subprocess.CalledProcessError:
        print("✖ Failed to upgrade pip. Please check your setup.\n")

def is_python_package_installed(package_name):
    """Check if a Python package is installed."""
    result = subprocess.run(f"pip show {package_name}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0
