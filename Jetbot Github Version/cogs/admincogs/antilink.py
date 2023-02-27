import re
import discord
from discord.ext import commands
from configuration import *

class AntiLink(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @commands.Cog.listener()
    async def on_message(self, message):
        adminrole = discord.utils.get(message.guild.roles, id=adminroleid)
        modrole = discord.utils.get(message.guild.roles, id=modroleid)
        if not message.author.bot and not (adminrole in message.author.roles or modrole in message.author.roles):
            match = re.search("(?P<url>https?://[^\s]+)", message.content)
            if match:
                await message.delete()
            if match and adminrole or modrole in message.author.roles:
                print("User was admin so message was not deleted")
                
async def setup(client: commands.Bot):
    await client.add_cog(AntiLink(client))
