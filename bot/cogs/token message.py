import discord
import asyncio
from discord.ext import commands


class AdminCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ticket(self, ctx):
        title = "ticket"
        description = "If you have a question or concern, please create a ticket by clicking on the 📩 emoji."

        embed = discord.Embed(
            title=title,
            description=description,
            color=0x2f2fd0
        )
        embed.set_author(
            name="Zeroone",
            icon_url = "https://cdn.discordapp.com/avatars/811934668433260614/30da9b63c3e4fdc4d59c5b60dff7c539.png?size=128"
        )

        msg = await ctx.send(embed=embed)
        await msg.add_reaction("📩")
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(AdminCommands(bot))