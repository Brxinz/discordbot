import discord
from discord.ext import commands

class wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wiki(self, ctx):
        await ctx.send("https://darling-in-the-franxx.fandom.com/wiki/001")

    def setup(bot):
        bot.add_cog(wiki(bot))
