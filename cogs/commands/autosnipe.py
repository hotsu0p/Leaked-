import discord, json
from discord.ext import commands
import motor.motor_asyncio as mongodb

class autosnipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.connection = mongodb.AsyncIOMotorClient("mongodb+srv://hacker:chetan2004@cluster0.rxh8r.mongodb.net/Flame?retryWrites=true&w=majority")
        self.db = self.connection["LEGEND"]["servers"]

    @commands.group(name="autosnipe", description="autosnipe channel\autosnipe config\autosnipe delete", invoke_without_command=True)
    @commands.has_permissions(administrator=True)
    async def autosnipe(self, ctx):
        """autosnipe channel\autosnipe config\leave delete"""
        x = "$"
        await ctx.send(f" Available Commands: `{x}autosnipe channel`")

    @autosnipe.command()
    @commands.has_permissions(administrator=True)
    async def channel(self, ctx, c: discord.TextChannel):
        try:
            await self.db.update_one(
                {
                    "guild": ctx.guild.id
                },
                {
                    "$set": {
                        "autosnipe-channel" : c.id
                    }
                }
            )
            await ctx.send(f"<a:cx_tick:1158669360223748106>  | autosnipe channel are updated to <#{c.id}>")
        except Exception as e:
            return await ctx.send(f"An error occoured {e}")

    @autosnipe.command(aliases=['show'])
    @commands.has_permissions(administrator=True)
    async def config(self, ctx):
        data = await self.db.find_one({"guild": ctx.guild.id})     
        x = data["autosnipe-channel"]
        if x == None:
          embed = discord.Embed(title=f"autosnipe channel:", description=f"No autosnipe Channel Found", color = 0x2f3136)
          await ctx.send(embed=embed)
        else:
          embed = discord.Embed(title=f"autosnipe channel:", description=f"<#{x}>", color = 0x2f3136)
          await ctx.send(embed=embed)

    @autosnipe.command()
    @commands.has_permissions(administrator=True)
    async def delete(self, ctx: commands.Context):
        await self.db.update_one(
                {
                    "guild": ctx.guild.id
                },
                {
                    "$set": {
                        "autosnipe-channel" : None
                    }
                }
            )
        await ctx.send(f'<a:cx_tick:1158669360223748106> | Successfully Deleted autosnipe Channel')

    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload: discord.RawMessageDeleteEvent):
        data = await self.db.find_one({"guild": payload.guild_id})     
        x = data["autosnipe-channel"]
        if x == None:
          return
        else: 
          channel = self.bot.get_channel(x)
          embed = discord.Embed(description=f'⚠️ Auto Snipe | Message sent by {payload.cached_message.author.mention} deleted in <#{payload.channel_id}>', color = 0x2f3136)
          embed.add_field(name=f"Auto Snipe | Deleted By", value=f"{payload.cached_message.author.mention}")
          embed.add_field(name="Auto Snipe | Message", value=f"{payload.cached_message.content}")
          embed.set_footer("MESSAGEMEESSAG", icon_url=self.bot.user.avatar)
          await channel.send(embed=embed)
          