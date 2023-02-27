import discord
from discord.ext import commands
from discord import app_commands
import discord.ext
from discord import Color
from configuration import *

class slowmode(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client
  @commands.command(name="slowmode", pass_context=True)
  async def slowmode(self, ctx, amount:int):
        modrole = discord.utils.get(ctx.guild.roles,id=modroleid)
        adminrole = discord.utils.get(ctx.guild.roles,id=adminroleid)
        if modrole or adminrole in ctx.author.roles:
            await ctx.channel.edit(slowmode_delay=amount)
            await ctx.reply(f"Channel Slowmode set to {amount} seconds!")
        else:
          await ctx.reply("Error occured.")

async def setup(client:commands.Bot) -> None:
  await client.add_cog(slowmode(client))