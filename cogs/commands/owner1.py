from __future__ import annotations
from discord.ext import commands
from core import Cog, Astroz, Context
from utils.Tools import *
import json, discord
import reactionmenu
from reactionmenu import ViewMenu, ViewButton
from discord import *
from utils.config import OWNER_IDS, No_Prefix
import typing
from utils import Paginator, DescriptionEmbedPaginator, FieldPagePaginator, TextPaginator
from typing import Optional



class PaginationViewWallah:
  def __init__(self, embed_list, ctx):
    self.elist = embed_list
    self.context = ctx

  def disable_button(self, menu):
    tax = str(menu.message.embeds[0].footer.text).replace(" ", "").replace("Page", "")
    num = int(tax[0])
    if num == 1:
      fis=menu.get_button("2", search_by="id")
      bax = menu.get_button("1", search_by="id")
      
      

  def enable_button(self, menu):
    tax = str(menu.message.embeds[0].footer.text).replace(" ", "").replace("Page", "")
    num = int(tax[0])
    if num != 1:
      fis=menu.get_button("2", search_by="id")
      bax = menu.get_button("1", search_by="id")
      print(bax)
      
    
  async def dis_button(self, menu):
    self.disable_button(menu)

  async def ene_button(self, menu):
    self.ene_button(menu)


  
  async def start(self, ctx, disxd=False):
    style = f"{ctx.bot.user.name} • Page $/&"
    menu = ViewMenu(ctx, menu_type=ViewMenu.TypeEmbed, style=style)
    for xem in self.elist:
      menu.add_page(xem)
    lax = ViewButton(style=discord.ButtonStyle.primary, label='≪',emoji=None, custom_id=ViewButton.ID_GO_TO_FIRST_PAGE)
    menu.add_button(lax)
    bax = ViewButton(style=discord.ButtonStyle.green, label='Back',emoji=None, custom_id=ViewButton.ID_PREVIOUS_PAGE)
    menu.add_button(bax)
    bax2 = ViewButton(style=discord.ButtonStyle.danger, label=None,emoji='<a:no:1158411070608769034>', custom_id=ViewButton.ID_END_SESSION)
    menu.add_button(bax2)
    bax3 = ViewButton(style=discord.ButtonStyle.green, label='Next',emoji=None, custom_id=ViewButton.ID_NEXT_PAGE)
    menu.add_button(bax3)
    sax = ViewButton(style=discord.ButtonStyle.primary, label='≫',emoji=None, custom_id=ViewButton.ID_GO_TO_LAST_PAGE)
    menu.add_button(sax)
    if disxd:
      menu.disable_all_buttons()
    menu.disable_button(lax)
    menu.disable_button(bax)
    async def all_in_one_xd(payload):
      
      newmsg = await ctx.channel.fetch_message(menu.message.id)
      tax = str(newmsg.embeds[0].footer.text).replace(f"{ctx.bot.user.name}","").replace(" ", "").replace("Page", "").replace("•","")
      saxl = tax.split("/")
      num = int(saxl[0])
      numw = int(saxl[1])
      if num == 1:
        menu.disable_button(lax)
        menu.disable_button(bax)
      else:
        menu.enable_button(lax)
        menu.enable_button(bax)
      if num == numw:
        menu.disable_button(bax3)
        menu.disable_button(sax)
      else:
        menu.enable_button(bax3)
        menu.enable_button(sax)
      await menu.refresh_menu_items()
    menu.set_relay(all_in_one_xd)
    await menu.start()

async def working_lister(ctx, color, listxd, *, title):
  embed_array = []
  t = title
  clr = color
  sent = []
  your_list = listxd
  count = 0
  idkh=True
  embed = discord.Embed(color=clr, description="", title=t)
  embed.set_footer(icon_url=ctx.bot.user.avatar)
  if idkh:
    for i in range(len(listxd)):
      for i__ in range(10):
        if not your_list[i].id in sent:
          count+=1
          if str(count).endswith("0") or len(str(count)) != 1:
            actualcount = str(count)
          else:
            actualcount = f"0{count}"
          embed.description+=f"`[{actualcount}]` | {your_list[i]} [<@{your_list[i].id}>]\n"
          sent.append(your_list[i].id)
      if str(count).endswith("0") or str(count) == str(len(your_list)):
        embed_array.append(embed)
        embed = discord.Embed(color=clr, description="", title=t)
        embed.set_footer(icon_url=ctx.bot.user.avatar)
  
  if len(embed_array) == 0:
    embed_array.append(embed)
  pag = PaginationViewWallah(embed_array, ctx)
  if len(embed_array) == 1:
    await pag.start(ctx, True)
  else:
    await pag.start(ctx)


class owner1(Cog):
  """Shows a list of commands available for my owners"""
  def __init__(self, client: Astroz):
    self.client = client
    self.owner_ids = [1036877996243562516,1036877996243562516]

  @commands.hybrid_group(name="np")
  async def _np(self, ctx: Context):
      print("No Prefix Command")

  @_np.command(name="add", aliases=["give"], description="Add user to no prefix")
  async def np_add(self, ctx: Context, user: discord.User):
    if ctx.message.author.id not in self.owner_ids:
            await ctx.send("<a:no:1158411070608769034> | this command can only be executed by my developers .")
            return
    with open('info.json', 'r') as idk:
      data = json.load(idk)
    np = data["np"]
    if user.id in np:
      await ctx.send(embed=discord.Embed(description=f"<a:no:1158411070608769034> | {user.name} Already have no prefix",color=0x0d0d13))
    else:
      data["np"].append(user.id)
    with open('info.json', 'w') as idk:
      json.dump(data, idk, indent=4)
      await ctx.send(embed=discord.Embed(description=f"<a:cx_tick:1158669360223748106> | Added no prefix to {user.name}",color=0x0d0d13))

  @_np.command(name="remove", aliases=["rmv"], description="Remove user from no prefix")
  async def np_remove(self, ctx: Context, user: discord.User):
    if ctx.message.author.id not in self.owner_ids:
            await ctx.send("<a:no:1158411070608769034> | this command can only be executed by my developers .")
            return
    with open('info.json', 'r') as idk:
      data = json.load(idk)
    np = data["np"]
    if user.id not in np:
      await ctx.send(embed=discord.Embed(description=f"<a:no:1158411070608769034> | {user.name} Doesn't have no prefix",color=0x0d0d13))
    else:
      data["np"].remove(user.id)
    with open('info.json', 'w') as idk:
      json.dump(data, idk, indent=4)
      await ctx.send(embed=discord.Embed(description=f"<a:cx_tick:1158669360223748106> | Removed no prefix from {user.name}",color=0x0d0d13))
      
  @_np.command(name="list")
  async def bye_buddy(self, ctx):
    if ctx.message.author.id not in self.owner_ids:
            await ctx.send("<a:no:1158411070608769034> | this command can only be executed by my developers .")
            return
    with open("info.json", "r") as f:
      file = json.load(f)
    if file["np"] == []:
      return await ctx.send("<a:no:1158411070608769034> | No one have no prefix.")
    comrade = []
    for idk in file["np"]:
      member = await self.client.fetch_user(int(idk))
      comrade.append(member)
    await working_lister(title="List Of Users In No Prefix", ctx=ctx, color=0x0d0d13, listxd=comrade)

        
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
            title=f"Server List of LEGEND- {len(self.client.guilds)}",
            color=0x2f3136,
            per_page=10),
                              ctx=ctx)
        await paginator.paginate()
    

