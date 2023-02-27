import discord
from discord.ext import commands
from colorama import Back, Fore, Style
import time
import json
import platform
from configuration import *
import logging
from dislash import InteractionClient, ActionRow, Button, ButtonStyle

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or(bot_prefix), intents=discord.Intents().all())

        self.cogslist = ["cogs.funcogs.rizzlevel","cogs.funcogs.gayrate","cogs.admincogs.kick","cogs.admincogs.ban","cogs.maincogs.rosearch","cogs.maincogs.ping","cogs.botlogs.rolelog","cogs.botlogs.channellog","cogs.botlogs.memberlog","cogs.maincogs.welcome","cogs.admincogs.announce","cogs.admincogs.handler","cogs.botlogs.messagelog","cogs.admincogs.antilink","cogs.admincogs.slowmode","cogs.maincogs.repo","cogs.admincogs.purge"]

    async def setup_hook(self):
      for ext in self.cogslist:
        await self.load_extension(ext)

    async def on_ready(self):
        prfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S GMT", time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
        print(prfx + " Logged in as " + Fore.YELLOW + self.user.name)
        print(prfx + " Bot ID " + Fore.YELLOW + str(self.user.id))
        print(prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
        print(prfx + " Python Version " + Fore.YELLOW + str(platform.python_version()))
        synced = await self.tree.sync()


    

client = Client()



client.run(token, log_handler=handler)
