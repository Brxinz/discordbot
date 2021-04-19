import discord
from discord.ext import commands

class Apearance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Appearance(self, ctx):
        await ctx.send("001 is a blue skinned humanoid klaxosaur with long flowing sky blue-white hair and prominent blue eyes with glowing blue pupils. She has dark lines under her eyes and all around her body. She also has eight spider-like appendages coming from her back and what seems to be a crown on her head, with two blue horns protruding from the center: one from her forehead and another from the back of the head.")

def setup(bot):
    bot.add_cog(Apearance(bot))