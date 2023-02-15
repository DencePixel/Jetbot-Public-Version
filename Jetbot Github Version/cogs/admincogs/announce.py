import discord.ext
from discord import Color
from configuration import *
from discord.ext import commands
import json
import requests


class announce(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client
    @client.command()
    async def announce(ctx,*,announcement=None):
        modrole = discord.utils.get(ctx.guild.roles,id=modroleid)
        if modrole in ctx.author.roles:
            info = {
                'content' : announcement
            }
            results = requests.post(announce_url,json=info)

            if results.status_code == 204:
                await ctx.reply("Message sent through webhook.")
            else:
                await ctx.reply("Message failed to send through webhook, check discord.log file.")
                
async def setup(client:commands.Bot) -> None:
  await client.add_cog(announce(client))