import discord
from discord.ext import commands, tasks
import requests
import json
client = discord.Client()

# load variables from an external config file, for easy user customization and security
from json import load
from pathlib import Path
with Path("config.json").open() as f:
        config = load(f)
token = config["token"]
autoscrape=config["autoscrape"]
time=config["autoscrape_time_minutes"]
autoscrape_channel = config["autoscrape_channel_ID"]

###
# determine which currency the user wants to auto-scrape and how often
if autoscrape == "eth":
    auto = 1
    print(f"Autoscraping ethereum every {time} minutes")
elif autoscrape == "btc":
    auto = 0
    print(f"Autoscraping bitcoin every {time} minutes")
elif autoscrape == "doge":
    auto = 7
    print(f"Autoscraping dogecoin every {time} minutes")
else:
    auto = 1
    print("Autoscrape not configured properly - defaulting to ethereum. Enter eth, btc, or doge in config.json")

bot = commands.Bot(command_prefix="!", case_insensitive=True)
###

###
# show user which bot is logged in (to verify/troubleshoot token)
@bot.event
async def on_ready():
   print(bot.user, 'ready')
###

###
# loops a get request and parse json per config file, then send data to channel per config file
@tasks.loop(minutes=time)
async def send():

    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
    request = requests.get(url)
    data = request.json()
    price = data[auto]['current_price'] # pull data from json https://dev.to/mikeywastaken/discord-py-project-3-random-dog-pics-3b4a
    id = data[auto]['id']
    channel = bot.get_channel(autoscrape_channel)
    await channel.send(f'{id}: ${price}')     # https://stackoverflow.com/questions/64587136/discord-py-typeerror-send-takes-from-1-to-2-positional-arguments-but-3-were-g

@send.before_loop
async def before():
    await bot.wait_until_ready()

send.start()
###

###
# manual command for price updates
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
###

bot.run(token)