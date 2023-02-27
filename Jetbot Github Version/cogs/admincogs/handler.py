import discord.ext
from discord import Color
from configuration import *
from discord.ext import commands
import traceback

class handle(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client
  @commands.command()
  async def handler(self, ctx):
    adminrole = discord.utils.get(ctx.guild.roles, id=adminroleid)
    if adminrole in ctx.author.roles:
      try:
        # Your code that may cause an exception
        await ctx.send("Hello, world!")
      except Exception as e:
        # Get the traceback information
        tb = traceback.format_exception(type(e), e, e.__traceback__)
        # Join the traceback information into a string
        error_message = "".join(tb)
        # Send the error message to the channel
        await ctx.send(f'```{error_message}```')

async def setup(client:commands.Bot) -> None:
  await client.add_cog(handle(client))