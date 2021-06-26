import discord
from discord.ext import commands
import random,os
from decouple import config

TOKEN = config('DISCORD_TOKEN')

client = commands.Bot(command_prefix='!')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# @client.event
# async def on_ready():
#     print("The bot is ready")
#
# @client.event
# async def on_member_join(ctx, member):
#     print(f"{member} has joined the server.")
#     await ctx.send(f"Welcome {member.mention} to our server")
#
# @client.event
# async def on_member_remove(ctx, member):
#     print(f"{member} has left the server.")
#     await ctx.send(f"{member.mention} has left our server")
#
# @client.command()
# async def ping(ctx):
#     await ctx.send("Pong!")
#
# @client.command(aliases = ['8ball','Test'])
# async def _8ball(ctx, *, question):
#     responses = ['It is certain.',
#                  'Without a doubt',
#                  'Yes. definitely',
#                  'Most likely',
#                  'Signs points to yes.',
#                  'Reply hazy, try again',
#                  'Ask again later',
#                  'Better not tell you now',
#                  'Cannot Predict now',
#                  'Concentrate and ask again',
#                  "Don't count on it",
#                  "My reply is no.",
#                  'Outlook is not so good',
#                  'Very doubtfull',
#                  'My sources say no.']
#     await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")
#
# @client.command()
# async def clear(ctx, amount=5):
#     await ctx.channel.purge(limit=amount)
#
# @client.command()
# async def kick(ctx, member : discord.Member, *, reason=None):
#     await member.kick(reason = reason)
#     await ctx.sendO(f"Kicked {member.mention} from the server.")
#
# @client.command()
# async def ban(ctx, member : discord.Member, *, reason=None):
#     await member.ban(reason = reason)
#     await ctx.send(f"Banned {member.mention} from the server.")
#
# @client.command()
# async def unban(ctx, *, member):
#     banned_users = await ctx.guild.bans()
#     member_name, member_descriminator = member.split('#')
#     for ban_entry in banned_users:
#         user = ban_entry.user
#
#         if( user.name, user.descriminator) == (member_name, member_descriminator):
#             await ctx.guild.unban(user)
#             await ctx.send(f"Unbanned {user.name}#{user.descriminator}")
#             return

client.run(TOKEN)