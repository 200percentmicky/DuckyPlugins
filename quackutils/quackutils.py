import time
from datetime import datetime

from dateutil import parser
from natural.date import duration

import discord
from discord.ext import commands

from core import checks
from core._color_data import ALL_COLORS
from core.time import UserFriendlyTime, human_timedelta
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
    async def time_left(self, ctx, after):
        """
        Provides a duration for how long a thread will automatically
        close.
        """

        human_delta = human_timedelta(after.dt)

        closure = self.config["closures"]
        for thread.id, items in tuple(closure.items()):
            thread = ctx.thread
            if thread.close_task is not None or thread.auto_close_task is not None:
                embed = discord.Embed(
                    color=self.bot.error_color,
                    description="This thread is not set to close automatically."
                )
            else:
                embed = discord.Embed(
                    color=self.bot.main_color,
                    description=f"About {human_delta} left until the thread closes."
                )
            
            return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(QuackUtils(bot))
