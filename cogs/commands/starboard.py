import discord
from discord.ext import commands

class Starboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.starboard_channel = None
        self.starboard_limit = 1
        self.starboard_lock = False
        self.starboard_messages = []

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or message.channel == self.starboard_channel:
            return

        if self.starboard_lock:
            return

        if message.reactions:
            for reaction in message.reactions:
                if reaction.emoji == '⭐' and reaction.count >= self.starboard_limit:
                    await self.add_to_starboard(message)

    async def add_to_starboard(self, message):
        embed = discord.Embed(title=message.content, color=discord.Color.orange())
        embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
        embed.set_footer(text=f"#{message.channel.name} • {message.id}")
        embed.timestamp = message.created_at

        starboard_message = await self.starboard_channel.send(embed=embed)
        self.starboard_messages.append(starboard_message.id)

    @commands.command()
    async def starboard(self, ctx, action=None, value=None):
        if action is None:
            await ctx.send(f"Starboard information:\n"
                           f"Current limit: {self.starboard_limit}\n"
                           f"Current lock: {'Locked' if self.starboard_lock else 'Unlocked'}\n"
                           f"Current channel: {self.starboard_channel.mention if self.starboard_channel else 'None'}\n"
                           f"Current stats: {len(self.starboard_messages)} messages on the Starboard")
            return

        if action.lower() == 'limit':
            self.starboard_limit = int(value)
            await ctx.send(f"Starboard limit set to {self.starboard_limit}")
        elif action.lower() == 'lock':
            self.starboard_lock = True
            await ctx.send("Starboard locked")
        elif action.lower() == 'unlock':
            self.starboard_lock = False
            await ctx.send("Starboard unlocked")
        elif action.lower() == 'setup':
            self.starboard_channel = ctx.channel
            await ctx.send(f"Starboard channel set to {ctx.channel.mention}")
        elif action.lower() == 'stats':
            await ctx.send(f"Current stats: {len(self.starboard_messages)} messages on the Starboard")
        else:
            await ctx.send("Invalid action")
