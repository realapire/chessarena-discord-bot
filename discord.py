import discord, os, requests, json
from discord.ext import commands
from datetime import datetime

url = 'https://adventure.chessarena.io/api/leaderboard_history?period=weekly&limit=10&count=1'

headers = {
  'ggjoin-app': 'battlechess',
  'content': 'application/json'
}

json_data = requests.get(url, headers=headers).json()
scores = json_data['leaderboards'][0]['scores']

counter = 0
for i in scores:
  counter+=1
  print(counter, i['nickname'],'/' ,i['nickname_tag'], ' score:', int(i['score']), 'checkmates', i['data']['checkmates'])
  

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)

now = datetime.now()
current_time = now.strftime("%H:%M")

now = datetime.now()
current_time = now.strftime("%H:%M")

@client.event
async def on_member_join(member):
    await member.send(f"Welcome to our Discord Server. Please take a look at this server https://discord.gg/3JDUUsvv")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1

    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=f'{members} members'))


@client.command()
async def top10(ctx):
  message = []
  url = 'https://adventure.chessarena.io/api/leaderboard_history?period=weekly&limit=10&count=1'
  json_data = requests.get(url, headers=headers).json()
  scores = json_data['leaderboards'][0]['scores']
  
  counter = 0
  for i in scores:
    counter+=1
    #print(counter, i['nickname'],'/' ,i['nickname_tag'], ' score:', int(i['score']), 'checkmates',           i['data']['checkmates'])
    message.append(f"**Rank**: {counter} **Player**: {i['nickname']}""#"f"{i['nickname_tag']} **Score**:{int(i['score'])} **Checkmates**: {i['data']['checkmates']}")
    
  await ctx.send('\n'.join(message))





my_secret = os.environ['TOKEN']
client.run(my_secret)
