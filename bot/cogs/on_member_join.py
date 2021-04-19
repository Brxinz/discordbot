import discord
from discord.ext import commands


class on_member_joined(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        embed = discord.Embed(
            title="Welcome !",
            color=discord.Color(0x67aff),
            description=f"{member.mention} Just joined! Welcome to r/ZeroOne , please read the <#799926552670109696>  before sending messages here , but most of all , enjoy staying !"
        )
        embed.set_footer(
            text="Made by zh6shi#8655"
        )
        embed.set_image(
            url=member.avatar_url
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/802276339246694480/811959619836313620/ffas.png%22"
        )

        channel_id = commands.get_channel(799936102337216532)
        await channel_id.send(embed=embed)

def setup(bot):
    bot.add_cog(on_member_joined(bot))