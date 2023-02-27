import discord
from discord.ext import commands
from discord import app_commands
import discord.ext
from discord import Color
import time
from configuration import *

class purge(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client
  @commands.command(name="purge")
  async def purge(self, ctx, amount : int):
    modrole = discord.utils.get(ctx.guild.roles, id=modroleid)
    adminrole = discord.utils.get(ctx.guild.roles, id=adminroleid)
    if modrole in ctx.author.roles or adminrole in ctx.author.roles:
      message1 = await ctx.send(f"Deleting {amount} messages...")
      deleted_messages = await ctx.channel.purge(limit=amount)
      await message1.edit(content=f"Succesfully deleted {amount} messages.")

async def setup(client:commands.Bot) -> None:
  await client.add_cog(purge(client))