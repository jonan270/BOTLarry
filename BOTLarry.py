import os
import discord
from dotenv import load_dotenv

load_dotenv()

# Use your own tokens
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

def getCorrectResponse(content):
    if 'telefon' in content.lower() or 'mobil' in content.lower():
        return "Aa fan att tekniken alltid ska strula asså!"
    else:
        return "" # No specific response needed


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

@client.event
async def on_message(message):
    print("In")
    # Dont talk to yourself silly Larry
    if message.author == client.user:
        return
    
    # Provide appropriate response if needed
    response = getCorrectResponse(message.content)
    if response != "":
        await textChannel.send(getCorrectResponse(message.content))

    

client.run(DISCORD_TOKEN)