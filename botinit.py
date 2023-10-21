import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
import re

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
async def youtube(ctx, youtube_url: str):
    try:
        video_id=""
        pattern = r"v=([^&]+)"
        match = re.search(pattern, youtube_url)
        if match:
            video_id = match.group(1)
        else:
            pattern = r"(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))([\w-]{11})"
            match = re.search(pattern, video_id)
            if match:
                video_id = match.group(1)
            else:
                print("Video ID not found.")
            print("Video ID not found.")
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = "\n".join([entry['text'] for entry in transcript])

        # Split the message if it's too long for a single Discord message
        for i in range(0, len(transcript_text), 2000):
            await ctx.send(transcript_text[i:i+2000])
            # await ctx.send(transcript_text[i:i+2000])
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.event
async def on_message(message):
    # This ensures that the bot does not reply to itself or other bots
    if message.author.bot:
        return

    # Check if the message author is ibuprofen
    if message.author.name == 'ibuprofen':
        await message.channel.send("Fuck u parddeep")

    # Important: to ensure that the bot still processes commands
    await bot.process_commands(message)

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

