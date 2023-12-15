from __future__ import annotations
from discord.ext import commands
from utils.Tools import *
from discord import *
from utils.config import OWNER_IDS, No_Prefix
import json, discord
import typing
from utils import Paginator, DescriptionEmbedPaginator, FieldPagePaginator, TextPaginator
from utils import Paginator, DescriptionEmbedPaginator, FieldPagePaginator, TextPaginator

from typing import Optional

#Cyg90MAh7a0
class Owner(commands.Cog):

    def __init__(self, client):
        self.client = client





    @commands.command(name="slist")
    @commands.is_owner()
    async def _slist(self, ctx):
        hasanop = ([hasan for hasan in self.client.guilds])
        hasanop = sorted(hasanop,
                         key=lambda hasan: hasan.member_count,
                         reverse=True)
        entries = [
            f"`[{i}]` | [{g.name}](https://discord.com/channels/{g.id}) - {g.member_count}"
            for i, g in enumerate(hasanop, start=1)
        ]
        paginator = Paginator(source=DescriptionEmbedPaginator(
            entries=entries,
            description="",
            title=f"Server List of Chatoic - {len(self.client.guilds)}",
            color=0x2f3136,
            per_page=10),
                              ctx=ctx)
        await paginator.paginate()



    @commands.command(name="restart", help="Restarts the client.")
    @commands.is_owner()
    async def _restart(self, ctx: Context):
        await ctx.reply("Restarting! <a:cx_tick:1158669360223748106> Pls Wait It Takes 5-6 Second")
        restart_program()

    @commands.command(name="shutdown", help="Shutdown the client.")
    @commands.is_owner()
    async def _shutdown(self, ctx: Context):
        await ctx.bot.logout()

    @commands.command(name="sync", help="Syncs all database.")
    @commands.is_owner()
    async def _sync(self, ctx):
        await ctx.reply("Syncing...", mention_author=False)
        with open('anti.json', 'r') as f:
            data = json.load(f)
        for guild in self.client.guilds:
            if str(guild.id) not in data['guild']:
                data['guilds'][str(guild.id)] = 'on'
                with open('anti.json', 'w') as f:
                    json.dump(data, f, indent=4)
            else:
                pass
        with open('config.json', 'r') as f:
            data = json.load(f)
        for op in data["guilds"]:
            g = self.client.get_guild(int(op))
            if not g:
                data["guilds"].pop(str(op))
                with open('config.json', 'w') as f:
                    json.dump(data, f, indent=4)

    @commands.group(name="blacklist",
                    help="let's you add someone in blacklist",
                    aliases=["bl"])
    @commands.is_owner()
    async def blacklist(self, ctx):
        if ctx.invoked_subcommand is None:
            with open("blacklist.json") as file:
                blacklist = json.load(file)
                entries = [
                    f"`[{no}]` | <@!{mem}> (ID: {mem})"
                    for no, mem in enumerate(blacklist['ids'], start=1)
                ]
                paginator = Paginator(source=DescriptionEmbedPaginator(
                    entries=entries,
                    title=
                    f"List of Blacklisted users of Chatoic - {len(blacklist['ids'])}",
                    description="",
                    per_page=10,
                    color=0x00FFCA),
                                      ctx=ctx)
                await paginator.paginate()

    @blacklist.command(name="add")
    @commands.is_owner()
    async def blacklist_add(self, ctx: Context, member: discord.Member):
        try:
            with open('blacklist.json', 'r') as bl:
                blacklist = json.load(bl)
                if str(member.id) in blacklist["ids"]:
                    embed = discord.Embed(
                        title="Error!",
                        description=f"{member.name} is already blacklisted",
                        color=discord.Colour(0x00FFCA))
                    await ctx.reply(embed=embed, mention_author=False)
                else:
                    add_user_to_blacklist(member.id)
                    embed = discord.Embed(
                        title="Blacklisted",
                        description=f"Successfully Blacklisted {member.name}",
                        color=discord.Colour(0x00FFCA))
                    with open("blacklist.json") as file:
                        blacklist = json.load(file)
                        embed.set_footer(
                            text=
                            f"There are now {len(blacklist['ids'])} users in the blacklist"
                        )
                        await ctx.reply(embed=embed, mention_author=False)
        except:
            embed = discord.Embed(title="Error!",
                                  description=f"An Error Occurred",
                                  color=discord.Colour(0x00FFCA))
            await ctx.reply(embed=embed, mention_author=False)

    @blacklist.command(name="remove")
    @commands.is_owner()
    async def blacklist_remove(self, ctx, member: discord.Member = None):
        try:
            remove_user_from_blacklist(member.id)
            embed = discord.Embed(
                title="User removed from blacklist",
                description=
                f"<a:cx_tick:1158669360223748106> | **{member.name}** has been successfully removed from the blacklist",
                color=0x00FFCA)
            with open("blacklist.json") as file:
                blacklist = json.load(file)
                embed.set_footer(
                    text=
                    f"There are now {len(blacklist['ids'])} users in the blacklist"
                )
                await ctx.reply(embed=embed, mention_author=False)
        except:
            embed = discord.Embed(
                title="Error!",
                description=f"**{member.name}** is not in the blacklist.",
                color=0x00FFCA)
            embed.set_thumbnail(url=f"{self.client.user.display_avatar.url}")
            await ctx.reply(embed=embed, mention_author=False)


    @commands.group(name="bdg", help="Allows owner to add badges for a user")
    @commands.is_owner()
    async def _badge(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)

    @_badge.command(name="add",
                    aliases=["give"],
                    help="Add some badges to a user.")

    @commands.is_owner()
    async def badge_add(self, ctx, member: discord.Member, *, badge: str):
        ok = getbadges(member.id)
        if badge.lower() in ["dev", "developer", "devp"]:
            idk = "**<a:AllBadges:1164375079166165053>・DEVELOPER**"
            ok.append(idk)
            makebadges(member.id, ok)
            embed2 = discord.Embed(



                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Added `Developer` Badge To {member}**",
                color=0x50101)
            await ctx.reply(embed=embed2)
        elif badge.lower() in ["king", "owner"]:
            idk = "**<a:adi_God:1167065065950826577>・LORD**"
            ok.append(idk)
            makebadges(member.id, ok)
            embed8 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Added `OWNER` Badge To {member}**",
                color=0x50101)
            await ctx.reply(embed=embed8)
        elif badge.lower() in ["co", "coowner"]:
            idk = "**<a:cx_crown:1158669179059183687> Co Owner**"
            ok.append(idk)
            makebadges(member.id, ok)
            embed12 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Added `CO OWNER` Badge To {member}**",
                color=0x50101)
            await ctx.reply(embed=embed12)
        elif badge.lower() in ["admin", "ad"]:
            idk = "<:admin:1162651420772806766>** ・ADMIN**"
            ok.append(idk)
            makebadges(member.id, ok)
            embed20 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Added `ADMIN` Badge To {member}**",
                color=0x50101)
            await ctx.reply(embed=embed20)
        elif badge.lower() in ["mods", "moderator"]:
            idk = "**<:xD:1158411024903454872> ・MODERATOR**"
            ok.append(idk)
            makebadges(member.id, ok)
            embed15 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Added `MODERATOR` Badge To {member}**",
                color=0x50101)
            await ctx.reply(embed=embed15)





        elif badge.lower() in ["staff", "support staff"]:
            idk = "**<:staff:1162650110610657361> ・STAFF****"
            ok.append(idk)
            makebadges(member.id, ok)
            embed3 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Added `STAFF` Badge To {member}**",
                color=0x50101)
            await ctx.reply(embed=embed3)
        elif badge.lower() in ["partner"]:
            idk = "**<a:partner:1162650996770607124> ・PARTNER**"
            ok.append(idk)
            makebadges(member.id, ok)
            embed4 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Added `PARTNER` Badge To {member}**",
                color=0x50101)

            await ctx.reply(embed=embed4)
        elif badge.lower() in ["sponser", "sp"]:
            idk = "**<a:RH_red_diamond:1158410970985676901> ・SPONSER**"
            ok.append(idk)
            makebadges(member.id, ok)
            embed5 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Added `SPONSER` Badge To {member}**",
                color=0x50101)

            await ctx.reply(embed=embed5)
        elif badge.lower() in [
                "friend", "friends", "homies", "owner's friend"
        ]:
            idk = "**<:cx_Friend:1162651212936642650> ・FRIENDS**"
            ok.append(idk)
            makebadges(member.id, ok)
            embed1 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Added `FRIENDS` Badge To {member}**",
                color=0x50101)

            await ctx.reply(embed=embed1)
        elif badge.lower() in ["early", "supporter", "support"]:
            idk = "**<:early:1125036703288135721>・EARLY SUPPORTER**"
            ok.append(idk)
            makebadges(member.id, ok)
            embed6 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Added `SUPPORTER` Badge To {member}**",
                color=0x50101)

            await ctx.reply(embed=embed6)

        elif badge.lower() in ["vip"]:
            idk = "**<:Vip:1158411013180362772> ・VIP**"
            ok.append(idk)
            makebadges(member.id, ok)
            embed7 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Added `VIP` Badge To {member}**",
                color=0x50101)

            await ctx.reply(embed=embed7)

        elif badge.lower() in ["bug", "hunter", "bh"]:
            idk = "**<:bug_hunter:1162655647138074625> ・BUG HUNTER**"
            ok.append(idk)
            makebadges(member.id, ok)
            embed8 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Added `BUG HUNTER` Badge To {member}**",
                color=0x50101)

            await ctx.reply(embed=embed8)

        elif badge.lower() in ["hindu"]:
            idk = "**<:_nuke_jai_shree_ram:1162649984513097778> ・KATTAR HINDU**"
            ok.append(idk)
            makebadges(member.id, ok)
            embed9 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Added `KATTAR HINDU` Badge To {member}**",
                color=0x50101)

            await ctx.reply(embed=embed9)

        elif badge.lower() in ["all"]:
            idk = "<a:cx_crown:1158669179059183687> ・**CO OWNER**\n<:admin:1162651420772806766> ・**ADMIN**\n<:xD:1158411024903454872>** ・MODERATOR\n<:staff:1162650110610657361> ・STAFF**\n<a:partner:1162650996770607124> ・**PARTNER**\n**<a:RH_red_diamond:1158410970985676901> ・SPONSER**\n**<:cx_Friend:1162651212936642650>  ・FRIENDS**\n**<:EarlySupporter:1162649432584618004> ・EARLY SUPPORTER**\n**<:Vip:1158411013180362772> ・VIP**\n**<:bug_hunter:1162655647138074625> ・BUG HUNTER**\n**<:_nuke_jai_shree_ram:1162649984513097778> ・KATTAR HINDU**"
            ok.append(idk)
            makebadges(member.id, ok)
            embedall = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Added `All` Badges To {member}**",
                color=0x50101)

            await ctx.reply(embed=embedall)
        else:
            hacker = discord.Embed(
                                   description="**Invalid Badge**",
                                   color=0x50101)

            await ctx.reply(embed=hacker)

    @_badge.command(name="remove",
                    help="Remove badges from a user.",
                    aliases=["re"])
    @commands.is_owner()
    async def badge_remove(self, ctx, member: discord.Member, *, badge: str):
        ok = getbadges(member.id)
        if badge.lower() in ["dev", "developer", "devp"]:
            idk = "**<a:icons:1125039695261335644>・DEVELOPER**"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed2 = discord.Embed(



                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Removed `Developer` Badge To {member}**",
                color=0x50101)
            await ctx.reply(embed=embed2)
        elif badge.lower() in ["king", "owner"]:
            idk = "**<a:cx_heart:1148894569967128579> Developer**"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed8 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Removed `OWNER` Badge To {member}**",
                color=0x50101)
            await ctx.reply(embed=embed8)
        elif badge.lower() in ["co", "coowner"]:
            idk = "**<a:cx_crown:1158669179059183687> Co Owner**"
            ok.remove(idk)
            ok.remove(idk)
            makebadges(member.id, ok)
            embed12 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Removed `CO OWNER` Badge To {member}**",
                color=0x50101)
            await ctx.reply(embed=embed12)
        elif badge.lower() in ["admin", "ad"]:
            idk = "<:admin:1162651420772806766>** ・ADMIN**"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed20 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Removed `ADMIN` Badge To {member}**",
                color=0x50101)
            await ctx.reply(embed=embed20)
        elif badge.lower() in ["mods", "moderator"]:
            idk = "**<:automod:1101354580199084032>・MODERATOR**"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed15 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Removed `MODERATOR` Badge To {member}**",
                color=0x50101)
            await ctx.reply(embed=embed15)





        elif badge.lower() in ["staff", "support staff"]:
            idk = "**<:bff_Staff:1101761690401513522>・STAFF**"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed3 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Removed `STAFF` Badge To {member}**",
                color=0x50101)
            await ctx.reply(embed=embed3)
        elif badge.lower() in ["partner"]:
            idk = "**<:partner:1101762417681248336>・PARTNER**"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed4 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Removed `PARTNER` Badge To {member}**",
                color=0x50101)

            await ctx.reply(embed=embed4)
        elif badge.lower() in ["sponsor"]:
            idk = "**<a:sponsor:1101773574747992157>・SPONSER**"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed5 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Removed `SPONSER` Badge To {member}**",
                color=0x50101)

            await ctx.reply(embed=embed5)
        elif badge.lower() in [
                "friend", "friends", "homies", "owner's friend"
        ]:
            idk = "**<a:friends:1101772553623703565>・FRIENDS**"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed1 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Removed `FRIENDS` Badge To {member}**",
                color=0x50101)

            await ctx.reply(embed=embed1)
        elif badge.lower() in ["early", "supporter", "support"]:
            idk = "**<:EarlySupporter:1162649432584618004> ・EARLY SUPPORTER**"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed6 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Removed `SUPPORTER` Badge To {member}**",
                color=0x50101)

            await ctx.reply(embed=embed6)

        elif badge.lower() in ["vip"]:
            idk = "**<:VIP:1101772542227779625>・VIP**"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed7 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Removed `VIP` Badge To {member}**",
                color=0x50101)

            await ctx.reply(embed=embed7)

        elif badge.lower() in ["hindu"]:
            idk = "**<:jai_shree_ram:1123650351552282624>・KATTAR HINDU**"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed8 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Removed `KATTAR HINDU` Badge To {member}**",
                color=0x50101)

            await ctx.reply(embed=embed8) 

        elif badge.lower() in ["bug", "hunter"]:
            idk = "**<:bot_hunter:1101792120429355018>・BUG HUNTER**"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed9 = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Removed `BUG HUNTER` Badge To {member}**",
                color=0x50101)

            await ctx.reply(embed=embed9)
        elif badge.lower() in ["all"]:
            idk = "<a:cx_crown:1158669179059183687> ・CO OWNER\n<:admin:1162651420772806766> ・ADMIN\n<:xD:1158411024903454872> ・MODERATOR\n<:staff:1162650110610657361> ・STAFF\n<a:partner:1162650996770607124> ・PARTNER\n<a:RH_red_diamond:1158410970985676901> ・SPONSER\n<:cx_Friend:1162651212936642650>  ・FRIENDS\n<:EarlySupporter:1162649432584618004> ・EARLY SUPPORTER\n<:Vip:1158411013180362772> ・VIP\n<:bug_hunter:1162655647138074625> ・BUG HUNTER\n<:_nuke_jai_shree_ram:1162649984513097778> ・KATTAR HINDU**"
            ok.remove(idk)
            makebadges(member.id, ok)
            embedall = discord.Embed(

                description=
                f"<a:cx_tick:1158669360223748106> | **Successfully Removed `All` Badges To {member}**",
                color=0x50101)

            await ctx.reply(embed=embedall)
        else:
            hacker = discord.Embed(
                                   description="**Invalid Badge**",
                                   color=0x50101)

            await ctx.reply(embed=hacker)


    @commands.command()
    async def dm(self, ctx, user: discord.User, *, message: str):
        """ DM the user of your choice """
        try:
            await user.send(message)
            await ctx.send(f"<a:cx_tick:1158669360223748106> | Successfully Sent a DM to **{user}**")
        except discord.Forbidden:
            await ctx.send("This user might be having DMs blocked or it's a bot account...")           



    @commands.group()
    @commands.is_owner()
    async def change(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send_help(str(ctx.command))


    @change.command(name="nickname")
    @commands.is_owner()
    async def change_nickname(self, ctx, *, name: str = None):
        """ Change nickname. """
        try:
            await ctx.guild.me.edit(nick=name)
            if name:
                await ctx.send(f"<a:cx_tick:1158669360223748106> | Successfully changed nickname to **{name}**")
            else:
                await ctx.send("<a:cx_tick:1158669360223748106> | Successfully cleared nickname")
        except Exception as err:
            await ctx.send(err)



    @commands.command()
    @commands.is_owner()
    async def globalban(self, ctx, *, user: discord.User = None):
        if user is None:
            return await ctx.send(
                "You need to define the user"
            )
        for guild in self.client.guilds:
            for member in guild.members:
                if member == user:
                    await user.ban(reason="...")

@commands.command(help="Make the bot say something in a given channel.")
@commands.is_owner()
async def say(self, ctx: commands.Context, channel_id: int, *, message):
    channel = self.bot.get_channel(channel_id)
    guild = channel.guild
    target_channel = await ctx.message.author.create_dm()
    await ctx.send(f"Sending message to **{guild}** <#{channel.id}>\n> {message}")
    await target_channel.send(message)


