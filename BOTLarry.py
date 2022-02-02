from asyncio.windows_events import NULL
import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()

# Use your own tokens
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD = os.getenv('DISCORD_GUILD')

mapPool = [
    'dust2',
    'mirage',
    'inferno',
    'overpass',
    'vertigo',
    'nuke',
    'ancient'
]

def mapQuote(map):
    quoteList = [
        f'Kör {map}! Vi vinner alltid när vi kör {map}.',
        f'Det kanske är dags för en {map}?',
        f'Jolle blir alltid så glad när vi lirar {map}:hearts:',
        (
        f'Kör {map}! Vi vinner aldrig när vi kör {map}'
        '... Men vi kör den ändå!'
        ),
        (
        f'Kan vi inte bara ta en {map}? Känns som '
        ' det var längesen.'
        )
    ]
    return random.choice(quoteList)


client = discord.Client()

def getCorrectResponse(content):
    msg = content.lower()
    if 'telefon' in msg or 'mobil' in msg:
        return "Aa fan att tekniken alltid ska strula asså!"
    elif msg == '!karta':
        return mapQuote(random.choice(mapPool))

    else:
        return NULL # No specific response needed


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
    # Dont talk to yourself silly Larry
    if message.author == client.user:
        return
    
    # Provide appropriate response if needed
    response = getCorrectResponse(message.content)

    if response:
        await textChannel.send(getCorrectResponse(message.content))

    

client.run(DISCORD_TOKEN)