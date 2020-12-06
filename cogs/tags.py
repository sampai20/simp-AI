from discord.ext import commands
import discord
import os
import psycopg2
import urllib.parse as urlparse

class Tags(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		DATABASE_URL = os.environ['DATABASE_URL']
		self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		self.cursor = self.conn.cursor()
		self.cursor.execute("""
			CREATE TABLE IF NOT EXISTS tags (
				discord_tag varchar,
				val_tag varchar
			);
		""")

	def get_tag(self, name):
		self.cursor.execute("""
			SELECT * from tags WHERE discord_tag = %s;
		""", (name,))

		res = self.cursor.fetchall()
		if len(res) == 0:
			return "bad"
		else:
			return res[0][1]

	def set_tag(self, name, vtag):
		if self.get_tag(name) == "bad":
			self.cursor.execute("""
				INSERT INTO tags VALUES (%s, %s);
			""", (name, vtag,))
		else:
			self.cursor.execute("""
				UPDATE tags SET val_tag = %s WHERE discord_tag = %s;
			""", (vtag, name,))
		self.conn.commit()

	@commands.command()
	async def settag(self, ctx, *, arg):
		self.set_tag(str(ctx.message.author), arg)
		await ctx.send("Tag for {0.mention} set to {1}!".format(ctx.message.author, arg))

	@commands.command()
	async def gettag(self, ctx, member: discord.Member):
		name = str(member)
		tag = self.get_tag(name)
		if tag == "bad":
			await ctx.send("Tag not set.")
		else:
			await ctx.send(tag)

def setup(bot):
	bot.add_cog(Tags(bot))
