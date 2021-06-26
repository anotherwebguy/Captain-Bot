import discord
from discord.ext import commands
import asyncio
import math
from math import sqrt


class Extras(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def poll(self, ctx, *, msg):
        """Create a poll using reactions. [p]help poll for more information.
        [p]poll <question> | <answer> | <answer> - Create a poll. You may use as many answers as you want, placing a pipe | symbol in between them.
        Example:
        [p]poll What is your favorite anime? | Steins;Gate | Naruto | Attack on Titan | Shrek
        You can also use the "time" flag to set the amount of time in seconds the poll will last for.
        Example:
        [p]poll What time is it? | HAMMER TIME! | SHOWTIME! | time=10
        """
        await ctx.message.delete()
        options = msg.split(" | ")
        time = [x for x in options if x.startswith("time=")]
        if time:
            time = time[0]
        if time:
            options.remove(time)
        if len(options) <= 1:
            return await ctx.send(self.bot.bot_prefix + "You must have 2 options or more.")
        if len(options) >= 11:
            return await ctx.send(self.bot.bot_prefix + "You must have 9 options or less.")
        if time:
            time = int(time.strip("time="))
        else:
            time = 30
        emoji = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣']
        to_react = []
        confirmation_msg = "**{}?**:\n\n".format(options[0].rstrip("?"))
        for idx, option in enumerate(options[1:]):
            confirmation_msg += "{} - {}\n".format(emoji[idx], option)
            to_react.append(emoji[idx])
        confirmation_msg += "\n\nYou have {} seconds to vote!".format(time)
        poll_msg = await ctx.send(confirmation_msg)
        for emote in to_react:
            await poll_msg.add_reaction(emote)
        await asyncio.sleep(time)
        async for message in ctx.message.channel.history():
            if message.id == poll_msg.id:
                poll_msg = message
        results = {}
        for reaction in poll_msg.reactions:
            if reaction.emoji in to_react:
                results[reaction.emoji] = reaction.count - 1
        end_msg = "The poll is over. The results:\n\n"
        for result in results:
            end_msg += "{} {} - {} votes\n".format(result, options[emoji.index(result) + 1], results[result])
        top_result = max(results, key=lambda key: results[key])
        if len([x for x in results if results[x] == results[top_result]]) > 1:
            top_results = []
            for key, value in results.items():
                if value == results[top_result]:
                    top_results.append(options[emoji.index(key) + 1])
            end_msg += "\nThe victory is tied between: {}".format(", ".join(top_results))
        else:
            top_result = options[emoji.index(top_result) + 1]
            end_msg += "\n{} is the winner!".format(top_result)
        await ctx.send(end_msg)

    @commands.command(pass_context=True)
    async def calc(self, ctx, *, msg):
        """Simple calculator. Ex: [p]calc 2+2"""
        equation = msg.strip().replace('^', '**').replace('x', '*')
        try:
            if '=' in equation:
                left = eval(equation.split('=')[0], {"__builtins__": None}, {"sqrt": sqrt})
                right = eval(equation.split('=')[1], {"__builtins__": None}, {"sqrt": sqrt})
                answer = str(left == right)
            else:
                answer = str(eval(equation, {"__builtins__": None}, {"sqrt": sqrt}))
        except TypeError:
            return await ctx.send(self.bot.bot_prefix + "Invalid calculation query.")
        if embed_perms(ctx.message):
            em = discord.Embed(color=0xD3D3D3, title='Calculator')
            em.add_field(name='Input:', value=msg.replace('**', '^').replace('x', '*'), inline=False)
            em.add_field(name='Output:', value=answer, inline=False)
            await ctx.send(content=None, embed=em)
            await ctx.message.delete()
        else:
            await ctx.send(self.bot.bot_prefix + answer)


def embed_perms(message):
    try:
        check = message.author.permissions_in(message.channel).embed_links
    except:
        check = True

    return check


def setup(client):
    client.add_cog(Extras(client))
