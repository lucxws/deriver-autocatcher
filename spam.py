"""
Use this script to spam if you want to get some spawns
Deriver protection is kinda bad so don't be afraid
I'll add mutiple accs later
"""

import requests
import time
import random
import threading

TOKEN = "TOKEN_TO_SPAM"
CHANNEL = 000000000000

def random_chars() -> str:
    """
    generate a random string of characters
    """
    return "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for i in range(0, random.randint(1, 20)))

def spam_channel(channel_id, content=str):
    """
    spam a channel with a certain content.
    i tried to make this legit, i'm not familliar with threading tho..
    """
    base_url = f"https://canary.discord.com/api/v9/channels/{channel_id}/messages"
    headers =  {"Authorization": TOKEN}
    data = {"content": content}

    r = requests.post(base_url, headers=headers, data=data)
    
    if r.status_code != 200:
        if 'retry_after' in r.headers:
            time.sleep(int(r.headers['retry_after']))
            print(f"Retrying after {r.headers['retry_after']} seconds")
        else:
            print(f"Error: {r.status_code} | {r.text}")
            
    time.sleep(3)


if __name__ == "__main__":
    while True:
        thread = threading.Thread(target=spam_channel(CHANNEL, random_chars()))
        thread.start()

            


   