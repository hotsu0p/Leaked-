import contextlib
from traceback import format_exception
import discord
from discord.ext import commands
import io
import textwrap
import datetime
import sys
from discord.ui import Button, View
import psutil
import time
import datetime
import platform
from utils.Tools import *
import os
import logging
from discord.ext import commands
import motor.motor_asyncio
from pymongo import MongoClient
from discord.ext.commands import BucketType, cooldown
import requests
import motor.motor_asyncio as mongodb
from typing import *
from utils import *


from core import Cog, Astroz, Context
from typing import Optional
from discord import app_commands
start_time = time.time()


def datetime_to_seconds(thing: datetime.datetime):
    current_time = datetime.datetime.fromtimestamp(time.time())
    return round(
        round(time.time()) +
        (current_time - thing.replace(tzinfo=None)).total_seconds())


cluster = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://RANDI:SHREEXD3110@cluster0.l8dzjae.mongodb.net/?retryWrites=true&w=majority")

notedb = cluster["discord"]["note"]


class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        mem = "ctx.author"
        self.connection = mongodb.AsyncIOMotorClient("mongodb+srv://RANDI:SHREEXD3110@cluster0.l8dzjae.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.connection["LEGEND"]["servers"]

    @commands.group(name="banner")
    async def banner(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)

    @banner.command(name="server")
    async def server(self, ctx):
        if not ctx.guild.banner:
            await ctx.reply("This server does not have a banner.")
        else:
            webp = ctx.guild.banner.replace(format='webp')
            jpg = ctx.guild.banner.replace(format='jpg')
            png = ctx.guild.banner.replace(format='png')
            embed = discord.Embed(
                color=0x00FFCA,
                description=f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp})"
                if not ctx.guild.banner.is_animated() else
                f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp}) | [`GIF`]({ctx.guild.banner.replace(format='gif')})"
            )
            embed.set_image(url=ctx.guild.banner)
            embed.set_author(name=ctx.guild.name,
                             icon_url=ctx.guild.icon.url
                             if ctx.guild.icon else ctx.guild.default_icon.url)
            embed.set_footer(
                text=f"Requested By {ctx.author}",
                icon_url=ctx.author.avatar.url
                if ctx.author.avatar else ctx.author.default_avatar.url)
            await ctx.reply(embed=embed)

    @blacklist_check()
    @ignore_check()
    @banner.command(name="user")
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    async def _user(self,
                    ctx,
                    member: Optional[Union[discord.Member,
                                           discord.User]] = None):
        if member == None or member == "":
            member = ctx.author
        bannerUser = await self.bot.fetch_user(member.id)
        if not bannerUser.banner:
            await ctx.reply("{} does not have a banner.".format(member))
        else:
            webp = bannerUser.banner.replace(format='webp')
            jpg = bannerUser.banner.replace(format='jpg')
            png = bannerUser.banner.replace(format='png')
            embed = discord.Embed(
                color=0x00FFCA,
                description=f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp})"
                if not bannerUser.banner.is_animated() else
                f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp}) | [`GIF`]({bannerUser.banner.replace(format='gif')})"
            )
            embed.set_author(name=f"{member}",
                             icon_url=member.avatar.url
                             if member.avatar else member.default_avatar.url)
            embed.set_image(url=bannerUser.banner)
            embed.set_footer(
                text=f"Requested By {ctx.author}",
                icon_url=ctx.author.avatar.url
                if ctx.author.avatar else ctx.author.default_avatar.url)

            await ctx.send(embed=embed)




    @commands.hybrid_command(name="invite", aliases=['inv'])
    @blacklist_check()
    @ignore_check()
    async def invite(self, ctx: commands.Context):
        embed = discord.Embed(
            title="** <a:999:1160135745114218606> LEGEND's Invite**<a:999:1160135745114218606> ",
            description=
            "> • **[Invite Me ](https://discord.com/api/oauth2/authorize?client_id=1163839531880038460&permissions=8&scope=bot)\n> • [Support Server](https://discord.gg/3Khp9KedDq)**",
            color=0x41eeee)
        embed.set_image(url="https://images-ext-2.discordapp.net/external/3q06ABqkXIYZecNSzlEvFVz9bj02w3ru67jF9JCfE4Y/https/share.creavite.co/hy4VXAZVW2VRsmDI.gif")      
        await ctx.send(embed=embed)

    @commands.hybrid_command(name="vote", aliases=['dbl'], description="Vote Me and Support Us")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @blacklist_check()
    @ignore_check()
    async def _vote(self, ctx):
        button = Button(label="Vote", url = "https://discord.gg/ErJkzJKgBU")

        embed = discord.Embed(color=discord.Colour(0x0d0d13), description="**[Click Here](https://discord.gg/ErJkzJKgBU)** To Vote Me.")
        view = View()
        view.add_item(button)
        embed.set_author(name='Vote LEGEND',
  icon_url=self.bot.user.display_avatar.url)
        await ctx.send(embed=embed, view=view)


    @commands.hybrid_command(name="botinfo",
                             aliases=['bi'],
                             help="Get info about me!",with_app_command = True)
    async def botinfo(self, ctx: commands.Context):
        users = sum(g.member_count for g in self.bot.guilds
                    if g.member_count != None)
        channel = len(set(self.bot.get_all_channels()))
        embed = discord.Embed(color=0x0d0d13,
                              title="LEGEND's Information",
                              description=f"""
**Bot's Mention:** {self.bot.user.mention}
**Bot's Username:** {self.bot.user}
**Total Guilds:** {len(self.bot.guilds)}
**Total Users:** {users}
**Total Channels:** {channel}
**Total Commands: **{len(set(self.bot.walk_commands()))}
**Total Shards:** {len(self.bot.shards)}
**Uptime:** {str(datetime.timedelta(seconds=int(round(time.time()-start_time))))}
**CPU usage:** {round(psutil.cpu_percent())}%
**Memory usage:** {int((psutil.virtual_memory().total - psutil.virtual_memory().available)
 / 1024 / 1024)} MB
**My Websocket Latency:** {int(self.bot.latency * 1000)} ms
**Python Version:** {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}
**Discord.py Version:** {discord.__version__}
""")
        embed.set_footer(text=f"Requested By {ctx.author}",
                         icon_url=ctx.author.avatar.url if ctx.author.avatar
                         else ctx.author.default_avatar.url)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        await ctx.send(embed=embed)


    @blacklist_check()
    @ignore_check()
    @commands.hybrid_command(name="userinfo",
                             aliases=["whois", "ui"],
                             usage="Userinfo [user]",with_app_command = True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    async def _userinfo(self,
                        ctx,
                        member: Optional[Union[discord.Member, discord.User]] = None):
        if member == None or member == "":
            member = ctx.author
        elif member not in ctx.guild.members:
            member = await self.bot.fetch_user(member.id)

        badges = ""
        if member.public_flags.hypesquad:
            badges += "<:Hypesquad:1125037578110914630> "
        if member.public_flags.hypesquad_balance:
            badges += "<:Balance:1162651395917348955>"
        if member.public_flags.hypesquad_bravery:
            badges += "<:Bravery:1162651268368568360>"
        if member.public_flags.hypesquad_brilliance:
            badges += "<:Brillance:1162651323032936458> "
        if member.public_flags.early_supporter:
            badges += "<:EarlySupporter:1162649432584618004>"
        if member.public_flags.active_developer:
            badges += "<:active_developer:1162651151821451324> "
        if member.public_flags.verified_bot_developer:
            badges += "<a:cx_developer:1162658477093687326> "
        if member.public_flags.discord_certified_moderator:
            badges += "<:mod:1162650110610657361>"
        if member.public_flags.staff:
            badges += "<:cdr_IconStaff:1162663142090870876> "
        if member.public_flags.partner:
            badges += "<a:partner:1162650996770607124> "
        if badges == None or badges == "":
            badges += "None"

        if member in ctx.guild.members:
            nickk = f"{member.nick if member.nick else 'None'}"
            joinedat = f"<t:{round(member.joined_at.timestamp())}:R>"
        else:
            nickk = "None"
            joinedat = "None"

        kp = ""
        if member in ctx.guild.members:
            if member.guild_permissions.kick_members:
                kp += " , Kick Members"
            if member.guild_permissions.ban_members:
                kp += " , Ban Members"
            if member.guild_permissions.administrator:
                kp += " , Administrator"
            if member.guild_permissions.manage_channels:
                kp += " , Manage Channels"


#    if  member.guild_permissions.manage_server:
#        kp = "Manage Server"
            if member.guild_permissions.manage_messages:
                kp += " , Manage Messages"
            if member.guild_permissions.mention_everyone:
                kp += " , Mention Everyone"
            if member.guild_permissions.manage_nicknames:
                kp += " , Manage Nicknames"
            if member.guild_permissions.manage_roles:
                kp += " , Manage Roles"
            if member.guild_permissions.manage_webhooks:
                kp += " , Manage Webhooks"
            if member.guild_permissions.manage_emojis:
                kp += " , Manage Emojis"

            if kp is None or kp == "":
                kp = "None"

        if member in ctx.guild.members:
            if member == ctx.guild.owner:
                aklm = "Server Owner"
            elif member.guild_permissions.administrator:
                aklm = "Server Admin"
            elif member.guild_permissions.ban_members or member.guild_permissions.kick_members:
                aklm = "Server Moderator"
            else:
                aklm = "Server Member"

        bannerUser = await self.bot.fetch_user(member.id)
        embed = discord.Embed(color=0x0d0d13)
        embed.timestamp = discord.utils.utcnow()
        if not bannerUser.banner:
            pass
        else:
            embed.set_image(url=bannerUser.banner)
        embed.set_author(name=f"{member.name}'s Information",
                         icon_url=member.avatar.url
                         if member.avatar else member.default_avatar.url)
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.
                            default_avatar.url)
        embed.add_field(name="__General Information__",
                        value=f"""
**Name:** {member}
**ID:** {member.id}
**Nickname:** {nickk}
**Bot?:** {'<a:cx_tick:1158669360223748106> Yes' if member.bot else '<a:no:1158411070608769034> No'}
**Badges:** {badges}
**Account Created:** <t:{round(member.created_at.timestamp())}:R>
**Server Joined:** {joinedat}
            """,
                        inline=False)
        if member in ctx.guild.members:
            r = (', '.join(role.mention for role in member.roles[1:][::-1])
                 if len(member.roles) > 1 else 'None.')
            embed.add_field(name="__Role Info__",
                            value=f"""
**Highest Role:** {member.top_role.mention if len(member.roles) > 1 else 'None'}
**Roles [{f'{len(member.roles) - 1}' if member.roles else '0'}]:** {r if len(r) <= 1024 else r[0:1006] + ' and more...'}
**Color:** {member.color if member.color else '000000'}
                """,
                            inline=False)
        if member in ctx.guild.members:
            embed.add_field(
                name="__Extra__",
                value=
                f"**Boosting:** {f'<t:{round(member.premium_since.timestamp())}:R>' if member in ctx.guild.premium_subscribers else 'None'}\n**Voice <:icons_mic:1162692708566040587>:** {'None' if not member.voice else member.voice.channel.mention}",
                inline=False)
        if member in ctx.guild.members:
            embed.add_field(name="__Key Permissions__",
                            value=", ".join([kp]),
                            inline=False)
        if member in ctx.guild.members:
            embed.add_field(name="__Acknowledgement__",
                            value=f"{aklm}",
                            inline=False)
        if member in ctx.guild.members:
            embed.set_footer(
                text=f"Requested by {ctx.author}",
                icon_url=ctx.author.avatar.url
                if ctx.author.avatar else ctx.author.default_avatar.url)
        else:
            if member not in ctx.guild.members:
                embed.set_footer(
                    text=f"{member.name} not in this this server.",
                    icon_url=ctx.author.avatar.url
                    if ctx.author.avatar else ctx.author.default_avatar.url)
        await ctx.send(embed=embed)


    @blacklist_check()
    @ignore_check()
    @commands.command(name="status",
                      description="Shows users status",
                      usage="status <member>",with_app_command = True)
    async def status(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        status = member.status
        if status == discord.Status.offline:
            status_location = "Not Applicable"
        elif member.mobile_status != discord.Status.offline:
            status_location = "Mobile"
        elif member.web_status != discord.Status.offline:
            status_location = "Browser"
        elif member.desktop_status != discord.Status.offline:
            status_location = "Desktop"
        else:
            status_location = "Not Applicable"
        await ctx.send(embed=discord.Embed(
            title="**<a:randi_dance:1138852908436299907> | status**",
            description="`%s`: `%s`" % (status_location, status),
            color=0x0d0d13))

    @commands.command(name="emoji",
                      help="Shows emoji syntax",
                      usage="emoji <emoji>")
    @blacklist_check()
    @ignore_check()
    async def emoji(self, ctx, emoji: discord.Emoji):
        return await ctx.send(embed=discord.Embed(
            title="**<:icons_emojis:1162692542421270629> | emoji**",
            description="emoji: %s\nid: **`%s`**" % (emoji, emoji.id),
            color=0x41eeee))

    @commands.command(name="user",
                      help="Shows user syntax",
                      usage="user [user]",with_app_command = True)
    @blacklist_check()
    @ignore_check()
    async def user(self, ctx, user: discord.Member = None):
        return await ctx.send(
            embed=discord.Embed(title="user",
                                description="user: %s\nid: **`%s`**" %
                                (user.mention, user.id),
                                color=0x0d0d13))

    @commands.command(name="channel",
                      help="Shows channel syntax",
                      usage="channel <channel>")
    @blacklist_check()
    @ignore_check()
    async def channel(self, ctx, channel: discord.TextChannel):
        return await ctx.send(
            embed=discord.Embed(title="channel",
                                description="channel: %s\nid: **`%s`**" %
                                (channel.mention, channel.id),
                                color=0x00FFCA))





    @commands.hybrid_command(name="steal",
                             help="Adds a emoji",
                             usage="steal <emoji>",
                             aliases=["eadd"],with_app_command = True)
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(manage_emojis=True)
    async def steal(self, ctx, emote):
        try:
            if emote[0] == '<':
                name = emote.split(':')[1]
                emoji_name = emote.split(':')[2][:-1]
                anim = emote.split(':')[0]
                if anim == '<a':
                    url = f'https://cdn.discordapp.com/emojis/{emoji_name}.gif'
                else:
                    url = f'https://cdn.discordapp.com/emojis/{emoji_name}.png'
                try:
                    response = requests.get(url)
                    img = response.content
                    emote = await ctx.guild.create_custom_emoji(name=name,
                                                                image=img)
                    return await ctx.send(
                        embed=discord.Embed(title="emoji-add",
                                            description="added \"**`%s`**\"!" %
                                            (emote),
                                            color=0x41eeee))
                except Exception:
                    return await ctx.send(
                        embed=discord.Embed(title="emoji-add",
                                            description=f"failed to add emoji",
                                            color=0x00FFCA))
            else:
                return await ctx.send(
                    embed=discord.Embed(title="emoji-add",
                                        description=f"invalid emoji",
                                        color=0x41eeee))
        except Exception:
            return await ctx.send(
                embed=discord.Embed(title="emoji-add",
                                    description=f"failed to add emoji",
                                    color=0x41eeee))

    @commands.hybrid_command(name="removeemoji",
                             help="Deletes the emoji from the server",
                             usage="removeemoji <emoji>")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(manage_emojis=False)
    async def removeemoji(self, ctx, emoji: discord.Emoji):
        await emoji.delete()
        await ctx.send(
            "**<a:cx_tick:1158669360223748106> emoji has been deleted.**")

    @commands.hybrid_command(name="unbanall",
                             help="Unbans Everyone In The Guild!",
                             aliases=['massunban'],
                             usage="Unbanall",with_app_command = True)
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unbanall(self, ctx):
        button = Button(label="Yes",
                        style=discord.ButtonStyle.green,
                        emoji="<a:cx_tick:1158669360223748106>")
        button1 = Button(label="No",
                         style=discord.ButtonStyle.red,
                         emoji="<a:no:1158411070608769034>")

        async def button_callback(interaction: discord.Interaction):
            a = 0
            if interaction.user == ctx.author:
                if interaction.guild.me.guild_permissions.ban_members:
                    await interaction.response.edit_message(
                        content="Unbanning All Banned Member(s)",
                        embed=None,
                        view=None)
                    async for idk in interaction.guild.bans(limit=None):
                        await interaction.guild.unban(
                            user=idk.user,
                            reason="Unbanall Command Executed By: {}".format(
                                ctx.author))
                        a += 1
                    await interaction.channel.send(
                        content=f"Successfully Unbanned {a} Member(s)")
                else:
                    await interaction.response.edit_message(
                        content=
                        "I am missing ban members permission.\ntry giving me permissions and retry",
                        embed=None,
                        view=None)
            else:
                await interaction.response.send_message(
                    "This Is Not For You Dummy!",
                    embed=None,
                    view=None,
                    ephemeral=True)

        async def button1_callback(interaction: discord.Interaction):
            if interaction.user == ctx.author:
                await interaction.response.edit_message(
                    content="Ok I will Not unban anyone.",
                    embed=None,
                    view=None)
            else:
                await interaction.response.send_message(
                    "This Is Not For You Dummy!",
                    embed=None,
                    view=None,
                    ephemeral=True)

        embed = discord.Embed(
            color=0x41eeee,
            description=
            '**Are you sure you want to unban everyone in this guild?**')

        view = View()
        button.callback = button_callback
        button1.callback = button1_callback
        view.add_item(button)
        view.add_item(button1)
        await ctx.reply(embed=embed, view=view, mention_author=False)

    @commands.command(name="joined-at",
                      help="Shows when a user joined",
                      usage="joined-at [user]",with_app_command = True)
    @blacklist_check()
    @ignore_check()
    async def joined_at(self, ctx):
        joined = ctx.author.joined_at.strftime("%a, %d %b %Y %I:%M %p")
        await ctx.send(embed=discord.Embed(title="joined-at",
                                           description="**`%s`**" % (joined),
                                           color=0x41eeee))

    @commands.command(name="github", usage="github [search]")
    @blacklist_check()
    @ignore_check()
    async def github(self, ctx, *, search_query):
        json = requests.get(
            f"https://api.github.com/search/repositories?q={search_query}"
        ).json()

        if json["total_count"] == 0:
            await ctx.send("No matching repositories found")
        else:
            await ctx.send(
                f"First result for '{search_query}':\n{json['items'][0]['html_url']}"
            )

    @commands.hybrid_command(name="vcinfo",
                             help="get info about voice channel",
                             usage="Vcinfo <VoiceChannel>",with_app_command = True)
    @blacklist_check()
    @ignore_check()
    async def vcinfo(self, ctx: Context, vc: discord.VoiceChannel):
        e = discord.Embed(title='VC Information', color=0x00FFCA)
        e.add_field(name='VC name', value=vc.name, inline=False)
        e.add_field(name='VC ID', value=vc.id, inline=False)
        e.add_field(name='VC bitrate', value=vc.bitrate, inline=False)
        e.add_field(name='Mention', value=vc.mention, inline=False)
        e.add_field(name='Category name', value=vc.category.name, inline=False)
        await ctx.send(embed=e)

    @commands.hybrid_command(name="channelinfo",
                             help="shows info about channel",
                             aliases=['channeli', 'cinfo', 'ci'],
                             pass_context=False,
                             no_pm=False,
                             usage="Channelinfo [channel]",with_app_command = True)
    @blacklist_check()
    @ignore_check()
    async def channelinfo(self, ctx, *, channel: int = None):
        """Shows channel information"""
        if not channel:
            channel = ctx.message.channel
        else:
            channel = self.bot.get_channel(channel)
        data = discord.Embed()
        if hasattr(channel, 'mention'):
            data.description = "**Information about Channel:** " + channel.mention
        if hasattr(channel, 'changed_roles'):
            if len(channel.changed_roles) > 0:
                data.color = 0x00FFCA if channel.changed_roles[
                    0].permissions.read_messages else 0x00FFCA
        if isinstance(channel, discord.TextChannel):
            _type = "Text"
        elif isinstance(channel, discord.VoiceChannel):
            _type = "Voice"
        else:
            _type = "Unknown"
        data.add_field(name="Type", value=_type)
        data.add_field(name="ID", value=channel.id, inline=False)
        if hasattr(channel, 'position'):
            data.add_field(name="Position", value=channel.position)
        if isinstance(channel, discord.VoiceChannel):
            if channel.user_limit != 0:
                data.add_field(name="User Number",
                               value="{}/{}".format(len(channel.voice_members),
                                                    channel.user_limit))
            else:
                data.add_field(name="User Number",
                               value="{}".format(len(channel.voice_members)))
            userlist = [r.display_name for r in channel.members]
            if not userlist:
                userlist = "None"
            else:
                userlist = "\n".join(userlist)
            data.add_field(name="Users", value=userlist)
            data.add_field(name="Bitrate", value=channel.bitrate)
        elif isinstance(channel, discord.TextChannel):
            try:
                pins = await channel.pins()
                data.add_field(name="Pins", value=len(pins), inline=False)
            except discord.Forbidden:
                pass
            data.add_field(name="Members", value="%s" % len(channel.members))
            if channel.topic:
                data.add_field(name="Topic", value=channel.topic, inline=False)
            hidden = []
            allowed = []
            for role in channel.changed_roles:
                if role.permissions.read_messages is False:
                    if role.name != "@everyone":
                        allowed.append(role.mention)
                elif role.permissions.read_messages is False:
                    if role.name != "@everyone":
                        hidden.append(role.mention)
            if len(allowed) > 0:
                data.add_field(name='Allowed Roles ({})'.format(len(allowed)),
                               value=', '.join(allowed),
                               inline=False)
            if len(hidden) > 0:
                data.add_field(name='Restricted Roles ({})'.format(
                    len(hidden)),
                               value=', '.join(hidden),
                               inline=False)
        if channel.created_at:
            data.set_footer(text=("Created on {} ({} days ago)".format(
                channel.created_at.strftime("%d %b %Y %H:%M"), (
                    ctx.message.created_at - channel.created_at).days)))
        await ctx.send(embed=data)

    @commands.command(name="note",
                      help="Creates a note for you",
                      usage="Note <message>")
    @cooldown(1, 10, BucketType.user)
    @blacklist_check()
    @ignore_check()
    async def note(self, ctx, *, message):
        message = str(message)
        print(message)
        stats = await notedb.find_one({"id": ctx.author.id})
        if len(message) <= 50:
            #
            if stats is None:
                newuser = {"id": ctx.author.id, "note": message}
                await notedb.insert_one(newuser)
                await ctx.send("**Your note has been stored**")
                await ctx.message.delete()

            else:
                x = notedb.find({"id": ctx.author.id})
                z = 0
                async for i in x:
                    z += 1
                if z > 2:
                    await ctx.send("**You cannot add more than 3 notes**")
                else:
                    newuser = {"id": ctx.author.id, "note": message}
                    await notedb.insert_one(newuser)
                    await ctx.send("**Yout note has been stored**")
                    await ctx.message.delete()

        else:
            await ctx.send("**Message cannot be greater then 50 characters**")

    @commands.command(name="notes", help="Shows your note", usage="Notes")
    @blacklist_check()
    @ignore_check()
    async def notes(self, ctx):
        stats = await notedb.find_one({"id": ctx.author.id})
        if stats is None:
            embed = discord.Embed(
                timestamp=ctx.message.created_at,
                title="Notes",
                description=f"{ctx.author.mention} has no notes",
                color=0x00FFCA,
            )
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(title="Notes",
                                  description=f"Here are your notes",
                                  color=0x00FFCA)
            x = notedb.find({"id": ctx.author.id})
            z = 1
            async for i in x:
                msg = i["note"]
                embed.add_field(name=f"Note {z}", value=f"{msg}", inline=False)
                z += 1
            await ctx.send(embed=embed)
        #  await ctx.send("**Please check your private messages to see your notes**")

    @commands.command(name="trashnotes",
                      help="Delete the notes , it's a good practice",
                      usage="Trashnotes",with_app_command = True)
    @blacklist_check()
    @ignore_check()
    async def trashnotes(self, ctx):
        try:
            await notedb.delete_many({"id": ctx.author.id})
            await ctx.send("**Your notes have been deleted , thank you**")
        except:
            await ctx.send("**You have no record**")

    @commands.hybrid_command(name="badges",
                             help="Check what premium badges a user have.",
                             aliases=["badge", "profile", "pr"],
                             usage="Badges [user]",with_app_command = True)
    @blacklist_check()
    @ignore_check()
    async def _badges(self, ctx, user: Optional[discord.User] = None):

        mem = user or ctx.author
        bdgs = getbadges(mem.id)
        badges = ""
        if mem.public_flags.hypesquad:
            badges += "Hypesquad\n"
        elif mem.public_flags.hypesquad_balance:
            badges += "<:Balance:1162651395917348955> **HypeSquad Balance**\n"

        elif mem.public_flags.hypesquad_bravery:
            badges += "<:Bravery:1162651268368568360> **HypeSquad Bravery**\n"
        elif mem.public_flags.hypesquad_brilliance:
            badges += "<:Brillance:1162651323032936458> **Hypesquad Brilliance**\n"
        if mem.public_flags.early_supporter:
            badges += "<:EarlySupporter:1162649432584618004> **Early Supporter**\n"
        elif mem.public_flags.verified_bot_developer:
            badges += "<a:cx_developer:1162658477093687326> **Verified Bot Developer**\n"
        elif mem.public_flags.active_developer:
            badges += "<:active_developer:1162651151821451324> **Active Developer**\n"
        if badges == "":
            badges = "None"
        if bdgs == []:
            embed2 = discord.Embed(color=mem.color)
            embed2.add_field(name="**User Badges:**",
                             value=f"{badges}",
                             inline=False)
            embed2.add_field(
                name="**Bot Badges:**",
                value="**<a:Cosy_girl_shy:1162081346865340457> Family**",
                inline=False)
            embed2.set_author(name=f"{mem}",
                              icon_url=mem.avatar.url
                              if mem.avatar else mem.default_avatar.url)
            embed2.set_thumbnail(
                url=mem.avatar.url if mem.avatar else mem.default_avatar.url)
            await ctx.reply(embed=embed2, mention_author=False)
        else:
            embed = discord.Embed(color=mem.color)
            embed.add_field(name="**User Badges:**",
                            value=f"{badges}",
                            inline=False)
            embed.add_field(name="**Bot Badges:**",
                            value="\n".join([bdg for bdg in bdgs]),
                            inline=False)
            embed.set_author(name=f"{mem}",
                             icon_url=mem.avatar.url
                             if mem.avatar else mem.default_avatar.url)
            embed.set_thumbnail(
                url=mem.avatar.url if mem.avatar else mem.default_avatar.url)
            await ctx.reply(embed=embed, mention_author=False)



    @commands.hybrid_command(name="ping",
                             aliases=["latency"],
                             usage="Checks the bot latency .",with_app_command = True)
    @ignore_check()
    @blacklist_check()
    async def ping(self, ctx):
        embed = discord.Embed(
            title="",
            description=f"**Pong 🏓 in {int(self.bot.latency * 1000)} ms ** ",
            color=0x41eeee)
        await ctx.reply(embed=embed)




    @commands.hybrid_command(name="source", description="Source of LEGEND")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    async def _source(self, ctx):
        button = Button(label="Code", url = "https://github.com/discord.py")
        button1 = Button(label="Tutorial", url = "https://youtu.be/xvFZjo5PgG0")

        embed = discord.Embed(color=discord.Colour(0xff0000),title="LEGEND Bot Source Code", description="Click the buttons below to access the source code and tutorial.")
        view = View()
        view.add_item(button)
        view.add_item(button1)
        embed.set_author(name=f"{ctx.author.name}",
                         icon_url=f"{ctx.author.avatar}")
        embed.set_footer(text="LEGEND Bot Source Code")
        await ctx.send(embed=embed, view=view)

    @commands.hybrid_command(name="statistics",
                             aliases=["st", "stats"],
                             usage="stats",
                             with_app_command=True)
    @blacklist_check()
    @ignore_check()
    async def stats(self, ctx):
        """Shows some usefull information about LEGEND"""
        loading_message = await ctx.send(embed=discord.Embed(
        color=0x2f3136,
        description="**<a:loading:1160242511533588650> Fetching Info From Database...**"
    ))

        serverCount = len(self.bot.guilds)
        textchannel = sum(len(guild.text_channels) for guild in self.bot.guilds)
        voicechannel = sum(len(guild.voice_channels) for guild in self.bot.guilds)
        categorichannel = sum(len(guild.categories) for guild in self.bot.guilds)
        total = textchannel + voicechannel + categorichannel
        cached = len(self.bot.users)

        used_memory = psutil.virtual_memory().percent
        cpu_used = str(psutil.cpu_percent())
        shard_count = self.bot.shard_count

        total_members = sum(g.member_count for g in self.bot.guilds
                            if g.member_count != None)

        pain = await self.bot.fetch_user(1036877996243562516)
        papa = await self.bot.fetch_user(926831289649201213)
        uts = await self.bot.fetch_user(1069894893410979850)
        #button2 = Button(label="Vote", url = "https://top.gg/bot/1136504108937908305/vote")
        button = Button(label="Support Server", url = "https://discord.gg/3Khp9KedDq")
        button1 = Button(label="Invite Me", url = "https://discord.com/api/oauth2/authorize?client_id=1163839531880038460&permissions=8&scope=bot")

        await asyncio.sleep(0000)

        embed = discord.Embed(
            color=0x2f3136,
            description=
            "**Hey, It's Me LEGEND A Feature Rich Advanced Multipurpose Bot. Build The Community Of Your Dreams With Me. Try LEGEND Now!**"
        )

        embed.add_field(
            name="**<a:moon:1158411057325428756> DEVELOPER**",
            value=f"[{pain}](https://discord.com/users/926831289649201213)\n[{papa}](https://discord.com/users/1125692368247595029)\n[{uts}](https://discord.com/users/1037912777932681338)")
        embed.add_field(
            name="**<a:cx_crown:1158669179059183687> OWNERS**",
            value=f"[{pain}](https://discord.com/users/926831289649201213)\n[{papa}](https://discord.com/users/1125692368247595029)",
        inline=False)
        embed.add_field(name='**Bot Stat(s)**',
                        value=f"**→** Total Guilds: **{serverCount} Guilds**\n**→** Total Users: **{total_members} Users | {cached} Cached**\n**→** Channels:\n- Total: **{total} Channels**\n- Text: **{textchannel} Channels**\n- Voice: **{voicechannel} Channels**\n- Categories: **{categorichannel} Channels**",
                            inline=False)
        embed.add_field(
            name="**Server(s) Usage**",
            value=
            f"**→** CPU Usage: **{cpu_used}%**\n**→** Memory Usage: **{used_memory}%**",
                            inline=False)
        embed.add_field(
            name="**Shard(s)**",
            value=f"**{ctx.guild.shard_id + 1}/{shard_count}**",
                            inline=False)

        view = View()
        view.add_item(button)
        view.add_item(button1)
        #view.add_item(button2)
        embed.set_author(name=f"About {self.bot.user.name}",
                         icon_url=self.bot.user.display_avatar.url)
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)

        await loading_message.delete()
        await ctx.send(embed=embed, view=view)