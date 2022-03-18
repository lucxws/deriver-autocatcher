import os

from discord.ext import commands
import discord

from src.utils import is_valid_token
from src.pokemon import Pokeutilities



class PokemonSelfBot(commands.Bot):

    def __init__(self, prefix: str=">", guilds_ids: list=None, enabled: bool=True):
        """
        Initialize the bot
        Default prefix is '>'
        """
        self.prefix = prefix    
        self.guilds_ids = guilds_ids
        self.enabled = enabled
        self.utilspoke = None
        super().__init__(command_prefix=self.prefix, self_bot=True)

        
    def run_bot(self, token: str=None):

        os.system(f"cls" if os.name == "nt" else "clear")

        if token is None:   
            raise Exception("Please provide a token")
        elif not is_valid_token(token):
            raise Exception("Invalid token")
        else:
            self.run(token, bot=False)

    

    
    async def on_message(self, message: discord.Message):

        if self.enabled:
            if self.guilds_ids is not None:
                if message.guild.id in self.guilds_ids:
                    await self.utilspoke.process_caught(message)
                    if self.utilspoke.is_valid_spawn(message):
                        ## await ctx.channel.typing()
                        await self.utilspoke.catch_pokemon(message)
        
        

        
        
    async def on_connect(self):
        banner = f"""
        ██████╗  ██████╗ ██╗  ██╗███████╗███╗   ███╗ ██████╗ ███╗   ██╗                             
        ██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝████╗ ████║██╔═══██╗████╗  ██║                             
        ██████╔╝██║   ██║█████╔╝ █████╗  ██╔████╔██║██║   ██║██╔██╗ ██║                             
        ██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║                             
        ██║     ╚██████╔╝██║  ██╗███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║                             
        ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝                             
                                                                                                    
        █████╗ ██╗   ██╗████████╗ ██████╗  ██████╗ █████╗ ████████╗ ██████╗██╗  ██╗███████╗██████╗ 
        ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔══██╗
        ███████║██║   ██║   ██║   ██║   ██║██║     ███████║   ██║   ██║     ███████║█████╗  ██████╔╝
        ██╔══██║██║   ██║   ██║   ██║   ██║██║     ██╔══██║   ██║   ██║     ██╔══██║██╔══╝  ██╔══██╗
        ██║  ██║╚██████╔╝   ██║   ╚██████╔╝╚██████╗██║  ██║   ██║   ╚██████╗██║  ██║███████╗██║  ██║
        ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
        {'-' * 94}
        >>> Connected to discord as {self.user} | {self.user.id} | [{self.prefix}]
        {'-' * 94}
        """
        print(banner)
        self.utilspoke = Pokeutilities(user_id=self.user.id, prefered_catch_type='cjk')


