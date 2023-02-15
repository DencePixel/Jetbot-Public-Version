import discord
from discord.ext import commands
from discord import app_commands
import discord.ext
from discord import Color
from configuration import *

class ban(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client
    @client.command(name="ban")
    async def ban(ctx, member: discord.Member,*,reason=None):
        adminrole = discord.utils.get(ctx.guild.roles,id=adminroleid)
        if adminrole in ctx.author.roles:
            if reason == None:
                if banmessage == True:
                    reason = f"{banmessage} {ctx.author}"
                if banmessage == False:
                    reason = f"No reason was provided and default message module is off."


            embed = discord.Embed(color=discord.Color.blurple(), title=f"User Banned - {member}")
            embed.add_field(name="Offender:", value=f"{member}")
            embed.add_field(name="Moderator:", value=f"{ctx.author.mention}")
            embed.add_field(name="Reason", value=f"{reason}")
            await member.ban(reason=reason)
            await ctx.reply(embed=embed)
            await channel.send(f"You have been banned by {ctx.author.mention} in {ctx.guild.name} for ``{reason}")
            
        if adminrole not in ctx.author.roles:
            await ctx.respond("Insufficent permissions")


async def setup(client:commands.Bot) -> None:
  await client.add_cog(ban(client))