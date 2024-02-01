import os
import datetime
import asyncio
from keep_alive import keep_alive
import discord
import random
import openai
import math
import pytz

api_token = os.environ['GPTTOKEN']
openai.api_key = api_token
model = 'gpt-3.5-turbo-instruct'

voicelines = ["Playtime is over.","Is that all you have?","I expected more from you.","Do you actually think you can defeat me?",	"Poor performance indeed.","You disappoint me. Is that the best you've got?","Too bad you won't make it much further.",	"You've really become quite an inconvenience for me.","This isn't over, Chris.","Seven minutes is all I can spare to play with you.","I'll see you dead!","I'm just getting started.","I tire of wasting my time with you.","You will not live to see the dawn!","I expected more of a challenge.","Farewell, old friend!","Your feeble attempts only delay the inevitable.",	"There's no point in hiding.","You can't hide forever!",	"Let's finish this.","Time to die, Chris.","You'll pay for that!","Just accept your fate.","You're merely postponing the inevitable!","Are you trying to make me angry?","I shall release Uroboros!"]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

async def send_image():
  now = datetime.datetime.now(pytz.timezone('US/Eastern'))
  print(now.weekday())
  print(now.hour)
  
  if now.weekday() == 2 and now.hour == 0:
    message_content = "https://cdn.discordapp.com/attachments/716485327652388874/1136380494800506991/IMG_9542.png"
    channel = client.get_channel(int(os.environ['Channel_ID']))
    await channel.send(message_content)
    await asyncio.sleep(86400)

@client.event
async def on_message(message):
  if message.content == "!voiceline":
    await message.channel.send(random.choice(voicelines))
  if client.user.mentioned_in(message) and message.author != client.user:
    print(message.content)
    splitString = message.content.split()
    if len(splitString) > 1:
      # If there are more than one word, exclude the first word
      promptAddon = ' '.join(splitString[1:])
    else:
      promptAddon = 'Hello'  # If there's only one word, the result will be an empty string
    prompt = "Respond to this message as if you are Albert Wesker from Resident Evil: " + promptAddon
    print(prompt)
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=300  # Adjust as needed
    )
    await message.channel.send(response.choices[0].text)

@client.event
async def on_ready():
  print("We have logged in as " + str(client.user))
  client.loop.create_task(schedule_image())

async def schedule_image():
  while not client.is_closed():
    await send_image()
    await asyncio.sleep(60)

# Run the bot
keep_alive()
client.run(os.environ['TOKEN'])