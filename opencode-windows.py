import subprocess
import sys

def run_command(command, description):
    print(f"\n{'=' * 50}")
    print(f"Running: {description}")
    print(f"{'=' * 50}\n")

    try:
        # Removed check=True so we can manually evaluate the exit code
        result = subprocess.run(command, shell=True) 
        
        # 0 = Success
        # 2316632107 = Winget code for "Already installed / No update available"
        if result.returncode in (0, 2316632107):
            if result.returncode == 2316632107:
                print(f"\nNOTE: Node.js is already installed and up to date.")
            print(f"SUCCESS: {description}")
        else:
            raise subprocess.CalledProcessError(result.returncode, command)
            
    except subprocess.CalledProcessError as e:
        print(f"\nERROR: {description} failed (exit code {e.returncode})")
        sys.exit(e.returncode or 1)

def main():
    # Step 1: Install Node.js LTS using winget
    run_command(
        "winget install --id OpenJS.NodeJS.LTS --exact --accept-package-agreements --accept-source-agreements",
        "Installing Node.js LTS"
    )

    # Step 2: Install OpenCode AI globally using npm
    run_command(
        "npm install -g opencode-ai",
        "Installing OpenCode AI"
    )

    print("\nAll installations completed successfully!")

if __name__ == "__main__":
    main()
