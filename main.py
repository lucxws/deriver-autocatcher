from os import getenv
from dotenv import load_dotenv
from src.bot import PokemonSelfBot


def main():
    load_dotenv()
    bot = PokemonSelfBot(guilds_ids=[0000, 0000, 0000], enabled=True) 
    ## add some guild ids here
    bot.run_bot(token=getenv("TOKEN"))


if __name__ == "__main__":
    main()


