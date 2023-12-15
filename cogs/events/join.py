import os
import discord
import aiohttp
from discord.ext import commands, tasks
from discord.colour import Color
import json
import random
from discord.ui import Button, View
#from utils.checks import getConfig, updateConfig



class Join(commands.Cog):
    def __init__(self, client):
        self.client = client

    

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
         # data = getConfig(guild.id)
          #key = "".join(random.choice("aAbBcCdDeE1234567890nNmMkKiIuUyY") for _ in range(6))
         # data['backupkey'] = key
          #updateConfig(guild.id, data)
          embed = discord.Embed(
            description="Thank you for adding me to your server!\n・ My default prefix is `$`\n・ You can use the `$help` command to get list of commands\n・ Our [Support Server](https://discord.gg/jj25BZgrFb) or our team offers detailed information & guides for commands\n・ Feel free to join our [Support Server](https://discord.gg/jj25BZgrFb) if you need help/support for anything related to the bot",
            color=0x0d0d13
          )
          skidgod = Button(label='Support Server', style=discord.ButtonStyle.link, url='https://discord.gg/jj25BZgrFb')
          #web = Button(label='Website', style=discord.ButtonStyle.link, url='https://discord.gg/3YmDAzbuRR')
          docs = Button(label='Invite Me',style=discord.ButtonStyle.link,url='https://discord.com/api/oauth2/authorize?client_id=1170735115891126302&permissions=8&scope=bot%20applications.commands')

          docs1 = Button(label='Vote Me',style=discord.ButtonStyle.link,url='https://discord.gg/jj25BZgrFb')
       # premium = Button(label='Premium',style=discord.ButtonStyle.link,url='https://discord.gg/3YmDAzbuRR')
       # vote = Button(label='Vote Me', style=discord.ButtonStyle.link, url='https://discord.com/oauth2/authorize?client_id=1021416292185546854&permissions=2113268958&scope=bot')
          view = View()
         # view.add_item(b)
          view.add_item(skidgod) 
          #view.add_item(web)
          view.add_item(docs)
          view.add_item(docs1)
          embed.set_author(name=f"{guild.name}",
                             icon_url=guild.icon.url)
          embed.set_thumbnail(url=guild.owner.avatar.url)
          await guild.owner.send(embed=embed,view=view)