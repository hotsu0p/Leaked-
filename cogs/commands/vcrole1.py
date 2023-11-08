import discord
from discord.ext import commands


class vcrole1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """VcRoles Commands"""
  
    def help_custom(self):
		      emoji = '<:merox_vcroles:1158734018813108265>'
		      label = "VcRoles"
		      description = "Show You Commands Of VcRoles"
		      return emoji, label, description

    @commands.group()
    async def __VcRoles__(self, ctx: commands.Context):
        """`vcrole bots add` , `vcrole bots remove` , `vcrole bots` , `vcrole config` , `vcrole humans add` , `vcrole humans remove` , `vcrole humans` , `vcrole reset` , `vcrole`"""