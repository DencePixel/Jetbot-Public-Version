import discord
from discord.ext import commands
from discord import app_commands
import discord.ext
from discord import Color
import random
from configuration import *

class rolelogs(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client
    @client.event
    async def on_guild_role_create(role):
        if advancelogging == None or False:
            log_channel1 = client.get_channel(logchannelid)
            embed = discord.Embed(color=discord.Color.green(),title="Role Created")
            embed.add_field(name="New Role:", value=role.mention, inline=False)
            embed.set_footer(text=f"Jetbot - Simple Logging System")
            await log_channel1.send(embed=embed)

        if advancelogging == True:
            rolelog = client.get_channel(rolelogid)
            embed = discord.Embed(color=discord.Color.green(),title="Role Created")
            embed.add_field(name="New Role:", value=role.mention, inline=False)
            embed.set_footer(text=f"Jetbot - Advanced Logging System")
            await rolelog.send(embed=embed)



    @client.event
    async def on_guild_role_delete(role):
        if advancelogging == None or False:
            log_channel1 = client.get_channel(logchannelid)
            embed = discord.Embed(color=discord.Color.red(),title="Role Deleted")
            embed.add_field(name="Deleted Role:", value=role, inline=False)
            embed.set_footer(text=f"Jetbot - Logging System")
            await log_channel1.send(embed=embed)

        if advancelogging == True:
            rolelog = client.get_channel(rolelogid)
            embed = discord.Embed(color=discord.Color.red(),title="Role Deleted")
            embed.add_field(name="Deleted Role:", value=role, inline=False)
            embed.set_footer(text=f"Jetbot - Advanced Logging System")
            await rolelog.send(embed=embed)




async def setup(client:commands.Bot) -> None:
  await client.add_cog(rolelogs(client))
