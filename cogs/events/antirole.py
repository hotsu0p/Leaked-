import os
import discord
from discord.ext import commands
import requests
import sys
import setuptools
from itertools import cycle
import threading
import datetime
import logging
import time
import asyncio
from core import Astroz, Cog
import aiohttp
import tasksio
from discord.ext import tasks
import random
from utils.Tools import *

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

class antirole(Cog):
    def __init__(self, client: Astroz):
        self.client = client      
        self.headers = {"Authorization": f"Bot MTAxMjYyNzA4ODIzMjE2NTM3Ng.G6fWNZ.oyQgaKEVU8T_zZ0Vk_Zj95QHQ4hVwqCgbBOFK4"}
        self.processing = [
            
        ]

    @tasks.loop(seconds=15)
    async def clean_processing(self):
        self.processing.clear()

    @commands.Cog.listener()
    async def on_ready(self):
        await self.clean_processing.start()

        
    @commands.Cog.listener()
    async def on_guild_role_create(self, role) -> None:
        try:
          anti = getanti(role.guild.id)
          data = getConfig(role.guild.id)
          punishment = data["punishment"]
          wled = data["whitelisted"]
          wlrole = data['wlrole']  
          guild = role.guild
          wlroles = guild.get_role(wlrole)
          reason = "Creating Roles | Not Whitelisted"
          async for entry in guild.audit_logs(
                limit=2,
                after=datetime.datetime.utcnow() - datetime.timedelta(seconds=30)):
            user = entry.user.id
            hacker = guild.get_member(entry.user.id)
          api = random.randint(8,9)
          if entry.user.id == self.client.user.id or entry.user.id == guild.owner_id or str(entry.user.id) in wled or anti == "off" or wlroles in hacker.roles:
            return
          else:
           if entry.action == discord.AuditLogAction.role_create:
             async with aiohttp.ClientSession(headers=self.headers) as session:
              if punishment == "ban":
                  async with session.put(f"https://discord.com/api/v{api}/guilds/%s/bans/%s" % (guild.id, user), json={"reason": reason}) as r:
                    if r.status in (200, 201, 204):
                      await role.delete()
                      logging.info("Successfully banned %s" % (user))
              elif punishment == "kick":
                         async with session.delete(f"https://discord.com/api/v{api}/guilds/%s/members/%s" % (guild.id, user), json={"reason": reason}) as r2:
                             if r2.status in (200, 201, 204):
                               await role.delete()
                               logging.info("Successfully kicked %s" % (user))
              elif punishment == "none":
                mem = guild.get_member(entry.user.id)
                await mem.edit(roles=[role for role in mem.roles if not role.permissions.administrator], reason=reason)
                await role.delete()
              else:
                      return
        except Exception as error:
            if isinstance(error, discord.Forbidden):
              return

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role) -> None:
        try:
          anti = getanti(role.guild.id)
          data = getConfig(role.guild.id)
          punishment = data["punishment"]
          wled = data["whitelisted"]
          wlrole = data['wlrole']
          guild = role.guild
          hacker = guild.get_member(entry.user.id)
          wlroles = guild.get_role(wlrole)
          reason = "Deleting Roles | Not Whitelisted"
          async for entry in guild.audit_logs(
                limit=2,
                after=datetime.datetime.utcnow() - datetime.timedelta(seconds=30)):
            user = entry.user.id
          api = random.randint(8,9)
          if entry.user.id == self.client.user.id or entry.user.id == guild.owner_id or str(entry.user.id) in wled or anti == "off" or wlroles in hacker.roles:
            return          
          else:
            if entry.action == discord.AuditLogAction.role_delete:
              async with aiohttp.ClientSession(headers=self.headers) as session:
                if punishment == "ban":
                  async with session.put(f"https://discord.com/api/v{api}/guilds/%s/bans/%s" % (guild.id, user), json={"reason": reason}) as r:
                    if role.is_bot_managed() or role.is_integration():
                      return
                    else:
                      okay = await guild.create_role(reason=reason, name=f"{role}", permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable, colour=role.colour)
                      await okay.edit(position=int(role.position))
                    if r.status in (200, 201, 204):
                      logging.info("Successfully banned %s" % (user))
                elif punishment == "kick":
                         async with session.delete(f"https://discord.com/api/v{api}/guilds/%s/members/%s" % (guild.id, user), json={"reason": reason}) as r2:
                             if role.is_bot_managed() or role.is_integration():
                               return
                             else:
                               otau = await guild.create_role(reason=reason, name=f"{role}", permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable, colour=role.colour)
                               await otau.edit(position=int(role.position))
                             if r2.status in (200, 201, 204):
                          
                               logging.info("Successfully kicked %s" % (user))
                elif punishment == "none":
                  mem = guild.get_member(entry.user.id)
                  await mem.edit(roles=[role for role in mem.roles if not role.permissions.administrator], reason=reason)
                  if role.is_bot_managed() or  role.is_integration():
                    return
                  else:
                    otay = await guild.create_role(reason=reason, name=f"{role}", permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable, colour=role.colour)
                    await otay.edit(position=int(role.position))
                else:
                       return
        except Exception as error:
            if isinstance(error, discord.Forbidden):
              return
    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after) -> None:
      try:
        data = getConfig(before.guild.id)
        anti = getanti(before.guild.id)
        punishment = data["punishment"]
        wled = data["whitelisted"]
        wlrole = data['wlrole']
        guild = after.guild
        hacker = guild.get_member(entry.user.id)
        wlroles = guild.get_role(wlrole)
        reason = "Updating Roles | Not Whitelisted"
        async for entry in guild.audit_logs(
                limit=1):
          user = entry.user.id
        api = random.randint(8,9)
        if entry.user.id == self.client.user.id or entry.user.id == guild.owner_id or str(entry.user.id) in wled or anti == "off" or wlroles in hacker.roles: 
            return                  
        else:
         if entry.action == discord.AuditLogAction.role_update:
          async with aiohttp.ClientSession(headers=self.headers) as session:
              if punishment == "ban":
                  await after.edit(name=f"{before.name}", permissions=before.permissions, reason=reason, colour=before.colour, hoist=before.hoist, mentionable=before.mentionable)
                  async with session.put(f"https://discord.com/api/v{api}/guilds/%s/bans/%s" % (guild.id, user), json={"reason": reason}) as r:
                    if r.status in (200, 201, 204):
                      logging.info("Successfully banned %s" % (user))
              elif punishment == "kick":
                         async with session.delete(f"https://discord.com/api/v{api}/guilds/%s/members/%s" % (guild.id, user), json={"reason": reason}) as r2:
                             if r2.status in (200, 201, 204):
                               await after.edit(name=f"{before.name}", permissions=before.permissions, reason=reason, colour=before.colour, hoist=before.hoist, mentionable=before.mentionable)
                               logging.info("Successfully kicked %s" % (user))
              elif punishment == "none":
                mem = guild.get_member(entry.user.id)
                await mem.edit(roles=[role for role in mem.roles if not role.permissions.administrator], reason=reason)
                await after.edit(name=f"{before.name}", permissions=before.permissions, reason=reason, colour=before.colour, hoist=before.hoist, mentionable=before.mentionable)
              else:
                       return
      except Exception as error:
            if isinstance(error, discord.Forbidden):
              return