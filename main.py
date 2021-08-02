import discord
from discord.ext import commands, tasks
import requests
import json
client = discord.Client()

# load from an external config file, for easier customization and security
from json import load
from pathlib import Path
with Path("config.json").open() as f:
        config = load(f)
token = config["token"]
time=config["autoscrape_time_minutes"]
autoscrape_channel = config["autoscrape_channel_ID"]

bot = commands.Bot(command_prefix="!", case_insensitive=True)

@bot.event
async def on_ready():
   print("Bot Ready")

###
@tasks.loop(minutes=time)
async def send():

    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
    request = requests.get(url)
    data = request.json()
    price = data[1]['current_price'] # Pull from json https://dev.to/mikeywastaken/discord-py-project-3-random-dog-pics-3b4a
    id = data[1]['id']
    channel = bot.get_channel(autoscrape_channel)
    await channel.send(f'{id}: ${price}')     # https://stackoverflow.com/questions/64587136/discord-py-typeerror-send-takes-from-1-to-2-positional-arguments-but-3-were-g

@send.before_loop
async def before():
    await bot.wait_until_ready()

send.start()

###

@bot.command()
async def eth(ctx):

    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
    request = requests.get(url)
    data = request.json()
    price = data[1]['current_price']
    id = data[1]['id']
    await ctx.channel.send(f'{id}: ${price}')

@bot.command()
async def btc(ctx):

    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
    request = requests.get(url)
    data = request.json()
    price = data[0]['current_price']
    id = data[0]['id']
    await ctx.channel.send(f'{id}: ${price}')

@bot.command()
async def doge(ctx):

    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
    request = requests.get(url)
    data = request.json()
    price = data[7]['current_price']
    id = data[7]['id']
    await ctx.channel.send(f'{id}: ${price}')

bot.run(token)