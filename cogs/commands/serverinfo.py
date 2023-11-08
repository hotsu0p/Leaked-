from discord.ext import commands
import discord
import os
from discord.ext.commands import Cog, Context
import humanize
from utils.Tools import *

class util:
  def checkrol(role):
    perms = ""
    for p in role.permissions:
      xd = p[0]
      checkofperm = p[1]
      wp = xd.replace("_", " ")
      if checkofperm:
        perms+=f"{xd.replace('_', ' ')}, "
    if perms == "":
      perms+="None"
    else:
      perms.replace("_", " ")
      perms.strip(", ")
    return perms

class Info(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.client = bot
    self.color = discord.Color (0x0d0d13)
  @commands.hybrid_command(name="roleinfo",
                             help="Shows you all information about a role.",
                             usage="Roleinfo <role>",with_app_command = True)
  @blacklist_check()
  @ignore_check()
  async def yomom(self, ctx: Context, *, role: discord.Role):
    p = util.checkrol(role)
    embed = discord.Embed(color=role.color)
    embed.set_author(name=f"{role.name}'s Information", icon_url=ctx.bot.user.avatar)
    embed.add_field(name="__General Info__",
                    value=f"""Role Name : {role.name}\nRole ID : {role.id}\nRole Position : {role.position}\nHex code : {role.color}\nCreated At : {discord.utils.format_dt(role.created_at)}\nMentionability : {role.mentionable}\nSeparated : {role.hoist}\nIntegration : {role.managed}""",
            inline=False
        )
    embed.add_field(name="Allowed Permissions", 
                    value=p.rsplit(",", 1)[0]),
    embed.set_footer(text=f"Requested by {ctx.author}",
    icon_url=ctx.author.avatar)
    await ctx.send(embed=embed)

   
  @commands.command(name="serverinfo",aliases=["sinfo","si"], description="Show's information of the server")
  @blacklist_check()
  @ignore_check()
  async def serverinfo(self, ctx: commands.Context):
        bammed = 0
        async for bans in ctx.guild.bans(limit=None):
          bammed += 1
        animated_emojis = len([emoji for emoji in ctx.guild.emojis if emoji.animated])
        static = len([emoji for emoji in ctx.guild.emojis if not emoji.animated])
        om = ctx.guild.afk_timeout /60
        default = None
        if ctx.guild.default_notifications == discord.NotificationLevel.all_messages:
          default = "All Messages"
        elif ctx.guild.default_notifications == discord.NotificationLevel.only_mentions:
          default = "Only @mentions"
        al = ctx.guild.emoji_limit
        al1 = ctx.guild.sticker_limit
        uf = ctx.guild.emoji_limit * 2
        nsfw_level = ''
        if ctx.guild.nsfw_level.name == 'default':
          nsfw_level = 'Default'
        if ctx.guild.nsfw_level.name == 'explicit':
          nsfw_level = 'Explicit'
        if ctx.guild.nsfw_level.name == 'safe':
          nsfw_level = 'Safe'
        if ctx.guild.nsfw_level.name == 'age_restricted':
          nsfw_level = 'Age Restricted'
        guild: discord.Guild = ctx.guild 
        for r in ctx.guild.roles:
            if len(ctx.guild.roles) < 1:
                roless = "None"
            else:
                if len(ctx.guild.roles) < 30:
                    roless = ", ".join(
                        [role.mention for role in ctx.guild.roles[1:][::-1]])
                else:
                    if len(ctx.guild.roles) > 30:
                        roless = "Too many roles to show here." 
        embed = discord.Embed(color=0x00FFCA,
            title=f" **{guild.name}'s Information**",
          description=f"**__About__**\n**Name:** {ctx.guild.name}\n**ID:** {ctx.guild.id}\n**Owner <a:cx_crown:1158669179059183687>:** {ctx.guild.owner} ({guild.owner.mention})\n**Created At:** <t:{round(guild.created_at.timestamp())}:R>\n**Members:** {len(guild.members)}\n**Banned:** {bammed}")
             
        embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar)
        if guild.icon is not None:
            embed.set_thumbnail(url=guild.icon.url)
        if guild.system_channel_flags.join_notifications:
          haa = "**System Welcome Messages**: <a:cx_tick:1158669360223748106>"
        else:
          haa = "**System Welcome Messages**: <a:no:1158411070608769034>"
        afkk = ctx.guild.afk_channel
        if ctx.guild.system_channel_flags.premium_subscriptions:
          skib = "**System Boost Messages**: <a:cx_tick:1158669360223748106>"
        else:
          skib = "**System Boost Messages**: <a:no:1158411070608769034>"  
        if guild.system_channel:
              ha = f"**System Messages Channel**: {guild.system_channel.mention}"
        else:
              ha = "**System Messages Channel**: None"
        mfa = ""
        if ctx.guild.mfa_level == discord.MFALevel.disabled:
          mfa = "Enabled <a:cx_tick:1158669360223748106>"
        else:
          mfa = "Disabled <a:no:1158411070608769034>"
        embed.add_field(
            name="**__Extras__**",
            value=f"""
**Verification Level:** {str(guild.verification_level).title()}
**Upload Limit:** {humanize.naturalsize(guild.filesize_limit)}
**Inactive Channel**: {afkk}
**Inactive Timeout:** {om} Mins
{ha}
{haa} 
{skib} 
**Default Notifications:** {default}
**Explicit Media Content Filter:** {guild.explicit_content_filter.name} 
**2FA Requirement:** {mfa}
**Boost Bar Enabled:** {'<a:no:1158411070608769034>' if not ctx.guild.premium_progress_bar_enabled else '<a:cx_tick:1158669360223748106>'}
            """,
            inline=False
        )
        embed.add_field(
            name="**__Description__**",
            value=f"""
{guild.description}
            """,
            inline=False
        )       
        if guild.features:
            dk = []
            for feat in guild.features:
              dk.append(feat.replace('_', ' ').title())
            embed.add_field(
                name="**__Features__**",
                value='\n'.join([f"<a:cx_tick:1158669360223748106> : {feature}" for feature in dk]),
                inline=False
            )
            if guild.rules_channel:
              bye = f"Rules Channel: {guild.rules_channel.mention}"
            else:
              bye = ""
            embed.add_field(
            name="**__Channels__**",
            value=f"""
Total: {len(guild.channels)}
Channels: <a:Hashtag:1162715140215558254> {len(guild.text_channels)} | <a:voicegoogle:1158411017324335135> {len(guild.voice_channels)} | <:stage:1162715428297113720> {len(guild.stage_channels)} 
{bye}
            """,
            inline=False
        )
        embed.add_field(
            name="**__Emoji Info__**",
            value=f"""
Regular: {static}/{al}
Animated: {animated_emojis}/{al}
Stickers: {len(guild.stickers)}/{al1}
Total Emoji: {len(guild.emojis)}/{uf}
            """, 
            inline=False
        )
        if guild.premium_subscriber_role:
          byecom = f"Booster Role: {guild.premium_subscriber_role.mention}"
        else:
          byecom = ""
        embed.add_field(
            name="**__Boost Status__**",
            value=f"""
Level: {guild.premium_tier} <a:diamond:1160512500719169608> {guild.premium_subscription_count} boosts] 
{byecom}
            """,
            inline=False
        )
        embed.add_field(name=f"**__Server Roles [ {len(guild.roles)} ]__**",
                        value=f"{roless}",
                        inline=False)
        if guild.banner is not None:
            embed.set_image(url=guild.banner.url)
        embed.timestamp = discord.utils.utcnow()
        return await ctx.send(embed=embed)