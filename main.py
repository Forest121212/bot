import discord
import random
import os

# List of characters with the last name Kong
kong_characters = [
    "Donkey Kong",
    "Diddy Kong",
    "Dixie Kong",
    "Kiddy Kong",
    "Chunky Kong",
    "Lanky Kong",
    "Tiny Kong",
    "Cranky Kong",
    "Funky Kong",
    "Wrinkly Kong",
    "Swanky Kong",
    "Candy Kong"
]

# Your bot's token from the environment variable
TOKEN = os.getenv('DISCORD_TOKEN')

# Ensure the token is correctly read
if TOKEN is None:
    raise ValueError("No token found. Please set the DISCORD_TOKEN environment variable.")

# Create an instance of the client
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    print(f'Received message: "{message.content}" from {message.author}')  # Debugging statement

    # Ignore messages from the client itself
    if message.author == client.user:
        print('Ignored own message')
        return

    # Check if the message starts with '!kong'
    if message.content.startswith('!kong'):
        print('Command recognized')  # Debugging statement
        # Get a random Kong character and send it as a response
        character = random.choice(kong_characters)
        await message.channel.send(character)
        print(f'Sent message: "{character}"')  # Debugging statement
    else:
        print('Command not recognized')  # Debugging statement

# Run the client
client.run(TOKEN)
