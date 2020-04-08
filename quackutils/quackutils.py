import time
from datetime import datetime

from dateutil import parser
from natural.date import duration

import discord
from discord.ext import commands

from core import checks
from core.thread import Thread
from core.models import PermissionLevel
from core.utils import *

class QuackUtils(commands.Cog):
    """Custom Commands for Ducky Mail"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="timeleft", aliases=["tl", "time"])
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    @checks.thread_only()
    async def time_left(self, ctx):
        """
        Provides a duration for how long a thread will automatically
        close.
        """

        def convert(seconds):
            return time.strftime("%H hours : %M minutes : %S seconds", time.gmtime(n))

        closure = self.bot.config["closures"]
        for recipient_id, items in tuple(closure.items()):
            after = (datetime.fromisoformat(items["time"]) - datetime.utcnow()).total_seconds()
            n = convert(after)
            thread = ctx.thread
            if thread.close_task is not None or thread.auto_close_task is not None:
                embed = discord.Embed(
                    color=self.bot.error_color,
                    description="This thread is not set to close automatically."
                )
            else:
                embed = discord.Embed(
                    color=self.bot.main_color,
                    description=f"About {n} left until the thread closes."
                )
            
            return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(QuackUtils(bot))
