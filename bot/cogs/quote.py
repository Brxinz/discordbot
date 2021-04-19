import discord
import random
from discord.ext import commands

class quote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def quote(self, ctx):
        lang = ['"Damned human wannabes."—001 about VIRM',
                '"Perharps some lives only shine when in unison with others."—001 about Hiro and Zero Two',
                '"Decide whether you want to fight or accept your ruin."—001 entrusts the Earths future to Hiro and Zero Two'
                ]
        await ctx.send(random.choice(lang))

def setup(bot):
    bot.add_cog(quote(bot))