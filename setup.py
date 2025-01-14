import os
import subprocess

# ANSI color codes for terminal output
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def run_command(command, description):
    """Runs a shell command and waits for it to complete."""
    print(f"{YELLOW}Starting: {description}{RESET}")
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"{GREEN}✔ {description} completed successfully.{RESET}\n")
    except subprocess.CalledProcessError as e:
        print(f"{RED}✖ {description} failed: {e}{RESET}")
        exit(1)  # Exit if a critical step fails

def install_homebrew():
    """Installs Homebrew if not already installed."""
    print(f"{YELLOW}Checking for Homebrew installation...{RESET}")
    try:
        subprocess.run("brew --version", shell=True, check=True)
        print(f"{GREEN}✔ Homebrew is already installed.{RESET}\n")
    except subprocess.CalledProcessError:
        print(f"{YELLOW}Homebrew is not installed. Installing now...{RESET}")
        run_command(
            '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',
            "Installing Homebrew"
        )

def setup_ssh_key():
    """Sets up an SSH key for GitHub and handles user authorization."""
    print(f"{YELLOW}Setting up an SSH key for GitHub access...{RESET}")

    ssh_dir = os.path.expanduser("~/.ssh")
    os.makedirs(ssh_dir, exist_ok=True)  # Ensure the .ssh directory exists
    key_name = "id_rsa_twilio_internal"
    key_path = os.path.join(ssh_dir, key_name)

    if os.path.exists(key_path):
        print(f"{GREEN}✔ SSH key already exists at {key_path}. Skipping key generation.{RESET}")
    else:
        print(f"{YELLOW}Generating a new SSH key...{RESET}")
        run_command(f"ssh-keygen -t rsa -b 4096 -f {key_path} -N ''", "Generating SSH key")

    print(f"{YELLOW}Adding the SSH key to the SSH agent...{RESET}")
    run_command("eval \"$(ssh-agent -s)\" && ssh-add " + key_path, "Adding SSH key to SSH agent")

    public_key_path = f"{key_path}.pub"
    print(f"{YELLOW}Adding the SSH key to GitHub...{RESET}")
    add_key_result = subprocess.run(
        ["gh", "ssh-key", "add", public_key_path, "--title", "Work Laptop - Twilio Internal"],
        capture_output=True,
        text=True,
    )
    if add_key_result.returncode == 0:
        print(f"{GREEN}✔ SSH key successfully added to GitHub.{RESET}")
    elif "already exists" in add_key_result.stderr:
        print(f"{YELLOW}✔ SSH key already exists in GitHub. Skipping addition.{RESET}")
    else:
        print(f"{RED}✖ Failed to add SSH key to GitHub: {add_key_result.stderr.strip()}{RESET}")

    print(f"{YELLOW}Opening GitHub SSH keys settings page...{RESET}")
    run_command("open https://github.com/settings/keys", "Opening GitHub SSH settings page")

    print(f"{YELLOW}🚨 IMPORTANT: Manually configure the SSH key for SAML SSO authorization.{RESET}")
    print(f"{YELLOW}1. Locate the newly added SSH key titled 'Work Laptop - Twilio Internal'.{RESET}")
    print(f"{YELLOW}2. Click the 'Configure SSO' button next to the key.{RESET}")
    print(f"{YELLOW}3. Follow the prompts to authorize the key for your organization.{RESET}")
    input(f"{YELLOW}Press Enter after you have completed the SAML SSO configuration to continue...{RESET}")

    print(f"{YELLOW}Testing the SSH connection to GitHub...{RESET}")
    result = subprocess.run("ssh -T git@github.com", shell=True, text=True, capture_output=True)
    if result.returncode == 0:
        print(f"{GREEN}✔ SSH connection to GitHub successful!{RESET}")
    else:
        print(f"{RED}✖ SSH connection failed: {result.stderr.strip()}{RESET}")

def main():
    print(f"{YELLOW}Starting developer onboarding process...{RESET}\n")

    # Install Homebrew
    install_homebrew()

    # Install or Upgrade Python
    run_command("brew install python || brew upgrade python", "Installing or upgrading Python")

    # Install or Upgrade GitHub CLI
    run_command("brew install gh || brew upgrade gh", "Installing or upgrading GitHub CLI")

    # GitHub Authentication with admin:public_key scope
    print(f"{YELLOW}Next step: Authenticate with GitHub CLI (with admin:public_key scope).{RESET}")
    run_command("gh auth login --scopes 'admin:public_key'", "GitHub authentication")
    print(f"{GREEN}✔ GitHub authentication completed. Moving to the next step.{RESET}")

    # Install CloudQuery CLI
    run_command("brew install cloudquery/tap/cloudquery || brew upgrade cloudquery", "Installing or upgrading CloudQuery CLI")

    # Install Python SDK
    run_command("pip install --upgrade cloudquery-plugin-sdk", "Installing or upgrading CloudQuery Python SDK")

    # SSH Key Setup
    setup_ssh_key()

    print(f"{GREEN}✔ All steps completed successfully! Your environment is ready for use.{RESET}")

if __name__ == "__main__":
    main()
