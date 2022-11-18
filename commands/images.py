from discord.ext import commands
import discord

class Image(commands.Cog):
    """Random images found"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="image", help="Mostra uma imagem aleatória de acordo com as características que você escolheu. Argumentos: largura, altura")
    async def get_random_image(self, ctx, largura, altura):
        url_image = f"https://picsum.photos/{largura}/{altura}"

        embed_image = discord.Embed(
            title="Resultado da busca",
            description="Este resultado é aleatório",
            color=0x000000
        )

        embed_image.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed_image.set_footer(text="Feito por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

        embed_image.add_field(name="API", value="Usamos a api do https://picsum.photos")
        embed_image.add_field(name="Parâmetros", value=f"{largura}/{altura}")

        embed_image.add_field(name="Exemplo", value=url_image, inline=False)

        embed_image.set_image(url=url_image)    

        await ctx.send(embed=embed_image)


def setup(bot):
    bot.add_cog(Image(bot))