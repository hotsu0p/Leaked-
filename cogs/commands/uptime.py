import discord
from discord.ext import commands
import datetime

class Uptime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.datetime.utcnow()

    @commands.command(aliases=["up", "u"])
    async def uptime(self, ctx):    
        now = datetime.datetime.utcnow()
        uptime = now - self.start_time
        hours, remainder = divmod(int(uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        uptime_str = "```{:d}d {:02d}h {:02d}m {:02d}s```".format(days, hours, minutes, seconds)

        embed = discord.Embed(title="CHAOTIC™ Uptime", description=uptime_str, color=0x2f3136)
        member = ctx.guild.get_member(ctx.author.id)
        if member:
            embed.set_author(name=f"CHAOTIC™ Uptime",icon_url=self.bot.user.display_avatar.url)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar.url)
        else:
            embed.set_footer(text=f"Requested by {ctx.author.name}")
        embed.set_thumbnail(url=self.bot.user.avatar.url)          
                      

        await ctx.send(embed=embed)