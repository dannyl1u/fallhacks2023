import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

background_tasks = {}

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

token = os.getenv('DISCORD_TOKEN')
bot.run(token)
