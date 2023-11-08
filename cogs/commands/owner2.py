import discord
from discord.ext import commands


class owner2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Owner commands"""
  
    def help_custom(self):
		      emoji = '<a:cx_crown:1158669179059183687>'
		      label = "Owner"
		      description = "Show You Commands Of Owner"
		      return emoji, label, description

    @commands.group()
    async def __Owner__(self, ctx: commands.Context):
        """`eval` , `shutdown` , `slist` , `restart` , `sync` , `np` , `np add` , `np remove` , `np list` , `bl show` , `bl add` , `bl remove` , `bdg` , `bdg add` , `bdg remove` , `dm` , `nick` , `globalban`"""