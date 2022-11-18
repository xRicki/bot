from discord.ext import commands

class Reactions(commands.Cog):
    """Work with reactions"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction.emoji)
        if reaction.emoji == "👍":
            role = user.guild.get_role(1042583639390703658)
            await user.add_roles(role)
        
        elif reaction.emoji == "👎":
            role = user.guild.get_role(1042583809146769502)
            await user.add_roles(role) 

def setup(bot):
    bot.add_cog(Reactions(bot))