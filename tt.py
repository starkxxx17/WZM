import subprocess

# Run update.py
try:
    subprocess.run(["python3", "update.py"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Failed to run update.py: {e}")
    exit(1)  # Exit if update.py fails

# Proceed with running the bot
if __name__ == "__main__":
    # Your bot code here
    print("Starting the bot...")
    # Example bot code:
    # import your_bot_module
    # your_bot_module.run()
