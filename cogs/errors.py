import discord
from discord.ext import commands


class ErrorCatcher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: discord.ApplicationContext, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.respond("Command not found")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.respond("Missing required argument")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.respond("Missing permissions")
        elif isinstance(error, commands.CheckFailure):
            await ctx.respond("You cant do that!")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.respond("You are on cooldown")
        else:
            await ctx.respond("An error has occured")
            raise error


def setup(bot):
    bot.add_cog(ErrorCatcher(bot))
