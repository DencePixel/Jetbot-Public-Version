import discord
from discord.ext import commands
from discord import app_commands
import discord.ext
from discord import Color
import random
from configuration import *

class memberlog(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if advancelogging == False or advancelogging == None:
            log_channel1 = self.client.get_channel(logchannelid)
            guild = member.guild
            guild_name = guild.name
            embed = discord.Embed(color=discord.Color.green(),title="Member Has Joined")
            embed.add_field(name="Member Joined:", value=f"{member.mention} has joined {guild_name}", inline=False)
            embed.set_footer(text=f"Jetbot - Simple Logging System")
            await log_channel1.send(embed=embed)
        if advancelogging == True:
            memberlogchan = self.client.get_channel(memberlogid)
            guild = member.guild
            guild_name = guild.name
            embed = discord.Embed(color=discord.Color.green(), title="Member Has Joined")
            embed.add_field(name="Member Joined:", value=f"{member.mention} has joined {guild_name}")
            embed.set_footer(text=f"Jetbot - Advanced logging System")
            await memberlogchan.send(embed=embed)
            
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if advancelogging == False or advancelogging == None:
            log_channel1 = self.client.get_channel(logchannelid)
            guild = member.guild
            guild_name = guild.name
            embed = discord.Embed(color=discord.Color.red(),title="Member Has Left")
            embed.add_field(name="Member Left:", value=f"{member.mention} has left {guild_name}", inline=False)
            embed.set_footer(text=f"Jetbot - Simple Logging System")
            await log_channel1.send(embed=embed)
        if advancelogging == True:
            memberlogchan = self.client.get_channel(memberlogid)
            guild = member.guild
            guild_name = guild.name
            embed = discord.Embed(color=discord.Color.red(), title="Member Has Left")
            embed.add_field(name="Member Left:", value=f"{member.mention} has left {guild_name}")
            embed.set_footer(text=f"Jetbot - Advanced logging System")
            await memberlogchan.send(embed=embed)


async def setup(client:commands.Bot) -> None:
  await client.add_cog(memberlog(client))