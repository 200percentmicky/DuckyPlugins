import discord
from discord.ext import commands
import logging

from core import checks
from core.models import PermissionLevel
from core.utils import *

logger = logging.getLogger("Modmail")

class QuackUtils(commands.Cog):
    """Custom Commands for Ducky Mail"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="restart", aliases=["reboot"])
    @checks.has_permissions(PermissionLevel.OWNER)
    async def restart(self, ctx):
        """
        Reboots the bot.
        Only works if the bot is handled by a process manager.
        """

        await ctx.send(embed=discord.Embed(
            color=37887,
            description="🔁 Restarting..."
        ))
        user = ctx.message.author
        logger.info(f"Restart initiated by {user.name}#{user.discriminator} ({user.id})")
        logger.info("Rebooting bot...")
        await ctx.bot.logout()

def setup(bot):
    bot.add_cog(QuackUtils(bot))
