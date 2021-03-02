import discord
from discord.ext import commands
import random

class on_member_remove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(member: discord.Member):
        leave = [f'The queen will be very disappointed once she hears of your absence {member.mention}',
                 f'No one ever liked you anyways {member.mention}']
        channel_id = commands.get_channel(799936102337216532)
        await channel_id.send(random.choice(leave))


def setup(bot):
    bot.add_cog(on_member_remove(bot))