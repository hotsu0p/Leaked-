# AMAN OP
import os
import discord
from discord.ext import commands
from discord.ui import View,Button



class Embed(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.client = bot

  @commands.command(name="tests")
  async def __embed_(self, ctx):
      msgx = "This is an example embed, You can customize everything."
      embed = discord.Embed(description="ok", color=0x2f3136)

      async def wait_for_message(channel):
          def check(m):
              return m.channel == channel and m.author == ctx.author and not m.author.bot

          try:
              response = await self.bot.wait_for("message", timeout=30, check=check)
              return response.content
          except Exception as e:
            print(e)
            await ctx.send("Timed Out")
            return None

      button1 = Button(label="Title", style=discord.ButtonStyle.green)
      await ctx.send("Please enter the title of the embed.")
      title = await wait_for_message(ctx.channel)
      if title:
          embed.title = title
          await ctx.send(content=msgx, embed=embed)

      button2 = Button(label="Description", style=discord.ButtonStyle.green)
      await ctx.send("Please enter the description of the embed.")
      description = await wait_for_message(ctx.channel)
      if description:
          embed.description = description
          await ctx.send(content=msgx, embed=embed)

      button3 = Button(label="Color", style=discord.ButtonStyle.green)
      await ctx.send("Please enter the color of the embed (e.g., hex code or integer).")
      color = await wait_for_message(ctx.channel)
      if color:
          try:
              embed.color = discord.Colour(int(color, 16))
              await ctx.send(content=msgx, embed=embed)
          except ValueError:
              await ctx.send("Invalid color format. Please use a hex code or integer.")

      button4 = Button(label="Thumbnail", style=discord.ButtonStyle.green)
      await ctx.send("Please enter the URL of the thumbnail.")
      thumbnail_url = await wait_for_message(ctx.channel)
      if thumbnail_url:
          embed.set_thumbnail(url=thumbnail_url)
          await ctx.send(content=msgx, embed=embed)

      button5 = Button(label="Image", style=discord.ButtonStyle.green)
      await ctx.send("Please enter the URL of the image.")
      image_url = await wait_for_message(ctx.channel)
      if image_url:
          embed.set_image(url=image_url)
          await ctx.send(content=msgx, embed=embed)

      button6 = Button(label="Footer", style=discord.ButtonStyle.green)
      await ctx.send("Please enter the text for the footer.")
      footer_text = await wait_for_message(ctx.channel)
      if footer_text:
          embed.set_footer(text=footer_text)
          await ctx.send(content=msgx, embed=embed)

      button7 = Button(label="Send", style=discord.ButtonStyle.blurple)
      await ctx.send("Please mention the channel where you want to send this embed.")
      channel_mention = await wait_for_message(ctx.channel)
      if channel_mention:
          try:
              channel = discord.utils.get(ctx.guild.channels, mention=channel_mention)
              if channel:
                  await channel.send(embed=embed)
                  await ctx.send("Sent")
              else:
                  await ctx.send("Invalid channel mention.")
          except discord.Forbidden:
              await ctx.send("I don't have permission to send messages in that channel.")

      views = View()
      buttons = [button1, button2, button3, button4, button5, button6, button7]
      for pp in buttons:
          views.add_item(pp)

      msg = await ctx.send(embed=embed, content=msgx, view=views)
      ctx.message = msg
  @commands.hybrid_command(name="embeds")
  async def _embeds(self, ctx):
    msgx = "This is an example embed, You can customize everything."
    embed = discord.Embed(description="ok", color=0x2f3136)
    button1 = Button(label="Title", style=discord.ButtonStyle.green, row=1)   
    def chk(m):
            return m.channel ==  and m.author == ctx.author and not m.author.bot    
    async def button_cal(interaction):
      try:
        await ctx.send("Please enter the title of the embed.")
        tit = await ctx.bot.wait_for("message", timeout=30, check=chk)
        embed.title = tit.content
        await ctx.message.edit(content=msgx, embed=embed)
      except Exception as e:
        print(e)
        await ctx.send("Timed Out")
      
    button1.callback = button_cal
    button2 = Button(label="Description", style=discord.ButtonStyle.green, row=1)
    async def button_call(interaction):
      tit = ""
      try:
        await ctx.send("Please enter the description of the embed.")
        tit = await ctx.bot.wait_for("message", timeout=30, check=chk)        
      except Exception as e:
        print(e)
        await ctx.send("Timed Out")
      embed.description = tit.content
      await ctx.message.edit(content=msgx, embed=embed)    
    button2.callback = button_call

    button3 = Button(label="Color", style=discord.ButtonStyle.green, row=1)
    async def button_calll(interaction):
      tit = ""
      try:
        await ctx.send("Please enter the color of the embed.")
        tit = await ctx.bot.wait_for("message", timeout=30, check=chk)
      except Exception as e:
        print(e)
        await ctx.send("Timed Out")
      embed.color = discord.Colour(tit.content)
      await ctx.message.edit(content=msgx, embed=embed)
    button3.callback = button_calll
    button4 = Button(label="Thumbnail", style=discord.ButtonStyle.green, row=2)
    async def button_callll(interaction):
      tit = ""
      try:
        await ctx.send("Please enter the url of the thumbnail.")
        tit = await ctx.bot.wait_for("message", timeout=30, check=chk)
      except Exception as e:
        print(e)
        await ctx.send("Timed Out")
      embed.set_thumbnail(url=tit.content)
      await ctx.message.edit(content=msgx, embed=embed)
    button4.callback = button_callll
    button5 = Button(label="Image", style=discord.ButtonStyle.green, row=2)
    async def button_calllll(interaction):
      tit = ""
      try:
        await ctx.send("Please enter the url of the image.")
        tit = await ctx.bot.wait_for("message", timeout=30, check=chk)
      except Exception as e:
        print(e)
        await ctx.send("Timed Out")
      embed.set_image(url=tit.content)
      await ctx.message.edit(content=msgx, embed=embed)
    button5.callback = button_calllll
    button6 = Button(label="Footer", style=discord.ButtonStyle.green, row=3)
    async def button_callllll(interaction):
      tit = ""
      try:
        await ctx.send("Please enter the text of footer.")
        tit = await ctx.bot.wait_for("message", timeout=30, check=chk)
      except Exception as e:
        print(e)
        await ctx.send("Timed Out")
      embed.set_footer(text=tit.content)
      await ctx.message.edit(content=msgx, embed=embed)
    button6.callback = button_callllll
    button7 = Button(label="Send", style=discord.ButtonStyle.blurple,row=3)
    async def button_callllllll(interaction):
      tit = ""
      try:
        await ctx.send("Please enter the channel where you want to send this embed.")
        tit = await ctx.bot.wait_for("message", timeout=30, check=chk)
      except Exception as e:
        print(e)
        await ctx.send("Timed Out")
      chnl = tit.channel_mentions[0]
      await chnl.send(embed=embed)
      await ctx.send("Sent")
    button7.callback = button_callllllll
    LING = View()
    buttons = [button1,button2,button3, button4,button5, button6, button7]
    for pp in buttons:
      LING.add_item(pp)
    msg=await ctx.send(embed=embed,content=msgx, view=LING)
    ctx.message = msg