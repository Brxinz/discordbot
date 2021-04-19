import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import config
import os


prefix = config.prefix


bot = commands.Bot(command_prefix= prefix, intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("aye foo its working")
    print("------------------------")
    await bot.change_presence(activity=discord.Game (name=config.playing))

    print("----------------------------------------")
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded {filename}')
            except Exception as e:
                print(f'Failed to load {filename}')
                print(f'[ERROR] {e}')
    print("----------------------------------------")

bot.token = config.Token
bot.run(bot.token, bot=True, reconnect=True)