import discord
from discord.ext import commands

class Userinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True, aliases=['user', 'uinfo', 'info', 'ui'])
    async def userinfo(self, ctx, *, name=""):
        if ctx.invoked_subcommand is None:
            if name:
                try:
                    user = ctx.message.mentions[0]
                    print(user)
                except IndexError:
                    user = ctx.guild.get_member_named(name)
                if not user:
                    user = ctx.guild.get_member(int(name))
                if not user:
                    user = self.client.get_user(int(name))
                if not user:
                    await ctx.send(self.client.bot_prefix + 'Could not find user.')
                    return
            else:
                user = ctx.message.author

            # if user.avatar_url_as(static_format='png')[54:].startswith('a_'):
            #     avi = user.avatar_url.rsplit("?", 1)[0]
            # else:
            #     avi = user.avatar_url_as(static_format='png')
            if isinstance(user, discord.Member):
                role = user.top_role.name
                if role == "@everyone":
                    role = "N/A"
            #     voice_state = None if not user.voice else user.voice.channel
            if embed_perms(ctx.message):
                em = discord.Embed(timestamp=ctx.message.created_at, colour=0x708DD0)
                em.add_field(name='User ID', value=user.id, inline=True)
                if isinstance(user, discord.Member):
                    em.add_field(name='Nick', value=user.nick, inline=True)
                    em.add_field(name='Status', value=user.status, inline=True)
                    em.add_field(name='Highest Role', value=role, inline=True)
                em.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
                if isinstance(user, discord.Member):
                    em.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
                em.set_author(name=user, icon_url='https://i.imgur.com/RHagTDg.png')
                await ctx.send(embed=em)
                print(em)
            else:
                if isinstance(user, discord.Member):
                    msg = '**User Info:** ```User ID: %s\nNick: %s\nStatus: %s\nGame: %s\nAccount Created: %s\nJoin Date: %s```' % (
                    user.id, user.nick, user.status, user.activity,
                    user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'),
                    user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
                else:
                    msg = '**User Info:** ```User ID: %s\nAccount Created: %s%s```' % (
                    user.id, user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
                await ctx.send(self.client.bot_prefix + msg)

            await ctx.message.delete()


def embed_perms(message):
    try:
        check = message.author.permissions_in(message.channel).embed_links
    except:
        check = True

    return check


def setup(client):
    client.add_cog(Userinfo(client))