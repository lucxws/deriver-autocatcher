# 🤖 | Deriver Discord Selboft

[![icon|icon](https://styles.redditmedia.com/t5_2utus2/styles/communityIcon_nlsut2fgerm71.png)](https://top.gg/bot/704130818339242094)

> This selfbot will automatically catch Pokémons, so you can touch grass lol\n
> Selfbots are against discord t.o.s, i'm not responsible for any damage.
> This tool was made for educational purposes

## Features
- Catches pokémon with 2 desired names (base, cjk)
- Spam script to get spawns

## Packages
- [discord] - https://discordpy.readthedocs.io/en/stable/api.html
- [imagehash] - https://pypi.org/project/ImageHash/
- [PIL] - https://pillow.readthedocs.io/en/stable/

## Installation
Python - https://www.python.org/
I used version 3.8.0 btw

Add your token in '.env'
```env
TOKEN="mfa..."
```
Inside 'main.py', add the guild ids.
In your command prompt
```sh
pip install -r requirements.txt
python main.py
```

## Spammer (beta)
Go to 'spam.py' and edit **TOKEN** and **CHANNEL** global variables
```py
TOKEN=""
CHANNEL=0000
```
You can also change the delay in line 39

### To be added
- [x] Cli logging for pokémons (easy)
- [ ] Webhook logging for pokémons (easy)
- [ ] Whitelist, blacklist pokémons (easy)
- Catch event.... 🤔

## License
MIT
