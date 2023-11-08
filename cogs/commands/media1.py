import discord
from discord.ext import commands


class media1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Media Commands"""
  
    def help_custom(self):
		      emoji = '<a:AG_SocialMedia:1158411040766308482>'
		      label = "Media"
		      description = "Show You Commands Of Media"
		      return emoji, label, description

    @commands.group()
    async def __Media__(self, ctx: commands.Context):
        """`media`, `media setup`, `media remove`, `media config`, `media reset`"""