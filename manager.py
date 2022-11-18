from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound

class Manager(commands.Cog):
    """Manage the bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"I'm ready! I'm logged on as {self.bot.user}")


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if "sexo" in message.content:
            await message.channel.send (f"{message.author.mention} SEXOO!")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Envie o comando corretamente! Envie ?help para ver a função dos comandos")
        elif isinstance(error, CommandNotFound):
            await ctx.send("Este comando não existe. Envie ?help para ver a função dos comandos")
        else:
            raise error


def setup(bot):
    bot.add_cog(Manager(bot))