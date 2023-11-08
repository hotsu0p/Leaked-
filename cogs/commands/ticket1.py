import discord
from discord.ext import commands


class hacker1111111111111111111(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  """Ticket commands"""

  def help_custom(self):
    emoji = '<:nexus_Ticket:1158721875925549097>'
    label = "Ticket"
    description = "Show You Ticket Commands"
    return emoji, label, description

  @commands.group()
  async def __Ticket__(self, ctx: commands.Context):
    """`sendpanel`"""
