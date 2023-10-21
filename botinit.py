import discord
from discord.ext import commands

# Create an instance of the bot
bot = commands.Bot(command_prefix="!")  # Change the prefix as needed

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I'm your bot!")

# Replace 'YOUR_TOKEN' with the actual bot token you copied from the Discord Developer Portal
bot.run('YOUR_TOKEN')
