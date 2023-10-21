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
    await channel.send("Greetings!!")
    print('Message sent to the channel')

@bot.command()
async def greet_all(ctx):
    for member in ctx.guild.members:
        if not member.bot:  # To ensure you don't send messages to other bots
            
            if member.name == 'ibuprofen':
                await ctx.send(f"You are stinky {member.name} ")
            elif member.name == 'haruuuuu.':
                await ctx.send(f"No greeting for {member.name}")
            elif member.name == 'beansinjeans.':
                await ctx.send(f"Do you smell that {member.name} ?")
            elif member.name == 'ace_2001.':
                await ctx.send(f"Did you hear ibuprofen fart {member.name} ?")
            else:
                await ctx.send(f"Hello, {member.name}!")
        
    await ctx.send("All members greeted!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I'm your bot!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


### Voice Channel Logic ###
@bot.command()
async def voice_command(ctx):
    # Check if the command author is in a voice channel
    author_voice_state = ctx.author.voice

    if author_voice_state is None:
        # User is not in a voice channel
        await ctx.send(f"{ctx.author.mention}, I'm watching you")
        try:
            # Send a DM to the user
            await ctx.author.send("You aren't in a voice channel :( you forgor me")
        except discord.Forbidden:
            # If the user has DMs disabled, send a message in the server
            await ctx.send(f"{ctx.author.mention}, please enable your DMs to receive instructions.")
    else:
        # User is in a voice channel
        voice_channel = author_voice_state.channel
        # You can add your logic here to join the voice channel and run a command
        await ctx.send(f"You are in {voice_channel.name} voice channel. I can run a command here.")

token = os.getenv('DISCORD_TOKEN')
bot.run(token)
