import re

import discord

from src.utils import *

class Pokeutilities:

    def __init__(self, user_id: int=0, preferred_catch_type: str="base"):
        self.deriver_id = 704130818339242094
        self.user_id = user_id
        self.preferred_catch_type = preferred_catch_type


        if self.prefered_catch_type not in ('base', 'cjk'):
            self.prefered_catch_type = "base"
        

    def is_valid_spawn(self, message: discord.Message) -> bool:
        if message.author.id == self.deriver_id:
            if message.embeds:
                title = str(message.embeds[0].title)
                if title.startswith("A wild pok") and title.endswith('appeared!'):
                    return True
        return False

    async def process_caught(self, message: discord.Message) -> None:

        caught_regex = re.compile(rf'Congratulations <@{self.user_id}>! You caught a level (\d+) (\w+)! \((\d+\.\d+)\%\)')
        caught_shiny_regex = re.compile(rf'Congratulations <@{self.user_id}>! You caught a level (\d+) Shiny (\w+)! \((\d+\.\d+)\%\)')

        if message.author.id == self.deriver_id:

            if caught_regex.search(message.content):
                pokemon_name = caught_regex.search(message.content).group(2)
                pokemon_level = caught_regex.search(message.content).group(1)
                print(f'caught! name: {pokemon_name} level: {pokemon_level} in {message.channel.name} | {message.guild.name}')

            if caught_shiny_regex.search(message.content):
                pokemon_name = caught_regex.search(message.content).group(2)
                pokemon_level = caught_regex.search(message.content).group(1)
                print(f'shiny caught! name: {pokemon_name} level: {pokemon_level} in {message.channel.name} | {message.guild.name}')
                

    async def catch_pokemon(self, message: discord.Message):
        image = message.embeds[0].image.url
        pokemon = recognize_pokemon(image, self.preferred_catch_type)
        await message.channel.send(f"<@{self.deriver_id}> catch {pokemon.lower()}")
