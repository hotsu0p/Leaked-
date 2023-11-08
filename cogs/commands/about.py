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
        embed = discord.Embed(title='About LEGEND', color=0x11100d)

        embed.add_field(name='', value='LEGEND is the Best bot with over 450+ commands. It protects your server and provides various features.', inline=False)
        embed.add_field(name='Commands', value='You can use `$help` to see a list of available commands.', inline=False)      
        embed.add_field(name='**<a:moon:1158411057325428756>・OWNER**', value='[Lord Sgamerz_](https://discord.com/users/926831289649201213)', inline=False)#
        embed.add_field(name='**<:clyde:1162357587967225856>・DEVELOPER**', value='[༄ᏞᎾᏒᎠ༒ÂMΔÑ࿐](https://discord.com/users/926831289649201213) ', inline=False)

        embed.set_author(name="About LEGEND",icon_url=self.bot.user.display_avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url=self.bot.user.avatar.url)

  #check server


        invite_link = 'https://discord.com/api/oauth2/authorize?client_id=1163839531880038460&permissions=8&scope=bot'
        support_server_link = 'https://discord.gg/3Khp9KedDq'
      

        buttons = [
            Button(style=discord.ButtonStyle.link, label='Invite LEGEND', url=invite_link),
            Button(style=discord.ButtonStyle.link, label='Join Support Server', url=support_server_link)
        ]

        view = View()
        view.add_item(buttons[0])
        view.add_item(buttons[1])

        await ctx.send(embed=embed, view=view)