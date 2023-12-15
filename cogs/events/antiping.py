import os
import discord
from discord.ext import commands
import requests
import sys
from utils.Tools import getConfig, add_user_to_blacklist, getanti
import setuptools
from itertools import cycle
from collections import Counter
import threading
import datetime
import logging
from core import Astroz, Cog
import time
import asyncio
import aiohttp
import tasksio
from discord.ui import View, Button
import json
from discord.ext import tasks
import random

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

class antipinginv(Cog):
    def __init__(self, client: Astroz):
        self.client = client
        self.spam_control = commands.CooldownMapping.from_cooldown(10, 12.0, commands.BucketType.user)


        

    @commands.Cog.listener()
    async def on_message(self, message):
      button = Button(label="Invite Me", url =  "https://discord.com/api/oauth2/authorize?client_id=1170735115891126302&permissions=8&scope=bot")
      button1 = Button(label="Support Server", url = "https://discord.gg/jj25BZgrFb")
      button2 = Button(label="Vote Me", url = "https://discord.gg/jj25BZgrFb")
      try:
       
        with open("blacklist.json", "r") as f:
          data2 = json.load(f)
        with open('ignore.json', 'r') as heck:
          randi = json.load(heck)
          astroz = '<@1170735115891126302>'
          try:
            data = getConfig(message.guild.id)
            anti = getanti(message.guild.id)
            prefix = data["prefix"]
            wled = data["whitelisted"]
            punishment = data["punishment"]
            wlrole = data['wlrole']
            guild = message.guild
            hacker = guild.get_member(message.author.id)
            wlroles = guild.get_role(wlrole)
          except Exception:
            pass
          guild = message.guild
          if message.mention_everyone:
            if str(message.author.id) in wled or anti == "off" or wlroles in hacker.roles:
              pass
            else:
              if punishment == "ban":
                await message.guild.ban(message.author, reason="Mentioning Everyone | Not Whitelisted")
              elif punishment == "kick":
                await message.guild.kick(message.author, reason="Mentioning Everyone | Not Whitelisted")
              elif punishment == "none":
                return


          elif message.content == astroz or message.content == "<@1170735115891126302>":
            if str(message.author.id) in data2["ids"]:
              embed = discord.Embed(title="<:bruh:1159400698354606141> Blacklisted", description="You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can't Appeal In Our Support Server By Clicking [here](https://discord.gg/jj25BZgrFb)")
              await message.reply(embed=embed, mention_author=False)
            if str(message.channel.id) in randi["ids"]:
                await message.reply(f"My all commands are disabled for {message.channel.mention}",mention_author=True, delete_after=10)
                
                
            
          else:
            return
      except Exception as error:
        if isinstance(error, discord.Forbidden):
              return






