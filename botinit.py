import discord
from discord.ext import commands

# Create an instance of the bot
# bot = commands.Bot(command_prefix="!")  # Change the prefix as needed
# Specify intents
intents = discord.Intents.all()  # This requests all available events
# If you only need certain events, you can modify this. For example:
# intents = discord.Intents(messages=True, guilds=True) 

# Create an instance of the bot with intents
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I'm your bot!")

token = 'MTE2NTM1MzE4ODU4MTQ0MTYwNg.G2fW0a.RkfgOBvwUU-x-cIRCQxaPkImmi7q8ivMAt32CM'
bot.run(token)
