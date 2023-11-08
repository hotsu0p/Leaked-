import discord
from discord.ext import commands,tasks
import os
import sys
import datetime
import re
from dateutil.relativedelta import relativedelta
from typing import Optional
import json
import asyncio
from utils.Tools import *

class ShortTime:
    compiled = re.compile(
        """
            (?:(?P<years>[0-9])(?:years?|y))?             # e.g. 2y
            (?:(?P<months>[0-9]{1,2})(?:months?|mo))?     # e.g. 2months
            (?:(?P<weeks>[0-9]{1,4})(?:weeks?|w))?        # e.g. 10w
            (?:(?P<days>[0-9]{1,5})(?:days?|d))?          # e.g. 14d
            (?:(?P<hours>[0-9]{1,5})(?:hours?|h))?        # e.g. 12h
            (?:(?P<minutes>[0-9]{1,5})(?:minutes?|m))?    # e.g. 10m
            (?:(?P<seconds>[0-9]{1,5})(?:seconds?|s))?    # e.g. 15s
        """,
        re.VERBOSE,
    )

    def __init__(self, argument: Optional[str], *, now=None):
        self.argument = argument
        match = self.compiled.fullmatch(str(argument).lower())
        if match is None or not match.group(0):
            raise commands.BadArgument(
                "Invalid time provided. Try something like this: `5m`, `2h` or `60s`"
            )

        data = {k: int(v) for k, v in match.groupdict(default=0).items()}
        now = now or datetime.datetime.now(datetime.timezone.utc)
        self.dt: datetime.datetime = now + relativedelta(**data)

    def __str__(self) -> str:
        return str(self.argument)

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    async def convert(cls, ctx, argument):
        return cls(argument, now=ctx.message.created_at)


async def create_timer(id, name, exp, cre, auth, c):
  with open("remind.json", "r") as f:
    datab = json.load(f)
  data = {'name': name, "id": id, "guild": c.guild.id, "created": cre, "expire": exp, "author": auth.id, "channel": c.id}
  datab[str(id)] = data
  with open("remind.json", "w") as f:
    json.dump(datab, f, indent=4)
  
async def delete_timer(id):
  with open("remind.json", "r") as f:
    data = json.load(f)
    if not data.get(str(id)):
      return "Land"
  data.pop(str(id))
  with open("remind.json", "w") as f:
    json.dump(data, f, indent=4)

class Reminder(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self._ling = asyncio.Lock()

  @tasks.loop(seconds=3)
  async def clear_reminders(self):
    with open("remind.json", "r") as f:
      data = json.load(f)
    if data == {}:
      return
    async with self._ling:
      for id in data:
        inf = data.get(str(id))
        if discord.utils.utcnow().timestamp() >= inf["expire"]:
          self.bot.dispatch("timer_end", **inf)
          await delete_timer(id)
          await asyncio.sleep(0)

  @clear_reminders.before_loop
  async def br(self):
    await self.bot.wait_until_ready()

  @commands.Cog.listener()
  async def on_ready(self):
    print("Reminder Commands")
    await self.clear_reminders.start()

  @commands.hybrid_group(name="remind",aliases=["reminder"],invoke_without_command=True)
  @blacklist_check()
  @ignore_check()
  async def _ling(self,ctx):
    embed = discord.Embed(title=f'`{ctx.prefix}reminder <when>`', description=f'`{ctx.prefix}reminder start`\nCreates a reminder.\n\n`{ctx.prefix}reminder delete`\nDeletes a reminder with message id.', color=0x00FFCA)
    await ctx.send(embed=embed)
    

  @_ling.command(name="start", aliases=["create", "set"])
  @blacklist_check()
  @ignore_check()
  async def ling(self,ctx,tame: ShortTime,name="..."):
    s= tame.dt.timestamp()
    await create_timer(ctx.message.id, name, s, ctx.message.created_at.timestamp(), ctx.message.author,ctx.channel)
    await ctx.send(f"Alright **{ctx.message.author}**, I'll remind you in **<t:{int(s)}:R>**: {name}", delete_after=5)
    
  @_ling.command(name="delete", aliases=["remove","close","rmv"])
  @blacklist_check()
  @ignore_check()
  async def _lingxd(self,ctx,msg_id):
    snap=await delete_timer(msg_id)
    if snap == "Land":
      return await ctx.send("Invalid reminder id.")
    await ctx.send("<a:cx_tick:1158669360223748106> | Successfully deleted reminder.")
  @commands.Cog.listener()
  async def on_timer_end(self, name, id, channel, expire, created, guild, author):
    chf = self.bot.get_channel(channel)
    embed = discord.Embed(
        title="**Reminder**",
        description=f">>> Message: {name}\nTime: <t:{int(created)}:R>", color=0x00FFCA)
    await chf.send(embed=embed, content=f"<@{author}>")
  