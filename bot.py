import discord
from discord.ext import commands
import os


bot = commands.Bot(command_prefix="$")
bot.load_extension('cogs.ranks')


@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))


token = os.getenv("simp_AI")
bot.run(token)