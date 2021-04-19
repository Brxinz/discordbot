import discord
import random
import asyncio
import datetime

from discord.ext import commands
from discord.utils import get
from time import strftime
from datetime import datetime


class Reaction(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    channel_ticket = None
    ticket_creator = None

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild_id = payload.guild_id
        guild = self.bot.get_guild(guild_id)
        user_id = payload.user_id
        user = self.bot.get_user(user_id)
        message_id = payload.message_id
        channel = self.bot.get_channel(payload.channel_id)

        # TICKETS
        emoji = payload.emoji.name

        if message_id == 833599138171060245 and emoji == "📩":
            self.ticket_creator = user_id

            message = await channel.fetch_message(message_id)
            await message.remove_reaction("📩", user)
            guild = self.bot.get_guild(833599002800685086)
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            support_role = guild.get_role(833600730136838155)
            category =  guild.get_channel(833600840560410654)
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                member: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                support_role: discord.PermissionOverwrite(read_messages=True, send_messages=True)
            }
            ticket_nr = random.randint(100, 999)
            self.channel_ticket = await category.create_text_channel(f'ticket-{ticket_nr}', overwrites=overwrites)

            embed = discord.Embed(
                title="How can we help you?",
                description="A supporter will take care of you as soon as possible.\n\n:white_check_mark: - Claim the ticket\n:lock: - Close the ticket",
                color=0x0000ff)
            embed.set_author(
                name="zeroone",
                icon_url = "https://cdn.discordapp.com/avatars/811934668433260614/30da9b63c3e4fdc4d59c5b60dff7c539.png?size=128"
            )

            msg = await self.channel_ticket.send(embed=embed)

            await msg.add_reaction("✅")
            await msg.add_reaction("🔒")

        if channel == self.channel_ticket and emoji == "🔒" and user_id != 826703001431441458:
            message = await channel.fetch_message(message_id)
            await message.remove_reaction("🔒", user)

            now = datetime.now()
            time = now.strftime(str("%d.%m.%Y") + " at " + str("%H:%M"))

            channel_log = self.bot.get_channel(833601243392901141)
            text = f"The ticket ``{self.channel_ticket}`` was closed by {user.mention} on {time}"

            embed = discord.Embed(
                title="Closed Ticket",
                description=text,
                color=0x0000ff)

            await channel_log.send(embed=embed)

            embed = discord.Embed(
                title="Ticket closed!",
                description=f":tickets: The ticket was just closed by {user.mention}.",
                color=0x0000ff)

            await channel.send(embed=embed)

            await asyncio.sleep(10)

            await channel.delete()

        if channel == self.channel_ticket and emoji == "✅" and user_id != 826703001431441458:

            message = await channel.fetch_message(message_id)
            await message.remove_reaction("✅", user)

            if self.ticket_creator == user_id:

                embed = discord.Embed(
                    title="You cant claim the ticket!",
                    color=0x0000ff)

                await channel.send(embed=embed)

            else:

                embed = discord.Embed(
                    title="Ticket claimed!",
                    description=f"The ticket was claimed by {user.mention}.",
                    color=0x0000ff)
                embed.set_author(name="Zeroone Ticket Bot")

                await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Reaction(bot))