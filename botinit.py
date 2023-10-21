import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
import re


intents = discord.Intents.all()  # This requests all available events
# If you only need certain events, you can modify this. For example:
# intents = discord.Intents(messages=True, guilds=True) 

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

@bot.command()
async def greet_all(ctx):
    for member in ctx.guild.members:
        if not member.bot:  # To ensure you don't send messages to other bots
            if member.name == 'ibuprofen':
                await ctx.send(f"Hello {member.name} 🖕")
            elif member.name == 'haruuuuu.':
                await ctx.send(f"No greeting for {member.name}")
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
async def hello(ctx):
    await ctx.send("Hello, I'm your bot!")

token = os.getenv('DISCORD_TOKEN')
bot.run(token)

