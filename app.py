from datetime import datetime as dt
import Commands

import discord
import json
import logging


config = json.load(open('Config/config.json'))

TOKEN = config["token"]
PREFIX = config["prefix"]

intents = discord.Intents.default()
client = discord.Client(intents=intents)


# Set up logging
logger = logging.getLogger('Discord Bot Logger')
logger.setLevel(10)
now = dt.now()
today_logs = f'{now.day}-{now.month}-{now.year}.txt'
fh = logging.FileHandler(f'Logs/{today_logs}')
logger.addHandler(fh)

def get_time():
    now = dt.now()
    return f'{now.hour}:{now.minute}:{now.second}'


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    logger.debug(f'[{get_time()}] Logged in as {client.user}')

@client.event
async def on_message(message : discord.message.Message):
    if message.author == client.user or not message.content.startswith(PREFIX):
        return
    
    command = message.content[1:] # 1 - len(message.content)
    if command == 'ping':
        ping = Commands.ping(client)
        await message.channel.send(f'Ping: {ping}ms')
    
    if command == 'coin':
        await message.channel.send(Commands.coin())
    
    logger.debug(f'{get_time()} Command {command} ran by {message.author}')

client.run(TOKEN)