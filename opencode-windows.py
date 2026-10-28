
import subprocess
import sys

def run_command(command, description):
    print(f"\n{'=' * 50}")
    print(f"Running: {description}")
    print(f"{'=' * 50}\n")

    try:
        subprocess.run(command, check=True, shell=True)
        print(f"\nSUCCESS: {description}")
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
        "npm install -g @opencode/cli",
        "Installing OpenCode AI Using npm"
    )

    print("\nAll installations completed successfully!")

if __name__ == "__main__":
    main()
