from discord.ext import commands
import discord

class Talks(commands.Cog):
    """Talks with user"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hi", help="Envia um Olá. Não requer argumentos")
    async def send_hello(self, ctx):
        name = ctx.author.mention

        response = name + ", Hello"

        await ctx.send(response)

    @commands.command(name="random", help="Envia uma dm. Não requer argumentos")
    async def random(self, ctx):
        try:
            name = ctx.author.mention
            
            await ctx.author.send("https://imageproxy.ifunny.co/crop:x-20,resize:640x,quality:90x75/images/f470034af8538a4b7cdf428d667dae64763c5474a3726a751690d7b28d2b6835_1.jpg")
            await ctx.send(name + " Olhe sua dm")

        except discord.errors.Forbidden:
            await ctx.send("Ative sua dm e tente novamente")


def setup(bot):
    bot.add_cog(Talks(bot))
