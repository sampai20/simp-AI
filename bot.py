import discord
import requests
from bs4 import BeautifulSoup
from config import token

def get_camel_rank():
	url = "https://tracker.gg/valorant/profile/riot/camellCase%23NA1/overview"
	req = requests.get(url)
	soup = BeautifulSoup(req.content, "html.parser")
	return soup.find_all("span", class_="valorant-highlighted-stat__value")[0].text




client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$camel'):
        await message.channel.send(get_camel_rank())


client.run(token)