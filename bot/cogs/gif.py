import discord
from discord.ext import commands
import giphy_client
from giphy_client.rest import ApiException
import random

class gif(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gif(self, ctx, *, q="DARLING in the FRANXX"):

        api_key = "cN6owNxZdjX3GNPULhh4UpCGl5jwyjQp"
        api_instance = giphy_client.DefaultApi()

        try:

            api_response = api_instance.gifs_search_get(api_key, q, limit=100, rating='r')
            lst = list(api_response.data)
            giff = random.choice(lst)

            emb = discord.Embed(title=q, colour=discord.Colour(0x67aff))
            emb.set_image(url=f'https://media.giphy.com/media/{giff.id}/giphy.gif')

            await ctx.channel.send(embed=emb)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

def setup(bot):
    bot.add_cog(gif(bot))