import discord
import wavelink
from wavelink.ext import spotify
from discord.ext import commands
import logging
from typing import Any, Dict, Union, Optional
from discord.enums import try_enum
import os
import datetime
import datetime as dt
import datetime

import typing as t
import requests
import re
from discord.ext.commands.errors import CheckFailure
import asyncio
import os
from wavelink import Player
import async_timeout
from utils.Tools import *
from wavelink.filters import Karaoke, Timescale

class MusicFilters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



@commands.group(name="nightcore",
                invoke_without_command=True,
                aliases=['nc'])
@blacklist_check()
@ignore_check()
async def _nightcore(self, ctx):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

@_nightcore.command(name="enable", aliases=[("on")])
@blacklist_check()
@ignore_check()
async def enable_nightcore(self, ctx: commands.Context):
    vc: wavelink.Player = ctx.voice_client

    if vc is None:
        hacker = discord.Embed(
            description=
            "<:red_cross:1098131641169350707> | You are not connected to a voice channel.",
            color=0x41eeee)
        hacker.set_footer(text=f"Requested By {ctx.author}",
                          icon_url=f"{ctx.author.avatar}")
        #hacker.set_thumbnail(url = f"{ctx.author.avatar}")
        
        return await ctx.reply(embed=hacker)
    
    # add nightcore filter
    nightcore_filter = wavelink.Filter(
        timescale=Timescale(rate=1.3),
        karaoke=Karaoke(level=1.0, mono_level=1.0, filter_band=220, filter_width=100)
    )
    
    await vc.set_filter(nightcore_filter, seek=True)
    hacker4 = discord.Embed(
        description=
        "<a:cx_tick:1158669360223748106> | Successfully enabled `nightcore` filter.",
        color=0x41eeee)

    await ctx.reply(embed=hacker4)
