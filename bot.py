import os
import discord
from decouple import config
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="?", intents=intents)

def load_cogs(bot):
    bot.load_extension("manager")
    bot.load_extension("tasks.current_time")

    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")

load_cogs(bot)

TOKEN = config("BOT_TOKEN")
bot.run(TOKEN)
