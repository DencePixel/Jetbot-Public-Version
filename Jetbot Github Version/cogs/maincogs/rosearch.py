import discord
from discord.ext import commands
from discord import app_commands
import discord.ext
from discord import Color
import json
import requests

class rosearch(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client
    @client.command(name="rosearch")
    async def rosearch(ctx, username : str):
        carros_json=requests.get(f"https://api.roblox.com/users/get-by-username?username={username}")
        carros=json.loads(carros_json.text)
        test = (carros["Id"])
        #image
        #display
        displayname2=requests.get(f"https://users.roblox.com/v1/users/{test}")
        displayname3=json.loads(displayname2.text)
        displayname4 = (displayname3["displayName"])
        #created
        date1=requests.get(f"https://users.roblox.com/v1/users/{test}")
        date2=json.loads(date1.text)
        date3 = (date2["created"])
        #image
        im1=requests.get(f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={test}&size=100x100&format=Png&isCircular=false")
        im2=json.loads(im1.text)
        im3 = (im2['data'][0]['imageUrl'])
        #description
        desc1=requests.get(f"https://users.roblox.com/v1/users/{test}")
        desc2=json.loads(desc1.text)
        desc3 = (desc2["description"])

        embed=discord.Embed(title=f"Roblox Search - {username}", url=f"https://www.roblox.com/users/{test}/profile", color=discord.Color.blurple())
        embed.set_footer(text=f"Roblox Search - Jetbot")
        embed.add_field(name="Username", value=f"{username}", inline=False)
        embed.add_field(name="ID", value=f"{test}", inline=False)
        embed.add_field(name="Display Name", value=f"{displayname4}", inline=True)
        embed.add_field(name="Created", value=f"{date3}", inline=False)
        embed.add_field(name="Description", value=f"{desc3}", inline=True)
        embed.set_thumbnail(url=f"{im3}")
        await ctx.send(embed=embed)


async def setup(client:commands.Bot) -> None:
  await client.add_cog(rosearch(client))