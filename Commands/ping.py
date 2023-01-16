from discord.client import Client




def ping(client : Client):
    return round(client.latency * 1000, 2)