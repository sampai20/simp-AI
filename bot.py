import discord
from discord.ext import commands
import requests
import os
import urllib
from bs4 import BeautifulSoup

bot = commands.Bot(command_prefix="$")

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

@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def camel(ctx):
	global camel_rank
	cur_rank = get_rank("camellCase#NA1")
	await ctx.send(get_rank("camellCase#NA1"))
	if cur_rank != camel_rank and cur_rank != "bad":
		await ctx.send("<@&781636133762629632>, camel rank has changed to " + cur_rank + "!")
		camel_rank = cur_rank

@bot.command()
async def rank(ctx):
	await ctx.send(get_rank(ctx.message.content[6:]))

token = os.getenv("simp_AI")
camel_rank = get_rank("camellCase#NA1")
bot.run(token)