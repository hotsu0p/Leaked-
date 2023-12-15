import discord
from traceback import format_exception
from discord.ext import commands
from difflib import get_close_matches
import io
import textwrap
import datetime
import sys
from contextlib import suppress
from core import Context
from core.Astroz import Astroz
from core.Cog import Cog
from utils.Tools import getConfig
from itertools import chain
import psutil
import time
import datetime
import platform
import os
import logging
import motor.motor_asyncio
from pymongo import MongoClient
import requests
import motor.motor_asyncio as mongodb
from typing import *
from utils import *
import json
from utils import help as vhelp
from utils import Paginator, DescriptionEmbedPaginator, FieldPagePaginator, TextPaginator

from core import Cog, Astroz, Context
from typing import Optional
from discord import app_commands
start_time = time.time()
client = Astroz()


def datetime_to_seconds(thing: datetime.datetime):
    current_time = datetime.datetime.fromtimestamp(time.time())
    return round(
        round(time.time()) +
        (current_time - thing.replace(tzinfo=None)).total_seconds())

client = Astroz()



class HelpCommand(commands.HelpCommand):

  async def on_help_command_error(self, ctx, error):
    serverCount = len(self.client.guilds)
    users = sum(g.member_count for g in self.client.guilds
                    if g.member_count != None)

    total_members = sum(g.member_count for g in self.client.guilds
                            if g.member_count != None)
    Chatoic = [
      commands.CommandOnCooldown, commands.CommandNotFound,
      discord.HTTPException, commands.CommandInvokeError
    ]
    if not type(error) in Chatoic:
      await self.context.reply(f"Unknown Error Occurred\n{error.original}",
                               mention_author=False)
    else:
      if type(error) == commands.CommandOnCooldown:
        return

        return await super().on_help_command_error(ctx, error)

  async def command_not_found(self, string: str) -> None:
    with open('blacklist.json', 'r') as f:
      data = json.load(f)
    if str(self.context.author.id) in data["ids"]:
      embed = discord.Embed(
        title="<:blacklist:1158791166867812495> Blacklisted",
        description=
        "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/jj25BZgrFb)",
        color=0x00FFCA)
      await self.context.reply(embed=embed, mention_author=False)
    else:

      if string in ("security", "anti", "antinuke"):
        cog = self.context.bot.get_cog("Antinuke")
        with suppress(discord.HTTPException):
          await self.send_cog_help(cog)
      else:
        msg = f"Command `{string}` is not found...\n"
        piyush = await self.context.bot.fetch_user(926831289649201213)
        cmds = (str(cmd) for cmd in self.context.bot.walk_commands())
        mtchs = get_close_matches(string, cmds)
        if mtchs:
          for okaay, okay in enumerate(mtchs, start=1):
            msg += f"Did You Mean: \n`[{okaay}]`. `{okay}`\n"
        embed1 = discord.Embed(
          color=0x11100d,
          title=f"Command `{string}` is not found...\n",
          description=f"Did You Mean: \n`[{okaay}]`. `{okay}`\n")

        return None

  async def send_bot_help(self, mapping):
    await self.context.typing()
    with open('ignore.json', 'r') as heck:
      randi = json.load(heck)
    with open('blacklist.json', 'r') as f:
      bled = json.load(f)
    if str(self.context.author.id) in bled["ids"]:
      embed = discord.Embed(
        title="<:blacklist:1158791166867812495> Blacklisted",
        description=
        "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/jj25BZgrFb)",
        color=0x11100d)
      return await self.context.reply(embed=embed, mention_author=False)
    elif str(self.context.channel.id) in randi["ids"]:
      return None
    data = getConfig(self.context.guild.id)
    prefix = data["prefix"]
    
    
    filtered = await self.filter_commands(self.context.bot.walk_commands(),sort=True)

    loading_message = await self.context.reply(embed=discord.Embed(color=0x2f3136,description="<a:Loading:1169275720116215901> **Loading Help command...**"))
    await asyncio.sleep(7)
    
    embed = discord.Embed(
      title="**Help Command Overview **:",
      description=
      f"**•  My defult Prefix is `{prefix}`\n •  Total Commands: {len(set(self.context.bot.walk_commands()))} | Usable by you (here): {len(set(filtered))}\n •  Links ~ [Invite](https://discord.com/api/oauth2/authorize?client_id=1170735115891126302&permissions=8&scope=bot) | [Support](https://discord.gg/jj25BZgrFb) \n• Type `{prefix}help <command | module>` for more info.**\n```    <> - Required | [] - Optional``` ",
      color= 0x41eeee)
    embed.set_thumbnail(url=self.context.bot.user.display_avatar.url)

    embed.set_footer(
      text="Made by the Hotsuop dev services💖",
      icon_url="https://cdn.discordapp.com/avatars/1170735115891126302/dc3e50807325ea566a4b814aab69d56c.png?size=1024")

    embed.add_field(name="**__Main Modules __**",
                    value="""
<:invisible:1158410927318773800><:xD:1158411024903454872> Antinuke\n <:invisible:1158410927318773800><a:tadaaa:1162353626593894460> Giveaway\n <:invisible:1158410927318773800><a:Musicz:1158410945744355439> Music\n <:invisible:1158410927318773800><:CommandsList:1158410923455819816> Logging\n <:invisible:1158410927318773800><:nexus_mod:1158410954229432410> Moderation\n <:invisible:1158410927318773800><a:moon:1158411057325428756>  Extra\n <:invisible:1158410927318773800><a:boost:1158411048190218291> Boost <:0_:1170733166999392317><:1_:1170733169344004156> \n <:invisible:1158410927318773800><a:messages:1158411054741725245> Message\n<:invisible:1158410927318773800><:nexus_Ticket:1158721875925549097> Ticket <:0_:1170733166999392317><:1_:1170733169344004156>\n<:invisible:1158410927318773800><a:Games:1169154665703817247> Games <:0_:1170733166999392317><:1_:1170733169344004156>s""",
                    inline=True)  

    embed.add_field(name="**__Basics Modules __**",
                    value="""<:invisible:1158410927318773800><a:_welcome_:1158720639268565003> Welcome\n <:invisible:1158410927318773800><a:sword:1158410994968699002> Raidmode\n <:invisible:1158410927318773800><a:planetz:1158410965780529202> Join Dm\n <:invisible:1158410927318773800><a:server:1158410977591709757> Server\n <:invisible:1158410927318773800><a:troll:1158410959338082374> Fun\n <:invisible:1158410927318773800><a:verify:1158411009036398624> Verification\n <:invisible:1158410927318773800><a:general:1158411852892602408> General\n <:invisible:1158410927318773800> <a:AG_SocialMedia:1158411040766308482> Media \n <:invisible:1158410927318773800><a:awful_pfp:1169154160017539083> Pfp \n <:invisible:1158410927318773800> <a:voicegoogle:1158411017324335135> Voice \n <:invisible:1158410927318773800> <:merox_vcroles:1158734018813108265> VcRoles\n <:invisible:1158410927318773800><:vanity:1158410999750213632> Vanity roles""",
                    inline=True) 
    #embed.add_field(
        #name="__Stats__",
        #value=f"""・**Ping** - {int(self.bot.latency * 1000)} ms """,
        #inline=False
   # )
    embed.set_author(name=self.context.author.name,
                     icon_url=self.context.author.display_avatar.url)
    embed.set_image(url="https://cdn.discordapp.com/attachments/1157042944637931582/1171838050972729474/city-lofi.mp4?ex=655e223b&is=654bad3b&hm=82b2b20a1b8b0fe44aa25214d8fa08860f2fc0390caf41caab6be1d16f7e6ec2&")
    embed.timestamp = discord.utils.utcnow()

    # Create the invite button
    invite_button = discord.ui.Button(
        style=discord.ButtonStyle.link,
   #     emoji='<a:985:1151531674207789189>',
        label="Invite Me",
        url="https://discord.com/api/oauth2/authorize?client_id=1170735115891126302&permissions=8&scope=bot"
    )
    support_button = discord.ui.Button(
        style=discord.ButtonStyle.link,
   #     emoji='<a:999:1151531721381134377>',
        label="Support Server",
      url="https://discord.gg/jj25BZgrFb"
    )
    Vote_button = discord.ui.Button(
        style=discord.ButtonStyle.link,
   #     emoji='<a:982:1142461636389650542>',
        label="Vote Me",
      url="https://discord.gg/jj25BZgrFb"
    )    

    view = vhelp.View(mapping=mapping, ctx=self.context, homeembed=embed, ui=2)
    view.add_item(invite_button)
    view.add_item(support_button)
   # view.add_item(Vote_button)    
    await loading_message.delete()
    await self.context.send(embed=embed, mention_author=False, view=view)

  async def send_command_help(self, command):
    with open('ignore.json', 'r') as heck:
      randi = json.load(heck)
    with open('blacklist.json', 'r') as f:
      data = json.load(f)
    if str(self.context.author.id) in data["ids"]:
      embed = discord.Embed(
        title="<:blacklist:1158791166867812495> Blacklisted",
        description=
        "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/jj25BZgrFb)",
        color=0x00FFCA)
      await self.context.reply(embed=embed, mention_author=False)
    elif str(self.context.channel.id) in randi["ids"]:
      return None
    else:
      hacker = f">>> {command.help}" if command.help else '>>> No Help Provided...'
      embed = discord.Embed(
        description=
        f"""```yaml\n- [] = optional argument\n- <> = required argument\n- Do NOT Type These When Using Commands !```\n{hacker}""",
        color=0x00FFCA)
      alias = ' | '.join(command.aliases)

      embed.add_field(name="**Aliases**",
                      value=f"{alias}" if command.aliases else "No Aliases",
                      inline=False)
      embed.add_field(name="**Usage**",
                      value=f"`{self.context.prefix}{command.signature}`\n")
      embed.set_author(name=f"{command.cog.qualified_name.title()}",
                       icon_url=self.context.bot.user.display_avatar.url)
      await self.context.reply(embed=embed, mention_author=False)

  def get_command_signature(self, command: commands.Command) -> str:
    parent = command.full_parent_name
    if len(command.aliases) > 0:
      aliases = ' | '.join(command.aliases)
      fmt = f'[{command.name} | {aliases}]'
      if parent:
        fmt = f'{parent}'
      alias = f'[{command.name} | {aliases}]'
    else:
      alias = command.name if not parent else f'{parent} {command.name}'
    return f'{alias} {command.signature}'

  def common_command_formatting(self, embed_like, command):
    embed_like.title = self.get_command_signature(command)
    if command.description:
      embed_like.description = f'{command.description}\n\n{command.help}'
    else:
      embed_like.description = command.help or 'No help found...'

  async def send_group_help(self, group):
    with open('blacklist.json', 'r') as f:
      idk = json.load(f)
    with open('ignore.json', 'r') as heck:
      randi = json.load(heck)
    if str(self.context.author.id) in idk["ids"]:
      embed = discord.Embed(
        title="<:blacklist:1158791166867812495> Blacklisted",
        description=
        "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/jj25BZgrFb)",
        color=0x00FFCA)
      await self.context.reply(embed=embed, mention_author=False)
    elif str(self.context.channel.id) in randi["ids"]:
      return None
    else:
      entries = [(
        f"`{self.context.prefix}{cmd.qualified_name}`",
        f"{cmd.short_doc if cmd.short_doc else 'No Description Provided...'}\n\n"
      ) for cmd in group.commands]
    paginator = Paginator(source=FieldPagePaginator(
      entries=entries,
      title=f"{group.qualified_name} Commands",
      description="```yaml\n- [] = optional argument\n- <> = required argument\n- Do NOT Type These When Using Commands !```",
      color=0x00FFCA,
      per_page=10),
                          ctx=self.context)
    await paginator.paginate()

  async def send_cog_help(self, cog):
    with open('blacklist.json', 'r') as f:
      data = json.load(f)
    with open('ignore.json', 'r') as heck:
      randi = json.load(heck)
    if str(self.context.author.id) in data["ids"]:
      embed = discord.Embed(
        title="<:blacklist:1158791166867812495> Blacklisted",
        description=
        "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/jj25BZgrFb)",
        color=0x00FFCA)
      return await self.context.reply(embed=embed, mention_author=False)
    elif str(self.context.channel.id) in randi["ids"]:
      return None
    #await self.context.typing()
    entries = [(
      f"`{self.context.prefix}{cmd.qualified_name}`",
      f"{cmd.short_doc if cmd.short_doc else 'No Description Provided...'}\n\n"
    ) for cmd in cog.get_commands()]
    paginator = Paginator(source=FieldPagePaginator(
      entries=entries,
      title=f"{cog.qualified_name.title()} ({len(cog.get_commands())})",
      description="```yaml\n- [] = optional argument\n- <> = required argument\n- Do NOT Type These When Using Commands !```\n\n",
      color=0x00FFCA,
      per_page=10),
                          ctx=self.context)
    await paginator.paginate()


class Help(Cog, name="help"):

  def __init__(self, client: Astroz):
    self._original_help_command = client.help_command
    attributes = {
      'name':
      "help",
      'aliases': ['h'],
      'cooldown':
      commands.CooldownMapping.from_cooldown(1, 5, commands.BucketType.user),
      'help':
      'Shows help about bot, a command or a category'
    }
    client.help_command = HelpCommand(command_attrs=attributes)
    client.help_command.cog = self

  async def cog_unload(self):
    self.help_command = self._original_help_command