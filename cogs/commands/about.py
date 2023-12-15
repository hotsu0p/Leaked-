import discord
from discord.ext import commands
from discord.ui import Button, View

class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user in message.mentions and ('about' in message.content.lower() or '$about' in message.content.lower()):
            ctx = await self.bot.get_context(message)
            await self.bot.invoke(ctx)

    @commands.command(name='about')
    async def about(self, ctx):
        embed = discord.Embed(title='About Chatoic', color=0x11100d)

        embed.add_field(name='', value='Chatoic is the Best bot with over 450+ commands. It protects your server and provides various features.', inline=False)
        embed.add_field(name='Commands', value='You can use `$help` to see a list of available commands.', inline=False)      
        embed.add_field(name='**<a:moon:1158411057325428756>・OWNER**', value='[Hotsuop](https://discord.com/users/969655699154042940)', inline=False)#
        embed.add_field(name='**<:clyde:1162357587967225856>・DEVELOPER**', value='[Hotsuop](https://discord.com/users/969655699154042940) ', inline=False)

        embed.set_author(name="About Chatoic",icon_url=self.bot.user.display_avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url=self.bot.user.avatar.url)

  #check server


        invite_link = 'https://discord.com/api/oauth2/authorize?client_id=1170735115891126302&permissions=8&scope=bot'
        support_server_link = 'https://discord.gg/jj25BZgrFb'
      

        buttons = [
            Button(style=discord.ButtonStyle.link, label='Invite Chatoic', url=invite_link),
            Button(style=discord.ButtonStyle.link, label='Join Support Server', url=support_server_link)
        ]

        view = View()
        view.add_item(buttons[0])
        view.add_item(buttons[1])

        await ctx.send(embed=embed, view=view)