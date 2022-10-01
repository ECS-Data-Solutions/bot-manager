
import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup


class BetaTesters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = self.bot.get_cluster()

    beta = SlashCommandGroup("beta", "Beta Testers commands")

    beta_admin = SlashCommandGroup(
        "betaa",
        "Beta Testers Admin commands",
        checks=[commands.is_owner().predicate],  # Ensures the owner_id user can access this group, and no one else
    )

    beta_testers = SlashCommandGroup(
        "betab",
        "Beta Testers Tester commands",
        checks=[commands.has_role(1015004274121515081)],
    )

    @beta_admin.command()
    async def add(self, ctx: discord.ApplicationContext, user: discord.Member):
        # Add user to beta testers role
        await user.add_roles(ctx.guild.get_role(1015004274121515081))
        # Add user to beta testers collection
        self.db.testers.insert_one({"id": user.id, "account_created": False, "license_created": False})
        await ctx.respond(f"{user.mention} has been added to beta testers")

    @beta_admin.command()
    async def remove(self, ctx: discord.ApplicationContext, user: discord.Member):
        # Remove user from beta testers role
        await user.remove_roles(ctx.guild.get_role(1015004274121515081))
        # Remove user from beta testers collection
        self.db.testers.delete_one({"id": user.id})
        await ctx.respond(f"{user.mention} has been removed from beta testers")

    @beta_admin.command()
    async def init_db(self, ctx: discord.ApplicationContext):
        # Insert all beta testers into database
        for member in ctx.guild.get_role(1015004274121515081).members:
            self.db.testers.insert_one({"id": member.id, "account_created": False, "license_created": False})


def setup(bot):
    bot.add_cog(BetaTesters(bot))

