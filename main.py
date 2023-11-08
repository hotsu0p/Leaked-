import os
from asyncore import loop
import datetime
import random
import time
import math
from core.Astroz import Astroz
import colorama
from colorama import Fore
import asyncio, json
import jishaku, cogs
from discord.ext import commands, tasks
from utils.config import OWNER_IDS, No_Prefix
import discord
from discord import app_commands
import traceback
from discord.ext.commands import Context
from discord import Spotify
import openai
from discord import Embed
from keep_alive import keep_alive
keep_alive()
from cogs.commands.ticket import createTicket, closeTicket

os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"

client = Astroz()
tree = client.tree
clr = 0x41eeee

async def VisionX_stats():
  while True:
    servers = len(client.guilds)
    users = sum(g.member_count for g in client.guilds
                if g.member_count != None)
    sv_ch = client.get_channel(1157962211600375848)
    users_ch = client.get_channel(1157961897572827147)
    await asyncio.sleep(600)
    await sv_ch.edit(name="『Servers : {}』".format(servers))
    await users_ch.edit(name="『Users : {}』".format(users))


class papa(discord.ui.Modal, title='Embed Configuration'):
  tit = discord.ui.TextInput(
    label='Embed Title',
    placeholder='Embed title here',
  )

  description = discord.ui.TextInput(
    label='Embed Description',
    style=discord.TextStyle.long,
    placeholder='Embed description optional',
    required=False,
    max_length=4000,
  )

  thumbnail = discord.ui.TextInput(
    label='Embed Thumbnail',
    placeholder='Embed thumbnail here optional',
    required=False,
  )

  img = discord.ui.TextInput(
    label='Embed Image',
    placeholder='Embed image here optional',
    required=False,
  )

  footer = discord.ui.TextInput(
    label='Embed footer',
    placeholder='Embed footer here optional',
    required=False,)
  
  async def on_submit( self, interaction: discord.Interaction):
    embed = discord.Embed(title=self.tit.value,
                          description=self.description.value,
                          color=0x000000)
    if not self.thumbnail.value is None:
      embed.set_thumbnail(url=self.thumbnail.value)
    if not self.img.value is None:
      embed.set_image(url=self.img.value)
    if not self.footer.value is None:
      embed.set_footer(text=self.footer.value)
    await interaction.response.send_message(embed=embed)
    #await mchannel.send("lol")

  async def on_error(self, interaction: discord.Interaction,
                     error: Exception) -> None:
    await interaction.response.send_message('Oops! Something went wrong.',
                                            ephemeral=True)

    traceback.print_tb(error.__traceback__)


@tree.command(name="embed", description="Create A Embed")
async def _embed( interaction: discord.Interaction) -> None:
  await interaction.response.send_modal(papa())



#####################################


@client.listen("on_guild_join")
async def dexterbalak(guild):
  with open('roles.json', 'r') as f:
    pp = json.load(f)
  if guild:
    if not str(guild.id) in pp:
      pp[str(guild.id)] = {"humanautoroles": [], "botautoroles": []}
      with open('role.json', 'w') as f:
        json.dump(pp, f, indent=4)


@client.listen("on_member_join")
async def autorolessacks(member):
  if member.id == client.user.id:
    return
  else:
    gd = member.guild
    with open('roles.json') as f:
      idk = json.load(f)
    g_ = idk.get(str(member.guild.id))
    human_autoroles = g_['humanautoroles']
    bot_autoroles = g_['botautoroles']
    if human_autoroles == []:
      pass
    else:
      for role in human_autoroles:
        rl = gd.get_role(int(role))
        if not member.bot:
          await member.add_roles(rl, reason="LEGEND Autoroles")
    if bot_autoroles == []:
      pass
    else:
      for rol in bot_autoroles:
        rml = gd.get_role(int(rol))
        if member.bot:
          await member.add_roles(rml, reason="LEGEND Autoroles")

#create_ticket_view = createTicket()
#close_ticket_view = closeTicket()


@client.event
async def on_ready():
  print (Fore.RED+ "MADE FOR All 💖")
  print(Fore.RED + "Loaded & Online!")
  print(Fore.BLUE + f"Logged in as: {client.user}")
  print(Fore.MAGENTA + f"Connected to: {len(client.guilds)} guilds")
  print(Fore.YELLOW + f"Connected to: {len(client.users)} users")
  create_ticket_view = createTicket()
  close_ticket_view = closeTicket()
  client.add_view(create_ticket_view)
  client.add_view(close_ticket_view)
  
  await client.loop.create_task(VisionX_stats())
  try:
    synced = await client.tree.sync()
    print(f"synced {len(synced)} commands")
  except Exception as e:
    print(e)



@client.event
async def on_command_completion(context: Context) -> None:

  full_command_name = context.command.qualified_name
  split = full_command_name.split("\n")
  executed_command = str(split[0])
  hacker = client.get_channel(1157962854952091818)
  if context.guild is not None:
    try:
      embed = discord.Embed(color=0x41eeee)
      embed.set_author(
        name=f"Executed {executed_command} Command By : {context.author}",
        icon_url=f"{context.author.avatar}")
      embed.set_thumbnail(url=f"{context.author.avatar}")
      embed.add_field(
        name="<a:blobpart:1163846302413635656> Command Name :",
        value=f"{executed_command}",
        inline=False)
      embed.add_field(
        name="<a:blobpart:1163846302413635656> Command Executed By :",
        value=
        f"{context.author} | ID: [{context.author.id}](https://discord.com/users/{context.author.id})",
        inline=False)
      embed.set_footer(text="Powered By LEGEND",
                       icon_url=client.user.display_avatar.url)
      await hacker.send(embed=embed)
    except:
      print('xD')
  else:
    try:

      embed1 = discord.Embed(color=0x11100d)
      embed1.set_author(
        name=f"Executed {executed_command} Command By : {context.author}",
        icon_url=f"{context.author.avatar}")
      embed1.set_thumbnail(url=f"{context.author.avatar}")
      embed1.add_field(
        name="<a:blobpart:1163846302413635656> Command Name :",
        value=f"{executed_command}",
        inline=False)
      embed1.add_field(
        name="<a:blobpart:1163846302413635656> Command Executed By :",
        value=
        f"{context.author} | ID: [{context.author.id}](https://discord.com/users/{context.author.id})",
        inline=False)
      embed1.set_footer(text="Powered By LEGEND ",
                        icon_url=client.user.display_avatar.url)
      await hacker.send(embed=embed1)
    except:
      print("xD")


@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(
      f"{ctx.author.mention} You do not have enough permissions to use the `{ctx.command}` command."
    )
  elif isinstance(error, commands.CommandNotFound):
    pass  # do nothing if the command doesn't exist
  else:
    print(f"Error occurred: {str(error)}")




  
@client.command(aliases=['wh'])
@commands.has_permissions(administrator=True)
async def create_hook(ctx, name=None):
  if not name:
    await ctx.send("Please specify a name for the webhook.")
    return
  webhook = await ctx.channel.create_webhook(name=name)
  embed = discord.Embed(
    title=
    f"**<a:no:1158411070608769034> | Webhook __{webhook.name}__ created successfully **",
    color=discord.Color.blue())
  try:
    await ctx.author.send(f"||{webhook.url}||")
    await ctx.author.send(embed=embed)
    await ctx.send(
      f"**<a:no:1158411070608769034>| Webhook :- __{webhook.name}__ created successfully.**\n** Check your DMs for the URL.\n {ctx.author.mention} **"
    )
  except discord.Forbidden:
    await ctx.send(
      f"**<a:no:1158411070608769034>|Webhook:- __{webhook.name}__ ||{webhook.url}|| (Unable to DM user) ** \n {ctx.author.mention}"
    )


@client.command()
@commands.has_permissions(administrator=True)
async def delete_hook(ctx, webhook_id):
  try:
    webhook = await discord.Webhook.from_url(
      webhook_id, adapter=discord.RequestsWebhookAdapter())
    await webhook.delete()
    await ctx.send("Webhook deleted successfully.")
  except discord.NotFound:
    await ctx.send("Webhook not found.")


@client.command(aliases=['all_hooks'])
async def list_hooks(ctx):
  webhooks = await ctx.channel.webhooks()
  if not webhooks:
    await ctx.send("No webhooks found in this channel.")
    return
  embed = discord.Embed(title="List of Webhooks", color=discord.Color.blue())
  for webhook in webhooks:
    embed.add_field(
      name="__Name__",
      value=f"**<a:no:1158411070608769034> | {webhook.name} **")
    embed.add_field(name="__ID__", value=webhook.id)
    embed.add_field(name="\u200b", value="\u200b")
  await ctx.send(
    f"{ctx.author.mention}, Here are the webhooks in this channel",
    embed=embed)




@client.command()
async def spotify(ctx, user: discord.Member = None):
  if user == None:
    user = ctx.author
    pass
  if user.activities:
    for activity in user.activities:
      if isinstance(activity, Spotify):
        nemo = discord.Embed(title=f"{user.name}'s Spotify",
                             description="Listening to {}".format(
                               activity.title),
                             color=0x11100d)
        nemo.set_thumbnail(url=activity.album_cover_url)
        nemo.add_field(name="Artist", value=activity.artist)
        nemo.add_field(name="Album", value=activity.album)
        nemo.set_footer(text="Song started at {}".format(
          activity.created_at.strftime("%H:%M")))
        await ctx.send(embed=nemo)

@client.event
async def on_guild_join(guild):
    channel_id = 1157962819493445693 # Replace with the ID of the channel you want to send the message to
    channel = client.get_channel(channel_id)
    if channel:
        await channel.send(f"LEGEND has been added to the server: {guild.name}")

@client.command()
async def chatgpt(ctx, *, question):
    embed = Embed(
        description="<a:loading:1160242511533588650> | Loading, Please Wait...",
        color=0x11100d
    )
    loading_message = await ctx.send(embed=embed)
    

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        max_tokens=3000,
        temperature=0.7
    )
    output = response["choices"][0]["text"]
    

    await asyncio.sleep(5)
    

    embed = Embed(description=f"```python {output}```", color=0x11100d)
    embed.set_author(
        name="LEGEND Chat Gpt`s Response:",
        icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url
    )
    embed.set_footer(
        text=f"Requested By {ctx.author}",
        icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url
    )
    

    await loading_message.delete()
    await ctx.send(embed=embed)


bot = client
@bot.command()
async def say(ctx, *, message=None):
    if message is None:
        await ctx.send("**Please provide a message to say.**")
        return
    await ctx.message.delete()
    await ctx.send(message)




@bot.command()
async def reaction(ctx):
    """
    See how fast you can get the correct emoji.
    """
    emoji = ["🍪", "🎉", "🧋", "🍒", "🍑"]
    random_emoji = random.choice(emoji)
    random.shuffle(emoji)
    embed = discord.Embed(
        title="Reaction time",
        description="After 1-15 seconds I will reveal the emoji.",
        color=0x01f5b6)
    first = await ctx.send(embed=embed)
    for react in emoji:
        await first.add_reaction(react)
    await asyncio.sleep(2.5)
    embed.description = "Get ready!"
    await first.edit(embed=embed)
    await asyncio.sleep(random.randint(1, 15))
    embed.description = f"GET THE {random_emoji} EMOJI!"
    await first.edit(embed=embed)

    def check(reaction, user):
        return reaction.message.id == first.id and str(
            reaction.emoji) == random_emoji and user != bot.user

    try:
        start_time = time.time()
        reaction, user = await bot.wait_for("reaction_add",
                                            check=check,
                                            timeout=15)
        end_time = time.time()
        reaction_time = end_time - start_time
    except asyncio.TimeoutError:
        embed.description = "Timeout"
        await first.edit(embed=embed)
    else:
        total_second = f"**{reaction_time * 1000:.2f}ms**"
        if reaction_time > 1:
            total_second = f"**{reaction_time:.2f}s**"
        embed.description = f"{user.mention} got the {random_emoji} in {total_second}"
        await first.edit(embed=embed)



async def main():
  async with client:
    os.system("clear")
    await client.load_extension("cogs")
    await client.load_extension("jishaku")
    await client.start("MTE3MDczNTExNTg5MTEyNjMwMg.GdVQ6L.fmMdCZ_lDVtRo9kK14jaucEfVRkRat2cGcpDBE")


if __name__ == "__main__":
  openai.api_key = os.getenv("Api")
  asyncio.run(main())
