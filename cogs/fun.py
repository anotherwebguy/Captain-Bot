import discord
from discord.ext import commands
import random

class Functions(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("The bot is ready")

    @commands.Cog.listener()
    async def on_member_join(self, ctx, member):
        print(f"{member} has joined the server.")
        await ctx.send(f"Welcome {member.mention} to our server")

    @commands.Cog.listener()
    async def on_member_remove(self, ctx, member):
        print(f"{member} has left the server.")
        await ctx.send(f"{member.mention} has left our server")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing Command argument")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("Invalid command")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command(aliases = ['8ball','Test'])
    async def _8ball(self, ctx, *, question):
        """Try your luck!!"""
        responses = ['It is certain.',
                     'Without a doubt',
                     'Yes. definitely',
                     'Most likely',
                     'Signs points to yes.',
                     'Reply hazy, try again',
                     'Ask again later',
                     'Better not tell you now',
                     'Cannot Predict now',
                     'Concentrate and ask again',
                     "Don't count on it",
                     "My reply is no.",
                     'Outlook is not so good',
                     'Very doubtfull',
                     'My sources say no.']
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

    @commands.command()
    async def clear(self, ctx, amount=5):
        """clear chats"""
        await ctx.channel.purge(limit=amount)

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """kick users"""
        await member.kick(reason=reason)
        await ctx.sendO(f"Kicked {member.mention} from the server.")

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """ban users"""
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention} from the server.")

    @commands.command()
    async def unban(self, ctx, *, member):
        """unban users"""
        banned_users = await ctx.guild.bans()
        print(banned_users)
        member_name, member_descriminator = member.split('#')
        print(member_name)
        print(member_descriminator)
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_descriminator):
                print("true")
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.name}#{user.discriminator}")
                return


def setup(client):
    client.add_cog(Functions(client))