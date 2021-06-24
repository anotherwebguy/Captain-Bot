import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print("The bot is ready")

client.run('ODU3NDIwMjg1NTY5NTMxOTA0.YNPU3g.FVsVxSuDFptXSMy3vP49oBPzlKo')