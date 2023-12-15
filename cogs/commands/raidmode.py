from discord.ext import commands
from utils.Tools import *
import discord
from core import Cog,Astroz, Context


class Automod(Cog):
    """Enable/Disable Anti-raid in your server to be protected from unknown raids!"""

    def __init__(self, client: Astroz):
        self.client = client

    @commands.hybrid_command(
        name="automod",
        aliases=["Automoderation"],
        help="Shows help about Automoderation feature of bot.")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 7, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    async def _antiraid(self, ctx: commands.Context):
        data = getConfig(ctx.guild.id)
        spam = data["antiSpam"]
        link = data["antiLink"]
        embed = discord.Embed(title="Chatoic | Automod Commands",
                              color=0x00FFCA)
        embed.add_field(
            name="<a:sword:1158410994968699002> antispam on/off",
            value=f"Enables/Disables antispam feature\nCurrently Its {spam}",
            inline=False)
        embed.add_field(
            name="<a:sword:1158410994968699002> antilink on/off",
            value=f"Enables/Disables antilink feature\nCurrently Its {link}",
            inline=False)
        await ctx.reply(embed=embed, mention_author=False)

    @commands.hybrid_command(name="antispam",
                             aliases=['anti-spam'],
                             help="Enables or Disables anti spam feature")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    async def _antispam(self, ctx: commands.Context, type: str):

        onOroff = type.lower()

        data = getConfig(ctx.guild.id)
        if ctx.author == ctx.guild.owner or ctx.guild.me.top_role <= ctx.author.top_role:
            if onOroff == "on":
                if data["antiSpam"] is True:
                    hacker = discord.Embed(
                        description=
                        f"<a:no:1158411070608769034> | Anti-Spam is already enabled for **`{ctx.guild.name}`**",
                        color=0x00FFCA)
                    await ctx.reply(embed=hacker, mention_author=False)
                else:
                    data["antiSpam"] = True
                    updateConfig(ctx.guild.id, data)
                    hacker1 = discord.Embed(
        
                        description=
                        f"<a:cx_tick:1158669360223748106> | Successfully enabled anti-spam for **`{ctx.guild.name}`**",
                        color=0x00FFCA)
                    await ctx.reply(embed=hacker1, mention_author=False)

            elif onOroff == "off":
                data = getConfig(ctx.guild.id)
                data["antiSpam"] = False
                updateConfig(ctx.guild.id, data)
                hacker2 = discord.Embed(
                    description=
                    f"<a:cx_tick:1158669360223748106> | Successfully disabled anti-spam for **`{ctx.guild.name}`**",
                    color=0x00FFCA)
                await ctx.reply(embed=hacker2, mention_author=False)
            else:
                hacker3 = discord.Embed(
                    description=
                    f"<a:no:1158411070608769034> | Invalid Type.\nIt Should Be On/Off",
                    color=0x00FFCA)
                await ctx.reply(embed=hacker3, mention_author=False)

        else:
            hacker5 = discord.Embed(
                color=0x00FFCA,
                title="Chatoic Security",
                description=
                f"<a:no:1158411070608769034> | Only owner of the server can run this command"
            )
            await ctx.reply(embed=hacker5, mention_author=False)

    @commands.hybrid_command(aliases=['anti-link'],
                             name="antilink",
                             help="Enables or Disables antilink feature")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    async def _antilink(self, ctx: commands.Context, type: str):

        onOroff = type.lower()

        data = getConfig(ctx.guild.id)
        if ctx.author == ctx.guild.owner or ctx.guild.me.top_role <= ctx.author.top_role:
            if onOroff == "on":
                if data["antiLink"] is True:
                    hacker = discord.Embed(
                        description=
                        f"<a:no:1158411070608769034> | Anti-link is already enabled for **`{ctx.guild.name}`**",
                        color=0x00FFCA)
                    await ctx.reply(embed=hacker, mention_author=False)
                else:
                    data["antiLink"] = True
                    updateConfig(ctx.guild.id, data)
                    hacker1 = discord.Embed(
                        description=
                        f"<a:cx_tick:1158669360223748106> | Successfully enabled anti-link for **`{ctx.guild.name}`**",
                        color=0x00FFCA)
                    await ctx.reply(embed=hacker1, mention_author=False)

            elif onOroff == "off":
                data = getConfig(ctx.guild.id)
                data["antiLink"] = False
                updateConfig(ctx.guild.id, data)
                hacker2 = discord.Embed(
                    description=
                    f"<a:cx_tick:1158669360223748106> | Successfully disabled anti-link for **`{ctx.guild.name}`**",
                    color=0x00FFCA)
                await ctx.reply(embed=hacker2, mention_author=False)
            else:
                hacker3 = discord.Embed(
            
                    description=
                    f"<a:no:1158411070608769034> | Invalid Type.\nIt Should Be On/Off",
                    color=0x00FFCA)
                await ctx.reply(embed=hacker3, mention_author=False)

        else:
            hacker5 = discord.Embed(
                color=0x00FFCA,
                description=
                f"<a:no:1158411070608769034> | Only owner of the server can run this command"
            )
            await ctx.reply(embed=hacker5, mention_author=False)