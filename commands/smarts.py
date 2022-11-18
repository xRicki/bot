from discord.ext import commands

class Smarts(commands.Cog):
    """Work with expressions"""

    def __init__(self, bot):
        self.bot = bot

@commands.command(name="calc", help="Calcula uma expressão. Argumentos: expressão")
async def calc(self, ctx, *expression):
    expression = "".join(expression)

    response = eval(expression)

    await ctx.send("O resultado é: " + str(response))

def setup(bot):
    bot.add_cog(Smarts(bot))