import discord
from discord.ext import commands
import os
from pymongo import MongoClient


class Client(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.cluster = MongoClient(os.getenv("MONGO_URI")).bot

        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                name = file[:-3]
                self.load_extension(f"cogs.{name}")

    def get_cluster(self):
        return self.cluster


bot = Client(debug_guilds=[997239798429388941])

bot.run(os.getenv('DISC_TOKEN'))
