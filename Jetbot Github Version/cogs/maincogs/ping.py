import discord
from discord.ext import commands
from discord import app_commands
import discord.ext
from discord import Color
import json
import requests

class ping(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client
    @client.command()
    async def ping(ctx):
        embed = discord.Embed(color=discord.Color.blurple(),title="Ping - Jetbot",description="Jetbots current ping!")
        embed.add_field(name="Current Ping",value=(f'Pong! In {round(client.latency * 1000)}ms'))
        embed.set_footer(text="Jetbot - Ping")
        embed.set_thumbnail(url=ctx.author.avatar.url)
        await ctx.send(embed=embed)


async def setup(client:commands.Bot) -> None:
  await client.add_cog(ping(client))