import discord
from discord import *
import logging

#--- Important ---#
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w') #--- Logs errors in discord.log file. DO NOT DELETE AT ANY COSTS. ---#
Intents = discord.Intents.all()
client = discord.Client(intents=Intents)
bot_prefix = ";"
token="0"
announce_url = "0"

#--- Tables ---#
rizzer = ["Rizz God", "1000 Rizz", "The Rizzer", "No Rizz", "Negative Rizz","Wizard Of Rizz","Unwanted Rizz"]

#----------------------------#

#--- Staff Permissions ---#
modroleid = 0 #--- Can use all staff commands except ban ---#
adminroleid = 0 #--- Can use every single command in the server ---#

#----------------------------#

#--- Channels ---#
suggestchannelid = 0 #--- Set 0 to the channel where all suggestions will be sent to ---#
welcomechannelid = 0 #--- Set 0 to the channel where all welcome messages will be sent to ---#

#----------------------------#

#--- Default Messages ---#
defaultbanmessage = None #--- Set to True or false if you want their to be a default reason message referenced below if no reason was provided for the ban ---#
defualtkickmessage = None  #--- Set to True or false if you want their to be a default reason message referenced below if no reason was provided for the kick ---#

kickmessage = "Jetbot | No Reason Given | Kicked | " #--- This message will be displayed in the audit logs if a staff member does not give a reason when kicking someone ---#
banmessage = "Jetbot | No Reason Given | Banned| " #--- This message will be displayed in the audit logs if a staff member does not give a reason when banning someone ---#

#----------------------------#

#--- Logging Config ---#
advancelogging = None

# Logging Channel Simple #
logchannelid = 0 #--- Set 0 to your channel id where everything will be logged ---#

# Logging Channel Advanced # | ALL OF THESE ID'S MUST BE SET TO A CHANNEL IF ADVANCEDLOGGING IS TRUE | #
rolelogid = 0 #--- Only change this if advancedlogging is set to true. If it is then change the 0 to your channel where you want to log all role changes
channellogid = 0 #--- Only change this if advancedlogging is set to true. If it is then change the 0 to your channel where you want to log all channel changes
memberlogid = 0 #--- Only change this if advancedlogging is set to true. If it is then change the 0 to your channel where you want to log all member changes

#----------------------------#
