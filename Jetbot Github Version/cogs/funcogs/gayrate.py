import discord
from discord.ext import commands
from discord import app_commands
import discord.ext
from discord import Color
import random
from configuration import rizzer

class gayrate(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client
    @client.command(name="gayrate")
    async def gayrate(ctx):
        await ctx.send(f"You are {random.randint(0,101)}% gay")

async def setup(client:commands.Bot) -> None:
  await client.add_cog(gayrate(client))