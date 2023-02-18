import discord
from token.py import token

intents = discord.Intents.default()
intents.members = True  # Enable the privileged members intent

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        await message.channel.send('Hello!')

client.run(token)
