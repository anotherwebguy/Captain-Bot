import discord
from discord.ext import commands
import os
from decouple import config

TOKEN = config('DISCORD_TOKEN')

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print("The bot is ready")

client.run(TOKEN)