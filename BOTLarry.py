import os
import discord
from dotenv import load_dotenv

load_dotenv()

# Use your own tokens
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    global guild
    global textChannel
    
    for guild in client.guilds:
        if guild.name == DISCORD_GUILD:
            break

    print(f'{client.user} have joined {guild.name}!')

    textChannel = discord.utils.get(guild.text_channels, name="general")
    print("Active in channel: ", textChannel.name)

    await textChannel.send("Sorry att jag försvann lite! Måste ha råkat stoppa tån i eluttaget igen :grimacing:")

client.run(DISCORD_TOKEN)