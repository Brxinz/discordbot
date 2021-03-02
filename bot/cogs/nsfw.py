import discord
from discord.ext import commands

class nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="nsfw")
    @commands.has_role("helpers")
    async def nsfw(self, ctx, member: discord.Member):
        role = ctx.guild.get_role(805673340168568855)
        await ctx.message.add_reaction('🍆')
        await member.add_roles(role)


def setup(bot):
    bot.add_cog(nsfw(bot))