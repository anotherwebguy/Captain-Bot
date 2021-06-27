import discord
from discord.ext import commands

class About(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def about(self, ctx, txt: str = None):
        """Links to the bot's github page."""
        if embed_perms(ctx.message) and txt != 'short':
            em = discord.Embed(color=0xad2929, title='\ud83e\udd16 anotherwebguy\'s Captain-Bot',
                               description='**Features:**\n- Custom commands/reactions\n- kick/ban/unban\n- Random jokes\n'
                                           '- Get news\n- Create a poll\n- Get user info\n- 8ball\n'
                                           '- Simple calculator\n- and much more')
            em.add_field(name='\ud83d\udd17 Link to download',
                         value='[Github link](https://github.com/anotherwebguy/Captain-Bot.git)')
            if txt == 'link': em.add_field(name='👋 Discord Server',
                                           value='Join the official Discord server [here](https://discord.gg/Ma4h8nFW82)!')
            em.set_footer(text='Made by Mohit Singh', icon_url='https://drive.google.com/file/d/19II56EPJKpN8Mavz6OzLqSc6wWeGAP7x/view?usp=drivesdk')
            await ctx.send(content=None, embed=em)
        else:
            await ctx.send('https://github.com/anotherwebguy/Captain-Bot.git')
        await ctx.message.delete()


def embed_perms(message):
    try:
        check = message.author.permissions_in(message.channel).embed_links
    except:
        check = True

    return check

def setup(client):
    client.add_cog(About(client))