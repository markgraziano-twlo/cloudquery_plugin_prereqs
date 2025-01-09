import os
import subprocess

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def run_command(command, description):
    """Runs a shell command and provides feedback."""
    print(f"Starting: {description}")
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"{GREEN}✔ {description} completed successfully.{RESET}\n")
    except subprocess.CalledProcessError:
        print(f"{RED}✖ {description} failed. Please check your setup.{RESET}\n")

def setup_ssh_key():
    """Sets up an SSH key for GitHub without user interaction."""
    print(f"{YELLOW}Setting up an SSH key for GitHub access...{RESET}")
    
    ssh_dir = os.path.expanduser("~/.ssh")
    os.makedirs(ssh_dir, exist_ok=True)  # Ensure the .ssh directory exists
    key_name = "id_rsa_twilio_internal"
    key_path = os.path.join(ssh_dir, key_name)

    # Check if the key already exists
    if os.path.exists(key_path):
        print(f"{GREEN}✔ SSH key already exists at {key_path}. Skipping key generation.{RESET}")
    else:
        # Generate SSH key
        print(f"{YELLOW}Generating a new SSH key...{RESET}")
        subprocess.run(["ssh-keygen", "-t", "rsa", "-b", "4096", "-f", key_path, "-N", ""], check=True)

    # Add key to SSH agent
    print(f"{YELLOW}Adding the SSH key to the SSH agent...{RESET}")
    subprocess.run("eval \"$(ssh-agent -s)\"", shell=True, check=True)
    subprocess.run(["ssh-add", key_path], check=True)

    # Add public key to GitHub using gh
    public_key_path = f"{key_path}.pub"
    print(f"{YELLOW}Adding the SSH key to GitHub...{RESET}")
    subprocess.run(["gh", "ssh-key", "add", public_key_path, "--title", "Work Laptop - Twilio Internal"], check=True)

   # Test the SSH connection
    print(f"{YELLOW}Testing the SSH connection to GitHub...{RESET}")
    result = subprocess.run("ssh -T git@github.com", shell=True, text=True, capture_output=True)
    if result.returncode == 0:
        print(f"{GREEN}✔ SSH connection to GitHub successful!{RESET}")
    else:
        print(f"{RED}✖ SSH setup failed: {result.stderr.strip()}{RESET}")
        if "does not provide shell access" in result.stderr:
            print(f"{GREEN}This message is normal. GitHub does not provide shell access. Your SSH key is still working for Git operations.{RESET}")


def main():
    # Upgrade Homebrew
    run_command("brew update", "Updating Homebrew")

    # Upgrade Python
    run_command("brew upgrade python", "Upgrading Python")

    # Install or Upgrade GitHub CLI
    run_command("brew install gh || brew upgrade gh", "Installing or upgrading GitHub CLI")

    # Install CloudQuery CLI
    run_command("brew install cloudquery/tap/cloudquery || brew upgrade cloudquery", "Installing or upgrading CloudQuery CLI")

    # Install Python packages
    run_command("pip install --upgrade cloudquery-plugin-sdk", "Installing or upgrading CloudQuery Python SDK")

    # SSH Key Setup
    setup_ssh_key()

if __name__ == "__main__":
    main()
