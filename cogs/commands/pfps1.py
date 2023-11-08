import discord
from discord.ext import commands


class pfps1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Pfp Commands"""
  
    def help_custom(self):
		      emoji = '<a:awful_pfp:1169154160017539083>'
		      label = "Pfp"
		      description = "Show You Commands Of Pfp"
		      return emoji, label, description

    @commands.group()
    async def __Pfp__(self, ctx: commands.Context):
        """`pic`, `boys` , `girls`, `couples`, `anime`"""