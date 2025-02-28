#!/usr/bin/env python3
import sys
import re
import requests

# Replace with your actual Discord webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_ID/YOUR_WEBHOOK_TOKEN"

def send_to_discord(join_code):
    """Send the join code to the Discord channel via webhook."""
    data = {"content": join_code}
    try:
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code == 204:
            print("Discord webhook sent successfully!")
        else:
            print(f"Failed to send webhook: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error sending webhook: {e}")

def main():
    # Compile the regex to capture the join code (assuming it's a sequence of letters/digits)
    pattern = re.compile(r"Session short code:\s*([A-Z0-9]+)")
    already_sent = False  # Optional: prevents sending duplicate codes

    for line in sys.stdin:
        # Optionally, print the log normally
        sys.stdout.write(line)
        sys.stdout.flush()

        match = pattern.search(line)
        if match and not already_sent:
            join_code = match.group(1)
            send_to_discord(join_code)
            already_sent = True  # Remove or adjust this if your code might change periodically

if __name__ == "__main__":
    main()
