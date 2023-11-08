from __future__ import annotations
from core import Astroz



#____________ Commands ___________

from .commands.starboard import Starboard 
#from .commands.embed import Embed
from .commands.zestar import Zestar
from .commands.Autorole import autorole
from .commands.Giveaways import giveaway
from .commands.giveaway_task import gwtask
from .commands.youtube import Youtube
from .commands.help import Help
from .commands.general import General
from .commands.music import Music
from .commands.moderation import Moderation
from .commands.vcroles import Voice
from .commands.anti import Security
from .commands.raidmode import Automod
from .commands.welcome import Welcomer
from .commands.fun import Fun
from .commands.games import Games
from .commands.extra import Utility
from .commands.owner import Owner
from .commands.role import Server
from .commands.ignore import Ignore
from .commands.vanityroles import Vanityroles
from .commands.List import list
from .commands.serverinfo import Info
from .commands.Afk import afk
from .commands.Verification import Verification
from .commands.Media import Media
from .commands.Logging import Logging
from .commands.owner1 import owner1
from .commands.Reminder import Reminder
from .commands.pfps import pfps
from .commands.joindm import joindm
from .commands.react import react
from .commands.about import About
from .commands.uptime import Uptime
from .commands.filter import MusicFilters
from .commands.nitro import Nitro
from .commands.boost import boost
from .commands.ticket import TicketCog

#____________ Events _____________


from .events.join import Join
from .events.antiban import antiban
from .events.antichannel import antichannel
from .events.antiguild import antiguild
from .events.antirole import antirole
from .events.antibot import antibot
from .events.antikick import antikick
from .events.antiprune import antiprune
from .events.antiwebhook import antiwebhook
from .events.antiping import antipinginv
from .events.antiemostick import antiemostick
from .events.antintegration import antintegration
from .events.antispam import AntiSpam
from .events.autoblacklist import AutoBlacklist
from .events.antiemojid import antiemojid
from .events.antiemojiu import antiemojiu
from .events.Errors import Errors
from .events.on_guild import Guild
from .events.greet2 import greet
from .events.voiceupdate import Vcroles2
from .events.boost2 import bst
from .events.boost3 import Boost3



##############select menu + button#############


from .commands.anti1 import anti1
from .commands.general1 import general1
from .commands.extra1 import extra1
from .commands.gw1 import gw1
from .commands.pfps1 import pfps1
from .commands.mod2 import mod1
from .commands.music1 import music1
from .commands.boost1 import velo1
from .commands.raidmode1 import raidmode1
from .commands.media1 import media1
from .commands.welcome1 import welcome1
from .commands.fun1 import fun1
from .commands.logging1 import logging1
from .commands.role1 import role1
from .commands.vanity1 import vanity1
from .commands.voice1 import voice1
from .commands.vcrole1 import vcrole1
from .commands.verification1 import ver1
from .commands.games1 import hacker1111111111
from .commands.ticket1 import hacker1111111111111111111
from .commands.joindm1 import joindm1
from .commands.owner2 import owner2


###############cmnd add################

async def setup(bot: Astroz):
  await bot.add_cog(Help(bot))
  await bot.add_cog(Starboard(bot))
  await bot.add_cog(autorole(bot))
  await bot.add_cog(General(bot))
  await bot.add_cog(Music(bot))
  await bot.add_cog(Moderation(bot))
  await bot.add_cog(Security(bot))
  await bot.add_cog(Automod(bot))
  await bot.add_cog(Welcomer(bot))
  await bot.add_cog(boost(bot))    
  await bot.add_cog(Fun(bot))
  await bot.add_cog(Games(bot))
  await bot.add_cog(Utility(bot))
  await bot.add_cog(Voice(bot))
  await bot.add_cog(Owner(bot))
  await bot.add_cog(Server(bot))
  await bot.add_cog(Vanityroles(bot))
  await bot.add_cog(Ignore(bot))
  await bot.add_cog(Verification(bot))
  await bot.add_cog(Media(bot))
  await bot.add_cog(Info(bot))
  await bot.add_cog(list(bot))
  await bot.add_cog(afk(bot))
  await bot.add_cog(Logging(bot))
  await bot.add_cog(owner1(bot))
  await bot.add_cog(Youtube(bot))
  await bot.add_cog(Reminder(bot))
  await bot.add_cog(giveaway(bot))
  await bot.add_cog(gwtask(bot))
  await bot.add_cog(pfps(bot))
  await bot.add_cog(joindm(bot))
  await bot.add_cog(Zestar(bot))
  await bot.add_cog(react(bot))
  await bot.add_cog(About(bot))
  await bot.add_cog(Uptime(bot))
  await bot.add_cog(MusicFilters(bot))
  await bot.add_cog(TicketCog(bot))
  await bot.add_cog(Nitro(bot))
  await bot.add_cog(bst(bot))
############select menu + button###############

  await bot.add_cog(anti1(bot))
  await bot.add_cog(general1(bot))  
  await bot.add_cog(extra1(bot))
  await bot.add_cog(gw1(bot))
  await bot.add_cog(pfps1(bot))
  await bot.add_cog(mod1(bot))
  await bot.add_cog(music1(bot))
  await bot.add_cog(velo1(bot))  
  await bot.add_cog(raidmode1(bot))
  await bot.add_cog(media1(bot))
  await bot.add_cog(welcome1(bot))
  await bot.add_cog(fun1(bot))
  await bot.add_cog(owner2(bot))
  await bot.add_cog(logging1(bot))
  await bot.add_cog(role1(bot))
  await bot.add_cog(hacker1111111111(bot))
 # await bot.add_cog(hacker1111111111(bot))await bot.add_cog(encryption1(bot))
  await bot.add_cog(vanity1(bot)) 
  await bot.add_cog(voice1(bot)) 
  await bot.add_cog(vcrole1(bot))
  await bot.add_cog(ver1(bot))
  await bot.add_cog(hacker1111111111111111111(bot))
  await bot.add_cog(joindm1(bot))


    
###########################events################3
  
  await bot.add_cog(antiban(bot))
  await bot.add_cog(antichannel(bot))
  await bot.add_cog(antiguild(bot))
  await bot.add_cog(antirole(bot))
  await bot.add_cog(antibot(bot))
  await bot.add_cog(antikick(bot))
  await bot.add_cog(antiprune(bot))
  await bot.add_cog(antiwebhook(bot))
  await bot.add_cog(antipinginv(bot))
  await bot.add_cog(antiemostick(bot))
  await bot.add_cog(antintegration(bot))  
  await bot.add_cog(AntiSpam(bot))
  await bot.add_cog(AutoBlacklist(bot))
  await bot.add_cog(antiemojid(bot))
  await bot.add_cog(antiemojiu(bot))
  await bot.add_cog(Guild(bot))
  await bot.add_cog(Errors(bot))
  await bot.add_cog(greet(bot))
  await bot.add_cog(Join(bot))
  await bot.add_cog(Vcroles2(bot))
  await bot.add_cog(Boost3(bot))



 
