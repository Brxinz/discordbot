import discord
from discord.ext import commands

class MemberInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx, member: discord.Member):
        embed = discord.Embed(
            title=[f"Roles Member Has = {member.roles}",
                   f"Member id = {member.id}",
                   f"Nickname = {member.nick}",
                   f"Account age in server = {member.joined_at}",
                   f"Account created in {member.created_at}"],
            description=f"{member.avatar_url}"
        )
        embed.set_image(
            url = member.avatar_url
        )
        embed.set_author(
            name= f"{member.display_name}#{member.discriminator}"
        )
        embed.set_footer(
            text=f"Requested by {ctx.author.name}"
        )
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(MemberInfo(bot))
