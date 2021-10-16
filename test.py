import discord
from discord import all
from discord.guild import Guild
import requests, json
from datetime import datetime
import pytz
from ischedule import schedule, run_loop
api_key = "1de69ed610001a9ef4621bc227b0c1f5"
full_url = "http://api.openweathermap.org/data/2.5/weather?appid=1de69ed610001a9ef4621bc227b0c1f5&q=montreal"
response = requests.get(full_url)
x = response.json()
z = x["weather"]
weather_description = z[0]["description"]
def check_weather():
      full_url = "http://api.openweathermap.org/data/2.5/weather?appid=1de69ed610001a9ef4621bc227b0c1f5&q=montreal"
      response = requests.get(full_url)
      x = response.json()
      z = x["weather"]
      weather_description = z[0]["description"]
      print(weather_description)
client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def nickname():
      await Guild.get_member(898999660683853905)
client.run('ODk4OTk5NjYwNjgzODUzOTA1.YWsYrQ.HHTuH9-m8YTn62534yV14a8BQd8')
schedule(check_weather, interval=3600.0)
run_loop()