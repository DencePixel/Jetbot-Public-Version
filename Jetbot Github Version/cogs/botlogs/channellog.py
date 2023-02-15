import discord
from discord.ext import commands
from discord import app_commands
import discord.ext
from discord import Color
import random
from configuration import *

class channellogs(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client
    @client.event
    async def on_guild_channel_create(channel):
        if advancelogging == None or False:
            simpleloggingchan = client.get_channel(logchannelid)
            embed = discord.Embed(color=discord.Color.green(),title="Channel Created")
            embed.add_field(name="Channel Created:",value=f"{channel.mention} has been Created.", inline=True)
            embed.set_footer(text="Jetbot - Simple Logging System")
            await simpleloggingchan.send(embed=embed)
        if advancelogging == True:
            advancloggingchan = client.get_channel(channellogid)
            embed = discord.Embed(color=discord.Color.green(),title="Channel Created")
            embed.add_field(name="Channel ",value=f"{channel.mention} has been Created by .", inline=False)
            embed.set_footer(text="Jetbot - Advanced Logging System")
            await advancloggingchan.send(embed=embed)

    @client.event
    async def on_guild_channel_delete(channel):
        if advancelogging == None or False:
            simpleloggingchan = client.get_channel(logchannelid)
            embed = discord.Embed(color=discord.Color.red(),title="Channel Deleted")
            embed.add_field(name="Channel Deleted:",value=f"{channel.name} has been Deleted.", inline=True)
            embed.set_footer(text="Jetbot - Simple Logging System")
            await simpleloggingchan.send(embed=embed)
        if advancelogging == True:
            advancloggingchan = client.get_channel(channellogid)
            embed = discord.Embed(color=discord.Color.red(),title="Channel Deleted")
            embed.add_field(name="Channel Deleted",value=f"{channel.name} has been Deleted.", inline=False)
            embed.set_footer(text="Jetbot - Advanced Logging System")
            await advancloggingchan.send(embed=embed)

async def setup(client:commands.Bot) -> None:
  await client.add_cog(channellogs(client))