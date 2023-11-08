
import discord
from discord.ext import commands
from core import Cog, Astroz, Context
from utils.Tools import *
from typing import *


class bst(Cog):
    def __init__(self, bot: Astroz):
        self.bot = bot

    @Cog.listener()
    async def on_member_update(self, before, after):
        if not before.premium_since and after.premium_since:
            data = getDB1(after.guild.id)
            msg = data["boost"]["message"]
            chan = list(data["boost"]["channel"])
            emtog = data["boost"]["embed"]
            emping = data["boost"]["ping"]
            emimage = data["boost"]["image"]
            emthumbnail = data["boost"]["thumbnail"]
            emautodel = data["boost"]["autodel"]
            user = after

            if chan == []:
                return
            else:
                if "<<boost.server_name>>" in msg:
                    msg = msg.replace("<<boost.server_name>>", "%s" % (user.guild.name))
                if "<<server.boost_count>>" in msg:
                    msg = msg.replace("<<server.boost_count>>", "%s" % (user.guild.premium_subscription_count))
                if "<<boost.user_name>>" in msg:
                    msg = msg.replace("<<boost.user_name>>", "%s" % (user))
                if "<<boost.user_mention>>" in msg:
                    msg = msg.replace("<<boost.user_mention>>", "%s" % (user.mention))
                if "<<user.boosted_at>>" in msg:
                    msg = msg.replace("<<user.boosted_at>>", f"<t:{int(user.premium_since.timestamp())}:F>")
                if msg == "":
                    msg = ""
                else:
                    msg = msg
                if emping == True:
                    emping = f"{user.mention}"
                else:
                    emping = ""
                if emautodel == 0:
                    emautodel = None
                else:
                    emautodel = emautodel
                em = discord.Embed(description=msg, color=0x2f3136)
                em.set_author(name=user, icon_url=after.avatar.url if after.avatar else after.default_avatar.url)
                em.timestamp = discord.utils.utcnow()
                if emimage == "":
                    em.set_image(url=None)
                else:
                    em.set_image(url=emimage)
                if emthumbnail == "":
                    em.set_thumbnail(url=None)
                else:
                    em.set_thumbnail(url=emthumbnail)
                if user.guild.icon is not None:
                    em.set_footer(text=user.guild.name, icon_url=user.guild.icon.url)
                if emtog == True:
                    for chh in chan:
                        ch = self.bot.get_channel(int(chh))
                        await ch.send(emping, embed=em)
                else:
                    for chh in chan:
                        ch = self.bot.get_channel(int(chh))
                        if emtog == False:
                            await ch.send(msg)