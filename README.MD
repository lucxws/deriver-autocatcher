# Deriver Discord Selboft

[![icon|icon](https://styles.redditmedia.com/t5_2utus2/styles/communityIcon_nlsut2fgerm71.png)](https://top.gg/bot/704130818339242094)

This tool was made for educational purposes
Use with responsibility
- This selfbot will automatically catch Pokémons, so you can touch grass lol
- **Selfbots are against discord t.o.s, i'm not responsible for any thing that happens in your account**

## Features
- Catches pokémon automatically
- Spam script to get spawns

Packages
------
- `discord` <https://discordpy.readthedocs.io/en/stable/api.html>
- `imagehash` <https://pypi.org/project/ImageHash/>
- `PIL` <https://pillow.readthedocs.io/en/stable/>

## Installation
Python - https://www.python.org/

In 'main.py' add your token and your guild ids.
```py
from src.bot import Deriver

token = ""
bot = Deriver(guilds_ids=[0000, 0000, 0000], enabled=True) 
bot.run(token, bot=False)
```
Installing the packages
```sh
pip install -r requirements.txt
python main.py
```

## Spammer (beta)
Go to 'spam/script.py' and edit your config
```py
TOKEN = ""
CHANNEL = 000000000000
DELAY = 3
AMOUNT = 4
```

### To be added
- [x] Cli logging for pokémons (easy)
- [ ] Webhook logging for pokémons (easy)
- [ ] Whitelist, blacklisted pokémons (easy)

### In future
- [ ] Catch event sniper
- [ ] Configuration System & Dashboard 
- [ ] Video Tutorial
- [ ] Legit system
- [ ] Egg hatcher

## License
MIT

