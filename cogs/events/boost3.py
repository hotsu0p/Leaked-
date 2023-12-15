
import os
import aiohttp
import discord
from discord.ext import commands
from core import Astroz, Cog
from utils.Tools import getDB1

headers = {"Authorization": f"Bot {os.environ.get('TOKEN')}"}

class Boost3(Cog):
    def __init__(self, bot: Astroz):
        self.bot = bot

    @Cog.listener()
    async def on_member_update(self, before, after):
        if not before.premium_since and after.premium_since:
            data = getDB1(after.guild.id)
            arh = data["boost1"]["role"]
            if arh == []:
                return
            else:
                if after.bot != True:
                    async with aiohttp.ClientSession(headers=headers, connector=None) as session:
                        for role in arh:
                            try:
                                async with session.put(f"https://discord.com/api/v10/guilds/{after.guild.id}/members/{after.id}/roles/{int(role)}", json={'reason': "CHAOTIC| Boost Role"}) as req:
                                    print(req.status)
                            except:
                                pass