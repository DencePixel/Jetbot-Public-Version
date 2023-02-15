import discord
from discord.ext import commands
from discord import app_commands
import discord.ext
from discord import Color
import random
from configuration import rizzer




hasriz = [
  "1000 Rizz",
  "No Rizz",
  "Negative Rizz",
  "Unwanted Rizz"
]

isriz = [
  "Rizz God",
  "Wizard Of Rizz",
  "Rizzer"
]

class rizzlevel(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client
    @client.command(name="rizz")
    async def rizz(ctx):
      answer = random.choice(rizzer)

      if answer in hasriz:
        embed = discord.Embed(color=discord.Color.blurple(), title=f"Rizz Level - {ctx.author}")
        embed.add_field(name="Rizz", value=f"{ctx.author.mention} has {random.choice(rizzer)}")

      if answer in isriz:
        embed = discord.Embed(color=discord.Color.blurple(), title=f"Rizz Level - {ctx.author}")
        embed.add_field(name="Rizz", value=f"{ctx.author.mention} is the {random.choice(rizzer)}")

      await ctx.send(embed=embed)

async def setup(client:commands.Bot) -> None:
  await client.add_cog(rizzlevel(client))