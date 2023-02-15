import discord
from discord.ext import commands
from discord import app_commands
import discord.ext
from discord import Color
import json
import requests

class welcome(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client
    @client.event
    async def on_member_join(member):
        embed = discord.Embed(color=discord.Color.og_blurple(), title="Jet Bot - New Member")
        embed.add_field(name="New Member:",value=f"Welcome {member.mention}")
        embed.add_field(name="What is this server?", value="Welcome to Jetbot! The official discord bot for the currently in development jet bot which is meant to be a beginner friendly bot that you can use for yourself, but you have to sort everything!")
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text="Jetbot - Welcome")

async def setup(client:commands.Bot) -> None:
  await client.add_cog(welcome(client))