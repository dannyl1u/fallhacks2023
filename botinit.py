import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
# Create an instance of the bot
# bot = commands.Bot(command_prefix="!")  # Change the prefix as needed
# Specify intents
intents = discord.Intents.all()  # This requests all available events
# If you only need certain events, you can modify this. For example:
# intents = discord.Intents(messages=True, guilds=True) 

# Create an instance of the bot with intents
bot = commands.Bot(command_prefix="!", intents=intents)
load_dotenv()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    channel = bot.get_channel(1162235364719722610)  # Replace YOUR_CHANNEL_ID with the actual channel ID you copied.
    # await channel.send("Fuck u, pardeep 🖕!")
    print('Message sent to the channel')

@bot.command()
async def greet_all(ctx):
    for member in ctx.guild.members:
        if not member.bot:  # To ensure you don't send messages to other bots
            
            if member.name == 'ibuprofen':
                await ctx.send(f"Fuck u {member.name} 🖕")
            elif member.name == 'haruuuuu.':
                await ctx.send(f"No greeting for {member.name}")
            else:
                await ctx.send(f"Hello, {member.name}!")
        
    await ctx.send("All members greeted!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I'm your bot!")

token = os.getenv('DISCORD_TOKEN')
bot.run(token)
