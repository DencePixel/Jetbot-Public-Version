import discord
from discord.ext import commands
from discord import app_commands
import discord.ext
from discord import Color
from configuration import *

class kick(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client
    @client.command(name="kick")
    async def kick(ctx, member: discord.Member,*,reason=None):
        modrole = discord.utils.get(ctx.guild.roles,id=modroleid)
        if member == ctx.author:
            await ctx.reply("You cannot kick yourself.")

        if member == client:
            await ctx.reply("I cannot kick myself.")

        if modrole in ctx.author.roles:
            if reason == None:
                if defualtkickmessage == True:
                    reason = f"{kickmessage} {ctx.author}"
                if defualtkickmessage == False:
                    reason = f"No reason was provided and default message module is off."

            embed = discord.Embed(color=discord.Color.blurple(), title=f"User Kicked - {member}")
            embed.add_field(name="Offender:", value=f"{member}")
            embed.add_field(name="Moderator:", value=f"{ctx.author.mention}")
            embed.add_field(name="Reason", value=f"{reason}")
            await member.kick(reason=reason)
            await ctx.reply(embed=embed)
            
        if modrole not in ctx.author.roles:
            await ctx.reply("Insufficent Role")


        





async def setup(client:commands.Bot) -> None:
  await client.add_cog(kick(client))