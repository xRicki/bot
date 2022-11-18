from discord.ext import commands
import requests

class Crypto(commands.Cog):
    """Crypto values"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="bnc", help="Verifica o preço de um par na binance. Argumentos: moeda, base")
    async def random_api(self, ctx, coin, convert):
        try:
            response = requests.get(f"https://economia.awesomeapi.com.br/last/{coin.upper()}-{convert.upper()}")
            print(response)

            data = response.json()
            bid = data.get("bid")

            if bid:
                await ctx.send(f"O valor do par {coin}/{convert} é {bid}")
            else:
                await ctx.send(f"O par {coin}/{convert} é inválido")
        except Exception as error:
            await ctx.send("Ops... Deu algum erro!")
            print(error)

def setup(bot):
    bot.add_cog(Crypto(bot))