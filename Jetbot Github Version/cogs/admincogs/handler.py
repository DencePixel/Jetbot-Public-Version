import discord.ext
from discord import Color
from configuration import *
from discord.ext import commands
import json
import requests


class handl(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client
    @client.command()
    async def handler(ctx):
        adminrole = discord.utils.get(ctx.guild.roles,id=adminroleid)
        if adminrole in ctx.author.roles:
            with open('discord.log', 'r') as f:
                log_file = f.read()
            await ctx.send(f'```{log_file}```')


                
async def setup(client:commands.Bot) -> None:
  await client.add_cog(handl(client))