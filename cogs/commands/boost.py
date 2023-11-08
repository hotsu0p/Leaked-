
from __future__ import annotations
import discord
import asyncio
import os
import logging
from discord.ext import commands
from utils.Tools import *
from discord.ext.commands import Context
from discord import app_commands
import time
import datetime
import re
from typing import *
from time import strftime
from core import Cog, Astroz, Context
from discord.ext import commands

logging.basicConfig(
    level=logging.INFO,
    format=
    "\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)
#welcome

class boost(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.group(name="boost",
                    aliases=['bst'],
                    invoke_without_command=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _boost(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)
            ctx.command.reset_cooldown(ctx)

    @_boost.command(name="thumbnail", help="Setups boost thumbnail .")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _boost_thumbnail(self, ctx, thumbnail_link):
        data = getDB1(ctx.guild.id)
        streamables = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if streamables.search(thumbnail_link):
                data["boost"]["thumbnail"] = thumbnail_link
                updateDB1(ctx.guild.id, data)
                hacker = discord.Embed(
                    color=0x2f3136,
                    description=
                    "<a:cx_tick:1158669360223748106> | Successfully updated the boost thumbnail url .",
                    timestamp=ctx.message.created_at)
                hacker.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=hacker)
            else:
                await ctx.send("Oops, Kindly put a valid link.")
        else:
            hacker5 = discord.Embed(description="""```diff
 - You must have Administrator permission. - Your top role should be above my top role. 
```""",
                                    color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")

            await ctx.send(embed=hacker5)

    @_boost.command(name="image", help="Setups boost image.")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _boost_image(self, ctx, *, image_link):
        data = getDB1(ctx.guild.id)
        streamables = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$',
            re.IGNORECASE)

        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if streamables.search(image_link):
                data["boost"]["image"] = image_link
                updateDB1(ctx.guild.id, data)
                hacker = discord.Embed(
                    color=0x2f3136,
                    description=
                    "<a:cx_tick:1158669360223748106> | Successfully updated the boost image url .",
                    timestamp=ctx.message.created_at)
                hacker.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=hacker)
            else:
                await ctx.send("Oops, Kindly put a valid link.")
        else:
            hacker5 = discord.Embed(description="""```diff
 - You must have Administrator permission. - Your top role should be above my top role. 
```""",
                                    color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")

            await ctx.send(embed=hacker5)

    @_boost.command(name="autodel",
                    help="Automatically delete message after x seconds .")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _boost_autodel(self, ctx, *, autodelete_second):
        data = getDB1(ctx.guild.id)
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            data['boost']['autodel'] = autodelete_second
            updateDB1(ctx.guild.id, data)
            hacker = discord.Embed(
                color=0x2f3136,
                description=
                f"<a:cx_tick:1158669360223748106> | Successfully updated the boost autodelete second to {autodelete_second} .\nFrom now boost message will be deleted after {autodelete_second} .",
                timestamp=ctx.message.created_at)
            hacker.set_author(name=f"{ctx.author.name}",
                              icon_url=f"{ctx.author.avatar}")
            await ctx.send(embed=hacker)
        else:
            hacker5 = discord.Embed(description="""```diff
 - You must have Administrator permission. - Your top role should be above my top role. 
```""",
                                    color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")

            await ctx.send(embed=hacker5)

    @_boost.command(name="message", help="Setups boost message.")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _boost_message(self, ctx: commands.Context):
        data = getDB1(ctx.guild.id)

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            msg = discord.Embed(
                color=0x2f3136,
                description=
                """Here are some keywords, which you can use in your boost message.\n\nSend your boost message in this channel now.\n\n\n```xml\n<<server.boost_count>> = server boost count\n<<boost.server_name>> = boosted server name\n<<boost.user_name>> = username of booster\n<<boost.user_mention>> = mention the booster user\n<<user.boosted_at>> = when the user boost the server\n```"""
            )
            await ctx.send(embed=msg)
            try:
                welcmsg = await self.bot.wait_for('message',
                                                  check=check,
                                                  timeout=30.0)
            except asyncio.TimeoutError:
                await ctx.send("Oops, too late. bye")
                return
            else:
                data["boost"]["message"] = welcmsg.content
                updateDB1(ctx.guild.id, data)
                hacker = discord.Embed(
                    color=0x2f3136,
                    description=
                    f"<a:cx_tick:1158669360223748106> | Successfully updated the boost message .",
                    timestamp=ctx.message.created_at)
                hacker.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=hacker)
        else:
            hacker5 = discord.Embed(description="""```diff
 - You must have Administrator permission. - Your top role should be above my top role. 
```""",
                                    color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")

            await ctx.send(embed=hacker5)

    @_boost.command(name="embed", help="Toggle embed for boost message .")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _boost_embed(self, ctx):
        data = getDB1(ctx.guild.id)
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if data["boost"]["embed"] == True:
                data["boost"]["embed"] = False
                updateDB1(ctx.guild.id, data)
                hacker = discord.Embed(
                    color=0x2f3136,
                    description=
                    f"<a:cx_tick:1158669360223748106> | Okay, Now your embed is removed and boost message will be a plain message .",
                    timestamp=ctx.message.created_at)
                hacker.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=hacker)
            elif data["boost"]["embed"] == False:
                data["boost"]["embed"] = True
                updateDB1(ctx.guild.id, data)
                hacker1 = discord.Embed(
                    color=0x2f3136,
                    description=
                    f"<a:cx_tick:1158669360223748106> | Okay, Now your embed is enabled and boost message will be a embed message.",
                    timestamp=ctx.message.created_at)
                hacker1.set_author(name=f"{ctx.author.name}",
                                   icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=hacker1)
        else:
            hacker5 = discord.Embed(description="""```diff
 - You must have Administrator permission. - Your top role should be above my top role. 
```""",
                                    color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")

            await ctx.send(embed=hacker5)

    @_boost.command(name="ping", help="Toggle embed ping for boostr.")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _boost_ping(self, ctx):
        data = getDB1(ctx.guild.id)
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if data["boost"]["ping"] == True:
                data["boost"]["ping"] = False
                updateDB1(ctx.guild.id, data)
                hacker = discord.Embed(
                    color=0x2f3136,
                    description=
                    f"<a:cx_tick:1158669360223748106> | Okay, Now your embed ping is disabled and users won't get pinged upon boost .",
                    timestamp=ctx.message.created_at)
                hacker.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=hacker)
            elif data["boost"]["ping"] == False:
                data["boost"]["ping"] = True
                updateDB1(ctx.guild.id, data)
                hacker1 = discord.Embed(
                    color=0x2f3136,
                    description=
                    f"<a:cx_tick:1158669360223748106> | Okay, Now your embed ping is enabled and I will ping new users outside the embed .",
                    timestamp=ctx.message.created_at)
                hacker1.set_author(name=f"{ctx.author.name}",
                                   icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=hacker1)
        else:
            hacker5 = discord.Embed(description="""```diff
 - You must have Administrator permission. - Your top role should be above my top role. 
```""",
                                    color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")

            await ctx.send(embed=hacker5)

    @_boost.group(name="channel", help="Setups boost channel.")
    @blacklist_check()
    @ignore_check()
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _boost_channel(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)
            ctx.command.reset_cooldown(ctx)

    @_boost_channel.command(name="add",
                            help="Add a channel to the boost channels list.")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _boost_channel_add(self, ctx, channel: discord.TextChannel):
        data = getDB1(ctx.guild.id)
        chh = data["boost"]["channel"]
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if len(chh) == 1:
                hacker = discord.Embed(
                    color=0x2f3136,
                    description=
                    f"<a:no:1158411070608769034> | You have reached maximum channel limit for channel which is one .",
                    timestamp=ctx.message.created_at)
                hacker.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=hacker)
            else:
                if str(channel.id) in chh:
                    hacker1 = discord.Embed(
                        color=0x2f3136,
                        description=
                        f"<a:no:1158411070608769034> | This channel is already in the boost channels list .",
                        timestamp=ctx.message.created_at)
                    hacker1.set_author(name=f"{ctx.author.name}",
                                       icon_url=f"{ctx.author.avatar}")
                    await ctx.send(embed=hacker1)
                else:
                    chh.append(str(channel.id))
                    updateDB1(ctx.guild.id, data)
                    hacker4 = discord.Embed(
                        color=0x2f3136,
                        description=
                        f"<a:cx_tick:1158669360223748106> | Successfully added {channel.mention} to boost channel list .",
                        timestamp=ctx.message.created_at)
                    hacker4.set_author(name=f"{ctx.author.name}",
                                       icon_url=f"{ctx.author.avatar}")
                    await ctx.send(embed=hacker4)
        else:
            hacker5 = discord.Embed(description="""```diff
 - You must have Administrator permission. - Your top role should be above my top role. 
```""",
                                    color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")

            await ctx.send(embed=hacker5)

    @_boost_channel.command(name="remove",
                            help="Remove a chanel from boost channels list ."
                            )
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _boost_channel_remove(self, ctx, channel: discord.TextChannel):
        data = getDB1(ctx.guild.id)
        chh = data["boost"]["channel"]
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if len(chh) == 0:
                hacker = discord.Embed(
                    color=0x2f3136,
                    description=
                    f"<a:no:1158411070608769034> | This server dont have any boost channel setupped yet .",
                    timestamp=ctx.message.created_at)
                hacker.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=hacker)
            else:
                if str(channel.id) not in chh:
                    hacker1 = discord.Embed(
                        color=0x2f3136,
                        description=
                        f"<a:no:1158411070608769034> | This channel is not in the boost channels list .",
                        timestamp=ctx.message.created_at)
                    hacker1.set_author(name=f"{ctx.author.name}",
                                       icon_url=f"{ctx.author.avatar}")
                    await ctx.send(embed=hacker1)
                else:
                    chh.remove(str(channel.id))
                    updateDB1(ctx.guild.id, data)
                    hacker3 = discord.Embed(
                        color=0x2f3136,
                        description=
                        f"<a:cx_tick:1158669360223748106> | Successfully removed {channel.mention} from boost channel list .",
                        timestamp=ctx.message.created_at)
                    hacker3.set_author(name=f"{ctx.author.name}",
                                       icon_url=f"{ctx.author.avatar}")
                    await ctx.send(embed=hacker3)
        else:
            hacker5 = discord.Embed(description="""```diff
 - You must have Administrator permission. - Your top role should be above my top role. 
```""",
                                    color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")

            await ctx.send(embed=hacker5)

    @_boost.command(name="test",
                    help="Test the boost message how it will look like.")
    @blacklist_check()
    @ignore_check()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def welctestt(self, ctx):
        data = getDB1(ctx.guild.id)
        msg = data["boost"]["message"]
        chan = list(data["boost"]["channel"])
        emtog = data["boost"]["embed"]
        emping = data["boost"]["ping"]
        emimage = data["boost"]["image"]
        emthumbnail = data["boost"]["thumbnail"]
        emautodel = data["boost"]["autodel"]
        user = ctx.author
        if chan == []:
            hacker = discord.Embed(
                color=0x2f3136,
                description=
                f"<a:no:1158411070608769034> | Oops, Kindly setup your boost channel first .",
                timestamp=ctx.message.created_at)
            hacker.set_author(name=f"{ctx.author.name}",
                              icon_url=f"{ctx.author.avatar}")
            await ctx.send(embed=hacker)
        else:
            if "<<boost.server_name>>" in msg:
                msg = msg.replace("<<boost.server_name>>", "%s" % (user.guild.name))
            if "<<server.boost_count>>" in msg:
                msg = msg.replace("<<server.boost_count>>",
                                  "%s" % (user.guild.premium_subscription_count))
            if "<<boost.user_name>>" in msg:
                msg = msg.replace("<<boost.user_name>>", "%s" % (user))
            if "<<boost.user_mention>>" in msg:
                msg = msg.replace("<<boost.user_mention>>", "%s" % (user.mention))
            if "<<user.boosted_at>>" in msg:
                msg = msg.replace("<<user.boosted_at>>",
                                  f"<t:{int(user.premium_since.timestamp())}:F>")

            if emping == True:
                emping = f"{ctx.author.mention}"
            else:
                emping = ""
            if emautodel == 0 or emautodel == "":
                emautodel = None
            else:
                emautodel = emautodel
            em = discord.Embed(description=msg, color=0x2f3136)
            em.set_author(name=ctx.author.name,
                          icon_url=ctx.author.avatar.url if ctx.author.avatar
                          else ctx.author.default_avatar.url)
            em.timestamp = discord.utils.utcnow()
            hacker1 = {emautodel}
            if emimage == "":
                em.set_image(url=None)
            else:
                em.set_image(url=emimage)

            if emthumbnail == "":
                em.set_thumbnail(url=None)
            else:
                em.set_thumbnail(url=emthumbnail)
            if user.guild.icon is not None:
                em.set_footer(text=user.guild.name,
                              icon_url=user.guild.icon.url)

            for chann in chan:
                channn = self.bot.get_channel(int(chann))
            if emtog == True:
                await channn.send(emping, embed=em)
            else:
                if emtog == False:
                    await channn.send(msg)

    @_boost.command(name="config", help="Get boost config for the server.")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def _config(self, ctx):
        data = getDB1(ctx.guild.id)
        msg = data["boost"]["message"]
        chan = list(data["boost"]["channel"])
        emtog = data["boost"]["embed"]
        emping = data["boost"]["ping"]
        emtog = data["boost"]["embed"]
        emimage = data["boost"]["image"]
        emthumbnail = data["boost"]["thumbnail"]
        emautodel = data["boost"]["autodel"]


        if chan == []:
            await ctx.reply(
                "First setup Your boost channel by Running `boost channel add #channel/id`"
            )
        else:
            
            embed = discord.Embed(color=0x2f3136,
                                  title=f"BoostMessage Config For {ctx.guild.name}")
            if emtog == True:                
                em = "Enabled"
            else:
                em = "Disabled"

            if emping == True:
               ping = "Enabled"
            else:
               ping = "Disabled"
            for chh in chan:
                    ch = self.bot.get_channel(int(chh))
            embed.add_field(name="**BoostMessage Channel:**", value=ch)
            
                                 
            embed.add_field(name="**BoostMessage Message:**", value=f"{msg}")

            embed.add_field(name="**BoostMessage Embed:**", value=em)

            embed.add_field(name="**BoostMessage Ping:**", value=f"{ping}")
            if ctx.guild.icon is not None:
                embed.set_footer(text=ctx.guild.name,
                                 icon_url=ctx.guild.icon.url)
                embed.set_thumbnail(url=ctx.guild.icon.url)

        await ctx.send(embed=embed)

    @_boost.command(name="reset", help="Clear boost config for the server.")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def _reset(self, ctx):
        data = getDB1(ctx.guild.id)
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if data["boost"]["channel"] == []:
                embed = discord.Embed(
                    description=
                    "<a:no:1158411070608769034> | This server don't have any boost channel setuped yet .",
                    color=0x2f3136)
                await ctx.send(embed=embed)
            else:
                data["boost"]["channel"] = []
                data["boost"]["image"] = ""
                data["boost"]["message"] = "<<boost.user_mention>> BoostMessage To <<boost.server_name>>"
                data["boost"]["thumbnail"] = ""
                updateDB1(ctx.guild.id, data)
                hacker = discord.Embed(
                    description=
                    "<a:cx_tick:1158669360223748106> | Succesfully cleared all boost config for this server .",
                    color=0x2f3136)
                await ctx.send(embed=hacker)
        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have Administrator permission.\n - Your top role should be above my top role.```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")
            await ctx.send(embed=hacker5)

    @commands.group(name="boostrole", invoke_without_command=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @blacklist_check()
    @ignore_check()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _boostrole(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)
            ctx.command.reset_cooldown(ctx)

    @_boostrole.command(name="config")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def _ar_config(self, ctx):
        if data := getDB1(ctx.guild.id):
            hum = list(data["boost1"]["role"])

            fetched_role: list = []

            #if data["boost1"]["role"] != []:
            for i in hum:
                role = ctx.guild.get_role(int(i))
                if role is not None:
                    fetched_role.append(role)

            #if data["boost1"]["bots"] != []:


            hums = "\n".join(i.mention for i in fetched_role)
            if not hums:
                hums = " Boost role Not Set."


            emb = discord.Embed(
                color=0x2f3136,
                title=f"Boost role of - {ctx.guild.name}").add_field(
                    name="__Role__", value=hums,
                    inline=False)

            await ctx.send(embed=emb)



    @_boostrole.command(name="reset",
                             help="Clear boost role config for the server .")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def _boost1_role_reset(self, ctx):
        data = getDB1(ctx.guild.id)
        rl = data["boost1"]["role"]
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if rl == []:
                embed = discord.Embed(
                    description=
                    "<a:no:1158411070608769034> | This server don't have any boost role setupped .",
                    color=0x2f3136)
                await ctx.send(embed=embed)
            else:
                if rl != []:
                    data["boost1"]["role"] = []
                    updateDB1(ctx.guild.id, data)
                    hacker = discord.Embed(
                        description=
                        f"<a:cx_tick:1158669360223748106> | Succesfully cleared all boost role for {ctx.guild.name} .",
                        color=0x2f3136)
                    await ctx.send(embed=hacker)
        else:
            hacker5 = discord.Embed(
                description=
                """```diff\n - You must have Administrator permission.\n - Your top role should be above my top role. \n```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")

            await ctx.send(embed=hacker5)





    @_boostrole.command(name="add",
                              help="Add role to list of boost role."
                              )
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _boost1_role_add(self, ctx, role: discord.Role):
        data = getDB1(ctx.guild.id)
        rl = data["boost1"]["role"]
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if len(rl) == 5:
                embed = discord.Embed(
                    description=
                    f"<a:no:1158411070608769034> | You have reached maximum channel limit for boost role which is five .",
                    color=0x2f3136)
                await ctx.send(embed=embed)
            else:
                if str(role.id) in rl:
                    embed1 = discord.Embed(
                        description=
                        "<a:no:1158411070608769034> | {} is already in boost role ."
                        .format(role.mention),
                        color=0x2f3136)
                    await ctx.send(embed=embed1)
                else:
                    rl.append(str(role.id))
                    updateDB1(ctx.guild.id, data)
                    hacker = discord.Embed(
                        description=
                        f"<a:cx_tick:1158669360223748106> | {role.mention} has been added to boost role .",
                        color=0x2f3136)
                    await ctx.send(embed=hacker)
        else:
            hacker5 = discord.Embed(
                description=
                """```diff\n - You must have Administrator permission.\n - Your top role should be above my top role. \n```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")

            await ctx.send(embed=hacker5)

    @_boostrole.command(
        name="remove", help="Remove a role from boost role.")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _boost1_role_remove(self, ctx, role: discord.Role):
        data = getDB1(ctx.guild.id)
        rl = data["boost1"]["role"]
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if len(rl) == 0:
                embed = discord.Embed(
                    description=
                    f"<a:no:1158411070608769034> | This server dont have any boost role setupped yet .",
                    color=0x2f3136)
                await ctx.send(embed=embed)
            else:
                if str(role.id) not in rl:
                    embed1 = discord.Embed(
                        description="{} is not in boost role .".format(
                            role.mention),
                        color=0x2f3136)
                    await ctx.send(embed=embed1)
                else:
                    rl.remove(str(role.id))
                    updateDB1(ctx.guild.id, data)
                    hacker = discord.Embed(
                        description=
                        f"<a:cx_tick:1158669360223748106> | {role.mention} has been removed from boost role .",
                        color=0x2f3136)
                    await ctx.send(embed=hacker)
        else:
            hacker5 = discord.Embed(
                description=
                """```diff\n - You must have Administrator permission.\n - Your top role should be above my top role. \n```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")

            await ctx.send(embed=hacker5)