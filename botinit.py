import asyncio
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from helper import generate_task_code
import youtube_dl


from youtube_transcript_api import YouTubeTranscriptApi
import re


from pydub import AudioSegment

import pygame
background_tasks = {}

# Create an instance of the bot
# bot = commands.Bot(command_prefix="!")  # Change the prefix as needed
# Specify intents
intents = discord.Intents.all()  # This requests all available events
# If you only need certain events, you can modify this. For example:
# intents = discord.Intents(messages=True, guilds=True) 
audioSong = "audio\\Frog.mp3"
# Create an instance of the bot with intents
bot = commands.Bot(command_prefix="!", intents=intents)
load_dotenv()

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
#     channel = bot.get_channel(1162235364719722610)  # Replace YOUR_CHANNEL_ID with the actual channel ID you copied.
#     print('Message sent to the channel')

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
        pass

    # Important: to ensure that the bot still processes commands
    await bot.process_commands(message)
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
                pass
            elif member.name == 'haruuuuu.':
                await ctx.send(f"No greeting for {member.name}")
            elif member.name == 'beansinjeans.':
                await ctx.send(f"Do you smell that {member.name} ?")
            elif member.name == 'ace_2001.':
                await ctx.send(f"Did you hear ibuprofen fart {member.name} ?")
            else:
                await ctx.send(f"Hello, {member.name}!")
        
@bot.command()
async def dayOne(ctx):
    message = """
**Customer Obsession**
Leaders start with the customer and work backwards. They work vigorously to earn and keep customer trust. Although leaders pay attention to competitors, they obsess over customers.

**Ownership**
Leaders are owners. They think long term and don’t sacrifice long-term value for short-term results. They act on behalf of the entire company, beyond just their own team. They never say “that’s not my job.”

**Invent and Simplify**
Leaders expect and require innovation and invention from their teams and always find ways to simplify. They are externally aware, look for new ideas from everywhere, and are not limited by “not invented here.” As we do new things, we accept that we may be misunderstood for long periods of time.

**Are Right, A Lot**
Leaders are right a lot. They have strong judgment and good instincts. They seek diverse perspectives and work to disconfirm their beliefs.

**Learn and Be Curious**
Leaders are never done learning and always seek to improve themselves. They are curious about new possibilities and act to explore them.

**Hire and Develop the Best**
Leaders raise the performance bar with every hire and promotion. They recognize exceptional talent, and willingly move them throughout the organization. Leaders develop leaders and take seriously their role in coaching others. We work on behalf of our people to invent mechanisms for development like Career Choice.

**Insist on the Highest Standards**
Leaders have relentlessly high standards — many people may think these standards are unreasonably high. Leaders are continually raising the bar and drive their teams to deliver high quality products, services, and processes. Leaders ensure that defects do not get sent down the line and that problems are fixed so they stay fixed.

**Think Big**
Thinking small is a self-fulfilling prophecy. Leaders create and communicate a bold direction that inspires results. They think differently and look around corners for ways to serve customers.

**Bias for Action**
Speed matters in business. Many decisions and actions are reversible and do not need extensive study. We value calculated risk taking.

**Frugality**
Accomplish more with less. Constraints breed resourcefulness, self-sufficiency, and invention. There are no extra points for growing headcount, budget size, or fixed expense.

**Earn Trust**
Leaders listen attentively, speak candidly, and treat others respectfully. They are vocally self-critical, even when doing so is awkward or embarrassing. Leaders do not believe their or their team’s body odor smells of perfume. They benchmark themselves and their teams against the best.

**Dive Deep**
Leaders operate at all levels, stay connected to the details, audit frequently, and are skeptical when metrics and anecdote differ. No task is beneath them.

**Have Backbone; Disagree and Commit**
Leaders are obligated to respectfully challenge decisions when they disagree, even when doing so is uncomfortable or exhausting. Leaders have conviction and are tenacious. They do not compromise for the sake of social cohesion. Once a decision is determined, they commit wholly.

**Deliver Results**
Leaders focus on the key inputs for their business and deliver them with the right quality and in a timely fashion. Despite setbacks, they rise to the occasion and never settle.

**Strive to be Earth’s Best Employer**
Leaders work every day to create a safer, more productive, higher performing, more diverse, and more just work environment. They lead with empathy, have fun at work, and make it easy for others to have fun. Leaders ask themselves: Are my fellow employees growing? Are they empowered? Are they ready for what’s next? Leaders have a vision for and commitment to their employees’ personal success, whether that be at Amazon or elsewhere.

**Success and Scale Bring Broad Responsibility**
We started in a garage, but we’re not there anymore. We are big, we impact the world, and we are far from perfect. We must be humble and thoughtful about even the secondary effects of our actions. Our local communities, planet, and future generations need us to be better every day. We must begin each day with a determination to make better, do better, and be better for our customers, our employees, our partners, and the world at large. And we must end every day knowing we can do even more tomorrow. Leaders create more than they consume and always leave things better than how they found them.
"""
    while message:
        chunk, message = message[:2000], message[2000:]
        await ctx.send(chunk)

@bot.command()
async def play(ctx, filename):
    # Check if the user is in a voice channel
    if ctx.author.voice and ctx.author.voice.channel:
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()

        try:
            audio = AudioSegment.from_mp3(filename)  # Load the MP3 file
            audio.export("temp.wav", format="wav")  # Convert to WAV

            voice_client.play(discord.FFmpegPCMAudio("temp.wav"))

            while voice_client.is_playing():
                await asyncio.sleep(1)

            await voice_client.disconnect()
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")
    else:
        await ctx.send("You need to be in a voice channel to use this command.")

@bot.command()
async def join(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()
        await ctx.send(f'Joined {voice_channel}')
        
@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I'm your bot!")




async def remind_countdown(ctx, task_code, seconds):
    
    await ctx.send("sleeping for {seconds} seconds...")
    await asyncio.sleep(seconds)
    
    # TODO: add annoyances here. When we reach this part of the code, it means the user did not finish the task in time
    
    # To prevent keeping references to finished tasks forever,
    # make each task remove its own reference from the dictionary after
    background_tasks[task_code].add_done_callback(background_tasks.pop(task_code))
    await ctx.send(f"{task_code} Failed to complete!")
    
@bot.command()
async def cancel(ctx, task_code):
    background_tasks[task_code].cancel()
    background_tasks.pop(task_code)
    await ctx.send(f"cancelled {task_code}")

@bot.command()
async def completeTask(ctx, task_code):
    if task_code in background_tasks:
        background_tasks[task_code].cancel()
        background_tasks.pop(task_code)
        await ctx.send(f"Congratulations, {ctx.author.name}! You have completed {task_code}!")
    else:
        await ctx.send(f"{task_code} is not in the list of tasks")

@bot.command()
async def tasks(ctx):
    await ctx.send("listing tasks...")
    for task in background_tasks.keys():
        await ctx.send(task)

@bot.command()
async def remind(ctx, task='leetcode',seconds=10):
    task_code = task+"-"+str(generate_task_code())
    await ctx.send(f"Activated reminder for {task_code}!")
    
    _task = asyncio.create_task(remind_countdown(ctx, task_code, seconds))

    background_tasks[task_code] = _task
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

### Voice Channel Logic ###
@bot.command()
async def pom_event(ctx):
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
        # bot join
        if ctx.author.voice and ctx.author.voice.channel:
            voice_channel = ctx.author.voice.channel
            voice_client = await voice_channel.connect()
            await ctx.send(f'Joined {voice_channel}')
            vid = "https://www.youtube.com/watch?v=Pv1QnqHvlg0&ab_channel=Airixs"
            await ctx.invoke(bot.get_command("playaudio"), vid)
        
@bot.command()
async def pom_timer(ctx, minutes):
    try:
        minutes = int(minutes)
    except ValueError:
        await ctx.send("Invalid input. Please provide a valid number of minutes.")
        return

    await ctx.send(f"Pomodoro timer started for {minutes} minutes. Work hard!")

    # Wait for the specified number of minutes
    await asyncio.sleep(minutes * 60)

    # After the specified time, send a message to notify the user
    await ctx.invoke(bot.get_command("pom_event"))

@bot.command()
async def playaudio(ctx, youtube_url): # play youtube video audio
    if ctx.author.voice and ctx.author.voice.channel:
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()
        await ctx.send(f'Joined {voice_channel}')

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            url2 = info['formats'][0]['url']

        voice_client.play(discord.FFmpegPCMAudio(url2))
        while voice_client.is_playing():
            await asyncio.sleep(1)
        await voice_client.disconnect()
    else:
        await ctx.send("You need to be in a voice channel to use this command.")


token = os.getenv('DISCORD_TOKEN')
bot.run(token)

