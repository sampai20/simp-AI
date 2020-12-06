from discord.ext import commands
import discord
import urllib
from bs4 import BeautifulSoup
import requests

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


class Ranks(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.camel_rank = get_rank("camellCase#NA1")

	@commands.command()
	async def camel(self, ctx):
		cur_rank = get_rank("camellCase#NA1")
		await ctx.send(get_rank("camellCase#NA1"))
		if cur_rank != self.camel_rank and cur_rank != "bad":
			await ctx.send("<@&781636133762629632>, camel rank has changed to " + cur_rank + "!")
			self.camel_rank = cur_rank

	@commands.command()
	async def rank(self, ctx):
		await ctx.send(get_rank(ctx.message.content[6:]))

	@commands.command()
	async def userrank(self, ctx, member: discord.Member):
		tagcog = self.bot.get_cog("Tags")
		usertag = tagcog.get_tag(str(member))
		if usertag == "bad":
			await ctx.send("Tag not set for that user.")
		else:
			await ctx.send(get_rank(usertag))

def setup(bot):
	bot.add_cog(Ranks(bot))


