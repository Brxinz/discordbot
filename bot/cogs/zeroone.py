import discord
from discord.ext import commands

class zeroone(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def zeroone(self, ctx):
        await ctx.send("01, also known as the Princess of Klaxosaurs, is a character in DARLING in the FRANXX. She is a Klaxo-sapien and is presumed to be the last surviving member of her kind.")


def setup(bot):
    bot.add_cog(zeroone(bot))