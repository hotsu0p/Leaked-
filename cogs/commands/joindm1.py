import discord
from discord.ext import commands


class joindm1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Join Dm Commands"""
  
    def help_custom(self):
		      emoji = '<a:planetz:1158410965780529202>'
		      label = "Join Dm"
		      description = "Show You Commands Of Join Dm"
		      return emoji, label, description

    @commands.group()
    async def __joindm1__(self, ctx: commands.Context):
        """`joindm enable`, `joindm disable`, `joindm message`"""