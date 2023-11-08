import discord
from discord.ext import commands


class hacker1111111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Games commands"""

    def help_custom(self):
          emoji = '<a:Games:1169154665703817247>'
          label = "Games"
          description = ""
          return emoji, label, description

    @commands.group()
    async def __Games__(self, ctx: commands.Context):
        """ `chess` , `hangman` , `typerace` , `rps` , `reaction` , `tick-tack-toe` , `wordle` , `2048` , `memory-game` , `number-slider` , `battleship` , `country-guesser`"""