import discord
import requests
import os
import urllib
from bs4 import BeautifulSoup

token = os.getenv("simp_AI")

def get_rank(name):
	url = "https://tracker.gg/valorant/profile/riot/" + urllib.parse.quote(name) + "/overview?playlist=competitive"
	req = requests.get(url)
	soup = BeautifulSoup(req.content, "html.parser")
	ans = ""
	try:
		ans = soup.find_all("span", class_="valorant-highlighted-stat__value")[0].text
	except:
		ans = "bad"
	return ans


client = discord.Client()
camel_rank = get_rank("camellCase#NA1")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$camel'):
    	cur_rank = get_rank("camellCase#NA1")
    	await message.channel.send(get_rank("camellCase#NA1"))
    	if cur_rank != camel_rank:
    		await message.channel.send("<@&781636133762629632>, camel rank has changed to " + cur_rank + "!")
    		camel_rank = cur_rank
        

    elif message.content.startswith('$rank'):
    	await message.channel.send(get_rank(message.content[6:]))
