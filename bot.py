import discord
import requests
import os
from bs4 import BeautifulSoup

token = os.getenv("simp_AI")

def get_rank(name):
	url = "https://tracker.gg/valorant/profile/riot/" + name.replace("#", "%23") + "/overview?playlist=competitive"
	req = requests.get(url)
	soup = BeautifulSoup(req.content, "html.parser")
	ans = ""
	try:
		ans = soup.find_all("span", class_="valorant-highlighted-stat__value")[0].text
	except:
		ans = "bad"
	return ans

def get_camel_rank():
	url = "https://tracker.gg/valorant/profile/riot/camellCase%23NA1/overview?playlist=competitive"
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
        await message.channel.send(get_rank("camellCase#NA1"))

    elif message.content.startswith('$rank'):
    	await message.channel.send(get_rank(message.content[6:]))

client.run(token)