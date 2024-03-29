#from asyncio.windows_events import NULL
import os
import discord
import random
from dotenv import load_dotenv
from crosshairgenerator import getCrosshair

load_dotenv()

# Use your own tokens
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

# No shitty maps allowed
mapPool = [
    'dust2',
    'mirage',
    'inferno',
    'overpass',
    'vertigo',
    'nuke',
    'ancient',
    'anubis'
]

# Get some classic larry quotes from text file
def getQuote():
    quotes = open('quotes.txt', 'r', encoding = 'utf8')
    lines = quotes.readlines()
    quote = str(random.choice(lines))
    return quote

# Try to add new quote to list
def addQuote(quote):
    nWords = len(quote.split());

    # Add quote if message contains more than just !citat
    if(nWords > 1):
        try:
            oldQuotes = open('quotes.txt', 'r', encoding = 'utf8')
            lines = oldQuotes.readlines()
            oldQuotes.close()
            
            # Remove !citat
            quote = quote.split(' ', 1)[1]

            # Add to a new line
            lines.append(f'\n{quote}')

            # Convert from list to single string
            newText = "".join(lines)

            newQuotes = open('quotes.txt', 'w', encoding = 'utf8')
            print("Writing")
            newQuotes.write(newText)
            newQuotes.close()
            return True;
        except:
            print("Quote could not be added.")
            return False;


# Spice up the chosen map message for the given map
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
        f'Kan vi inte bara ta en {map}? Känns som'
        ' det var längesen.'
        )
    ]
    return random.choice(quoteList)

@client.event
async def getCorrectResponse(content):
    msg = content.lower()
    firstWord = msg.split()[0]

    if firstWord == '!citat':
        success = addQuote(content)
        if success:
            return 'Kunde inte ha sagt det bättre själv! Det ska jag komma ihåg.'
        else:
            return 'Sådär skulle jag aldrig säga!'
    elif msg == '!larry':
        print("larry")
        return getQuote()
    elif 'telefon' in msg or 'mobil' in msg:
        return 'Aa fan att tekniken alltid ska strula asså!'
    elif msg == '!karta':
        return mapQuote(random.choice(mapPool))
    elif firstWord == '!crosshair':
        return getCrosshair(content)
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

    #await textChannel.send("Sorry att jag försvann lite! Måste ha råkat stoppa tån i eluttaget igen :grimacing:")

@client.event
async def on_message(message):
    print(message.author.name)
    # Dont talk to yourself silly Larry
    if message.author == client.user:
        return

    activeTextChannel = discord.utils.get(message.guild.text_channels, name="general")

    # Provide appropriate response if needed
    response = await getCorrectResponse(message.content)
    if response:
        await activeTextChannel.send(response)

client.run(DISCORD_TOKEN)
