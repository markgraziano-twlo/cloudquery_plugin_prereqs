import os
import subprocess

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def setup_ssh_key():
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
