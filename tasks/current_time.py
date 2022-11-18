from discord.ext import commands, tasks
import time
import datetime

class Tasks(commands.Cog):
    """Current time TASK"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.time.start()

    @tasks.loop(hours=10)
    async def time(self):
        now = datetime.datetime.now()

        now = now.strftime("%d/%m/%Y às %H:%M:%S")

        channel = self.bot.get_channel(1042050875335659613)

        await channel.send("Data atual: " + now)

def setup(bot):
    bot.add_cog(Tasks(bot))