# LeafMeAlone

## Introduction:
Our project, inspired by the theme "uncovering a new leaf" 🍃, presents a Discord bot designed to usher in a fresh approach to studying. Recognizing the challenges that students and learners face in managing their time, sourcing study materials, and retaining information, we have integrated features such as Pomodoro timers, YouTube video audio streaming for educational content, text-to-speech functionality, and reminder systems. By simply using commands prefixed with '!', users can revamp their study habits, and turn over a new leaf in their academic journey 📚.

## Features:

### 1. Pomodoro Timer:
   - Use the bot for effective time management by setting study and break intervals.
   - Command: `!pomodoro <study_time> <break_time>` to start the timer (`<study_time>` and `<break_time>` are in minutes)
   - Stop the timer anytime with `!stop`.
   

### 2. YouTube Video Summarizer:
   - YouTube videos are a great way to turn over a new leaf by learning a new skill, get a concise summary of a YouTube video by providing its link.
   - Using OpenAI's API and YouTube Transcript API, the bot summarizes the video and sends it to the user.
   - Command: `!youtube <youtube_url>`.

### 3. Voice Channel Audio Playback (WIP):
   - The bot can join a voice channel and play audio from a YouTube video.
   - Commands: `!join` to join a voice channel, and `!playaudio <youtube_url>` to play the YouTube video's audio.

### 4. Reminders:
   - Cultivate your memory by sowing tasks and nurturing their growth until the deadline 🍂
   - Commands: `!remind <task_name> <duration_in_seconds>` to set a reminder.
   - complete a task using `!completeTask <task-code>`

   ```
   !remind leetcode 900 // set task leetcode due in 15 minutes
   !tasks // list out tasks and their task-code
   !completeTask leetcode-##### // mark task as completed
   !cancel leetcode-##### // cancel task
   ```


### 5. Greet All Members:
   - A fun command that greets all members in a guild with customized greetings for specific members.
   - Command: `!greet_all`.

... and many more to come!

## Installation and Setup:

### Create a Bot on Discord Developer Portal

Go to the [Discord Developer Portal](https://discord.com/developers/applications). <br>

1. Click **New Application** <br> 
2. Name your bot and Click **Create** <br>
3. Go to **OAuth2/General**, set Authorization Method to **In-app Authorization**, scope to **Administrator**
4. Go to **OAuth2/URL Generator**, set scope to **bot**, bot permission to **Administrator**, and copy generated URL
5. Go to **Bot**, click **Reset Token**and Copy the bot token

### Run the Discord Bot
1. Clone this repository.
2. Install the required packages using pip: `pip install -r requirements.txt`.
3. Set up your `.env` file with the necessary tokens (e.g., `DISCORD_TOKEN` and `OPENAI_API_KEY`).
4. Run the bot script: `python botinit.py`.

### File Structure
- botinit.py 
- readme.md 
- requirements.txt

### Participants Name and Contact Information
- Danny Liu, dla216@sfu.ca
- Pardeep Bhattal, psbhatta@sfu.ca
- Amy Cao, caoamyc@sfu.ca
- Jenna Han, jha336@sfu.ca
- Abishek Tharmapala, atharmap@sfu.ca

## Acknowledgements

- All modules and libraries can be seen in the requirements.txt file
- Open AI Chat GPT3.5 was used for debugging code errors in the botinit.py file

## Contribution:
Feel free to fork this repository, add your own features, and create a pull request. We're always open to improvements and new features!

