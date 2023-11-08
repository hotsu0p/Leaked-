import discord
from discord.ext import commands


class gw1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Giveaway Commands"""
  
    def help_custom(self):
		      emoji = '<a:tadaaa:1162353626593894460>'
		      label = "Giveaway"
		      description = "Show You Commands Of Giveaway"
		      return emoji, label, description

    @commands.group()
    async def __Giveaway__(self, ctx: commands.Context):
        """`gstart` , `gend` , `greroll`"""