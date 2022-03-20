import requests
import time
import random
import threading

TOKEN = ""
CHANNEL = 000000000000
DELAY = 3
AMOUNT = 4

def random_chars() -> str:
    return "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for i in range(0, random.randint(1, 20)))

def spam_channel(token: str, channel_id=str, content=str, delay=float, amount=int) -> None:
    
    base_url = f"https://canary.discord.com/api/v9/channels/{channel_id}/messages"
    headers =  {"Authorization": token}
    data = {"content": content}

    for _ in range(amount):
        r = requests.post(base_url, headers=headers, data=data)
        
        if r.status_code != 200:
            print(f"Error: {r.status_code} | {r.text}")
                
        time.sleep(delay)


while True:
    thread = threading.Thread(target=spam_channel(TOKEN, CHANNEL, random_chars(), DELAY, AMOUNT))
    thread.start()

            


   