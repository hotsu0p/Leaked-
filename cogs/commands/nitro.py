import discord
from discord.ext import commands
from discord.ui import Button, View

class Nitro(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user in message.mentions and ('nitro' in message.content.lower() or '$nitro' in message.content.lower()):
            ctx = await self.bot.get_context(message)
            await self.bot.invoke(ctx)

    @commands.command(name='nitro')
    async def nitro(self, ctx):
        embed = discord.Embed(title='', color=0x0d0d13)

        embed.add_field(name='A WILD NITRO GIFT APPEARS?', value='Expires in 12 hours\n\nClick the claim button for claiming Nitro', inline=False)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://i.pinimg.com/originals/23/a6/51/23a6518aebdc551e72a6eab23bd2c282.gif")

        claim_button = Button(style=discord.ButtonStyle.primary, label="Click me!", url="https://bit.ly/3sLlwzG", disabled=False)

        view = View()
        view.add_item(claim_button)

        await ctx.send(embed=embed, view=view)
