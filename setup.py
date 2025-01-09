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
    """Sets up an SSH key for GitHub."""
    print(f"{YELLOW}Next, we'll set up an SSH key for GitHub access. Please ensure you're logged into the GitHub account used for the twilio-internal organization.{RESET}\n")
    response = input("Do you need to create a new SSH key? (Y/N): ").strip().lower()

    if response == "y":
        print("\nLet's create a new SSH key.")
        ssh_dir = os.path.expanduser("~/.ssh")
        key_name = "id_rsa_twilio_internal"
        key_path = os.path.join(ssh_dir, key_name)

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
        result = subprocess.run("ssh -T git@github.com", shell=True)
        if result.returncode == 0:
            print(f"{GREEN}✔ SSH setup completed successfully!{RESET}")
        else:
            print(f"{RED}✖ SSH setup failed. Please troubleshoot the connection.{RESET}")

    elif response == "n":
        print(f"{YELLOW}Testing existing SSH keys...{RESET}")
        test_result = subprocess.run("ssh -T git@github.com", shell=True)
        if test_result.returncode == 0:
            print(f"{GREEN}✔ Existing SSH key works successfully!{RESET}")
        else:
            print(f"{RED}Existing SSH key does not work.{RESET}")
            retry = input("Would you like to create a new SSH key? (Y/Exit): ").strip().lower()
            if retry == "y":
                setup_ssh_key()
            else:
                print(f"{RED}Exiting the script. Please set up the SSH key manually if needed.{RESET}")
    else:
        print(f"{RED}Invalid input. Exiting script.{RESET}")

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
