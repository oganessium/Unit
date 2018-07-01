import discord
import asyncio
from discord.ext import commands
import requests
import json
from PIL import Image, ImageFilter
import urllib
import urllib.request
import time
import numpy as np
import random
from random import randint
import math
import html

class coolM(object):
	def __init__(self, bot):
		self.bot = bot
	@commands.command(pass_context=True)
	async def reverse(self, ctx, *, arg):
		if "enoyreve@" in arg:
			arg=arg.replace("enoyreve@", "enoyreve ")
		if "ereh@" in arg:
			arg=arg.replace("ereh@", "ereh ")
		await self.bot.say("```" + arg[::-1] + "```")

	@commands.command(pass_context=True)
	async def urban(self, ctx, *, arg):
		embed = discord.Embed(title=arg)
		embed.set_footer(text="{} | Using Urban Dictionary API v0".format(arg))
		
		definition = requests.get("http://api.urbandictionary.com/v0/define?term=" + arg).json()["list"][0]["definition"]
		example = requests.get("http://api.urbandictionary.com/v0/define?term=" + arg).json()["list"][0]["example"]
		
		embed.add_field(name="Definition", value="{}".format(definition))
		embed.add_field(name="Example", value="{}".format(example))
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/logopedia/images/a/a7/UDAppIcon.jpg/revision/latest?cb=20170422211150")
		await self.bot.say(embed=embed)
		
	@commands.command(pass_context=True)
	async def dictionary(self, ctx, *, arg):
		with open('dictionary.json') as defos:
			embed = discord.Embed()
			arg = arg.lower()
			definition=json.load(defos)[arg]
			embed.add_field(name="{}".format(arg), value="{}".format(definition))
			embed.set_thumbnail(url="https://www.collinsdictionary.com/images/thumb/dictionary_168552845_250.jpg?version=3.1.158")
			await self.bot.say(embed=embed)
			
	@commands.command(pass_context=True)
	async def img(self, ctx, effect, arg):
		urllib.request.urlretrieve(arg,'img.jpg')
		im = Image.open('img.jpg')
		im_sharp = eval("im.filter(ImageFilter." + effect.upper() + ")")
		im_sharp.save('img.jpg','JPEG')
		im_sharp.save('imgnew.jpg','JPEG')
		with open('img.jpg', 'rb') as f:
			await self.bot.send_file(ctx.message.channel, f)
			
	@commands.command(pass_context=True)
	async def grayscale(self, ctx, arg):
		urllib.request.urlretrieve(arg,'img.jpg')
		im = Image.open('img.jpg','r')
		im_gs = im.convert('L')
		theboys=np.asarray(im_gs.getdata(),dtype=np.float64)
		theboys=theboys.reshape((im_gs.size[1],im_gs.size[0]))
		theboys=np.asarray(theboys,dtype=np.uint8)
		finalimg=Image.fromarray(theboys,mode='L')
		finalimg.save('img.jpg','JPEG')
		with open('img.jpg', 'rb') as f:
			await self.bot.send_file(ctx.message.channel, f)
			
	@img.error
	async def img_error(self, error, ctx):
		if isinstance(error, AttributeError):
			await self.bot.say('**Error:** Invalid Attribute used!')
		if isinstance(error, discord.ext.commands.MissingRequiredArgument):
			await self.bot.say('**Error:** Argument missing. Please specify Filter, then URL.')
		
	@commands.command(pass_context=True)
	async def doggo(self, ctx):
		dgo = discord.Embed(title="Doggo for you")
		req = requests.get("https://random.dog/woof.json").json()["url"]
		while True:
			if ".mp4" in req:
				req = requests.get("https://random.dog/woof.json").json()["url"]
			else:
				break
		print(req)
		dgo.set_image(url=req)
		dgo.set_footer(text="Puppers provided by random.dog")
		await self.bot.say(embed=dgo)
		
	@commands.command(pass_context=True)
	async def cat(self, ctx):
		dgo = discord.Embed(title="meow")
		dgo.set_footer(text="Cats provided by shibe.online")
		req = requests.get("http://shibe.online/api/cats?count=[1-100]&urls=[true/false]&httpsUrls=[true/false]").json()[0]
		print(req)
		dgo.set_image(url=req)
		await self.bot.say(embed=dgo)
		
	@commands.command(pass_context=True)
	async def duck(self, ctx):
		dgo = discord.Embed(title="quack")
		dgo.set_footer(text="Ducks from https://duckgroup.xyz")
		url="https://duckgroup.xyz/img/imagebot/duck/{}.jpg".format(randint(1,114))
		print(url)
		dgo.set_image(url=url)
		await self.bot.say(embed=dgo)
		
	@commands.command(pass_context=True)
	async def bird(self, ctx):
		dgo = discord.Embed(title="Random birb")
		dgo.set_footer(text="Birds provided by shibe.online")
		req = requests.get("http://shibe.online/api/birds?count=[1-100]&urls=[true/false]&httpsUrls=[true/false]").json()[0]
		print(req)
		dgo.set_image(url=req)
		await self.bot.say(embed=dgo)
		
	@commands.command(pass_context=True)
	async def shibe(self, ctx):
		dgo = discord.Embed(title="Shibe for you")
		dgo.set_footer(text="Shibes provided by shibe.online")
		req = requests.get("http://shibe.online/api/shibes?count=[1-100]&urls=[true/false]&httpsUrls=[true/false]").json()[0]
		print(req)
		dgo.set_image(url=req)
		await self.bot.say(embed=dgo)
		
	@commands.command(pass_context=True)
	async def fox(self, ctx):
		dgo = discord.Embed(title="Fox")
		dgo.set_footer(text="Foxes provided by randomfox.ca")
		req = requests.get("https://randomfox.ca/floof/").json()["image"]
		print(req)
		dgo.set_image(url=req)
		await self.bot.say(embed=dgo)
		
	@commands.command(pass_context=True)
	async def fortune(self, ctx):
		embed=discord.Embed(title="Fortune Cookie")
		cookie = requests.get("http://fortunecookieapi.herokuapp.com/v1/cookie").json()
		
		embed.set_thumbnail(url="https://images-na.ssl-images-amazon.com/images/I/81TTG8pX%2BtS._SL1416_.jpg")
		embed.add_field(name="Fortune", value="{}".format(cookie[0]["fortune"]["message"]))
		embed.add_field(name="Lesson", value="{0} ({1}) | {2}".format(cookie[0]["lesson"]["chinese"],cookie[0]["lesson"]["pronunciation"],cookie[0]["lesson"]["english"]))
		embed.add_field(name="Lucky Numbers", value="{0},{1},{2},{3},{4},{5}".format(cookie[0]["lotto"]["numbers"][0],cookie[0]["lotto"]["numbers"][1],cookie[0]["lotto"]["numbers"][2],cookie[0]["lotto"]["numbers"][3],cookie[0]["lotto"]["numbers"][4],cookie[0]["lotto"]["numbers"][5]))
		await self.bot.say(embed=embed)
		
	@commands.command(pass_context=True)
	async def redpanda(self, ctx):
		dgo = discord.Embed(title="b")
		dgo.set_footer(text="Red Pandas provided by Some Random API")
		req = requests.get("https://some-random-api.glitch.me/redpandaimg").json()["link"]
		print(req)
		dgo.set_image(url=req)
		await self.bot.say(embed=dgo)
		
	@commands.command(pass_context=True)
	async def weather(self, ctx, *, arg):
		metric = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX".format(arg)).json()
		imperial = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX".format(arg)).json()
		if metric["cod"]=="404":
			await self.bot.say("Location data not found!")
		else:	
			hd="E"
			vd="N"
			embed = discord.Embed(title="Weather for the city {0}, {1}".format(metric["name"],metric["sys"]["country"]))
			if metric["coord"]["lon"] < 0:
				hd="W"
			if metric["coord"]["lat"] < 0:
				vd="S"
			embed.add_field(name="Coordinates", value="{0}°{1}, {2}°{3}".format(abs(metric["coord"]["lat"]),vd,abs(metric["coord"]["lon"]),hd))
			embed.add_field(name="Temperature", value="{0}°F, {1}°C".format(imperial["main"]["temp"],metric["main"]["temp"]))
			embed.add_field(name="Weather", value="{0} ({1})".format(metric["weather"][0]["main"],metric["weather"][0]["description"]))
			embed.add_field(name="Humidity", value="{0}%".format(metric["main"]["humidity"]))
			embed.add_field(name="Wind Speed", value="{0}mph, {1}m/s\n{2}°".format(imperial["wind"]["speed"],metric["wind"]["speed"],metric["wind"]["deg"]))
			embed.set_thumbnail(url="http://openweathermap.org/img/w/{}.png".format(metric["weather"][0]["icon"]))
			embed.set_footer(text="Weather data from OpenWeatherMap, apiKey used.")
			await self.bot.say(embed=embed)
		
	@commands.command(pass_context=True)
	async def catfact(self, ctx):
		thumb = requests.get("http://shibe.online/api/cats?count=[1-100]&urls=[true/false]&httpsUrls=[true/false]").json()[0]
		req = requests.get("https://catfact.ninja/facts").json()["data"][0]
		dgo = discord.Embed(title="Cat fact", description=req["fact"])
		dgo.set_footer(text="Cat Facts from catfact.ninja")
		dgo.set_thumbnail(url=thumb)
		await self.bot.say(embed=dgo)
		
	@commands.command(pass_context=True)
	async def dogfact(self, ctx):
		thumb = requests.get("https://random.dog/woof.json").json()["url"]
		while True:
			if ".mp4" in thumb:
				thumb = requests.get("https://random.dog/woof.json").json()["url"]
			else:
				break
		req = requests.get("https://api-to.get-a.life/dogfact").json()
		dgo = discord.Embed(title="Dog fact", description=req["fact"])
		dgo.set_footer(text="Dog Facts from api-to.get-a.life")
		dgo.set_thumbnail(url=thumb)
		await self.bot.say(embed=dgo)
		
	@commands.command(pass_context=True)
	async def catinfo(self, ctx, *, arg):
		in_api=0
		jdata = requests.get("https://catfact.ninja/breeds").json()
		for i in jdata['data']:
			if i['breed'] == arg:
				in_api=1
				embed=discord.Embed(title="Cat Info")
				embed.set_footer(text="Cat Info from catfact.ninja")
				embed.add_field(name="Native Country", value="{}".format(i['country']))
				embed.add_field(name="Origin", value="{}".format(i['origin']))
				embed.add_field(name="Coat Length", value="{}".format(i['coat']))
				embed.add_field(name="Coat Pattern", value="{}".format(i['pattern']))
				await self.bot.say(embed=embed)
				break
		if(in_api==0):
			await self.bot.say('There is no info about this cat!')
	@commands.command(pass_context=True)
	async def ping(self, ctx):
		tmee = time.monotonic()
		msgping = await self.bot.say("pinging...")
		getping = "%.2f" % (1000*(time.monotonic()-tmee))
		await self.bot.edit_message(msgping, "**Pong!** ({}ms)".format(getping))
		
	@commands.command(pass_context=True)
	async def h3lix(self, ctx):
		await self.bot.say('jansjdjemejwoe')
		
	@commands.command(pass_context=True)
	async def say(self, ctx, *, arg):
		if "@everyone" in arg:
			arg=arg.replace("@everyone", " everyone")
		if "@here" in arg:
			arg=arg.replace("@here", " here")
		await self.bot.say(arg)
		
	@commands.command(pass_context=True)
	async def avatar(self, ctx, *, arg:str=None):
		if arg == None:
			avatar = 'https://discordapp.com/api/users/{0.id}/avatars/{0.avatar}.jpg'.format(ctx.message.author)
			await self.bot.say(avatar)
		elif len(ctx.message.mentions):
			avatar = 'https://discordapp.com/api/users/{0.id}/avatars/{0.avatar}.jpg'.format(ctx.message.mentions[0])
			await self.bot.say(avatar)
		else:
			await bot.say('Invalid Input: please specify a user or do not specify for yourself')

	@commands.command(pass_context=True)
	async def innuendo(self, ctx):
		with open('unitquotes.json') as fw:
			jdata = json.load(fw)
			quote = jdata[randint(0,7)]
			await self.bot.say(quote)
	
	@commands.command(pass_context=True)
	async def wojak(self, ctx, args):
		argInt = int(args)
		if(argInt<1 or argInt>53):
			await self.bot.say("invalid input, specify number 1-53")
		else:
			dgo = discord.Embed(title="zoop :point_left: :sunglasses: :point_left:")
			dgo.set_footer(text="API by Yak#7474, Wojaks mostly from boards.4chan.org/pol/. (Wojak #{})".format(str(argInt)))
			req = requests.get("https://raw.githubusercontent.com/oganessium/oganessium.github.io/master/wojaks/wojak.json").json()[argInt-1]
			print(req)
			dgo.set_image(url=req)
			await self.bot.say(embed=dgo)
		
	@wojak.error
	async def wojak_error(self, error, ctx):
		wjk = discord.Embed(title="zoop :point_left: :sunglasses: :point_left:")
		ttt=randint(0,52)
		wjk.set_footer(text="API by Yak#7474, Wojaks mostly from boards.4chan.org/pol/. (Wojak #{})".format(str(ttt+1)))
		req = requests.get("https://raw.githubusercontent.com/oganessium/oganessium.github.io/master/wojaks/wojak.json").json()
		print(req[ttt])
		wjk.set_image(url=req[ttt])
		await self.bot.say(embed=wjk)
		
	@commands.command(pass_context=True)
	async def tcancel(self, ctx):
		print("A trivia game has been cancelled!")
		
	@commands.command(pass_context=True)
	async def trivia(self, ctx, *, arg=None):
		
		answers = []
	
		embed = discord.Embed(title="Trivia")
		if arg==None:
			req = requests.get("https://opentdb.com/api.php?amount=1").json()["results"][0]
		else:
			alert = await self.bot.say("Searching for category...")
			req = requests.get("https://opentdb.com/api.php?amount=1").json()["results"][0]
			i=0
			while i < 25:
				req = requests.get("https://opentdb.com/api.php?amount=1").json()["results"][0]
				i = i + 1
				print(i)
				if req['category']==arg:
					await self.bot.delete_message(alert)
					break
			if i>=24:
				await self.bot.edit_message(alert, new_content="Category not found, giving standard trivia question.")
				
			
		
		ques = req["question"]
		ques = html.unescape(ques)
		
		embed.add_field(name="Question", value="{}".format(ques))
		embed.add_field(name="Difficulty", value="{}".format(req["difficulty"]))
		embed.add_field(name="Category", value="{}".format(req["category"]))
		embed.set_thumbnail(url="https://pixel.nymag.com/imgs/daily/selectall/2018/01/05/05-encounter-scott-rogowsky.nocrop.w710.h2147483647.jpg")
		embed.set_footer(text="{}'s Question (respond with answer, type u;tcancel to cancel game)".format(ctx.message.author))
		
		if req["type"]=="multiple":
			answers.append(req["correct_answer"] + "")
			answers.append(req["incorrect_answers"][0])
			answers.append(req["incorrect_answers"][1])
			answers.append(req["incorrect_answers"][2])
			random.shuffle(answers)
			embed.add_field(inline=False, name="Options", value="(1) {0}\n(2) {1}\n(3) {2}\n(4) {3}".format(answers[0],answers[1],answers[2],answers[3]))
		if req["type"]=="boolean":
			answers.append(req["correct_answer"] + "")
			answers.append(req["incorrect_answers"][0])
			embed.add_field(inline=False, name="Options", value=req["correct_answer"] + "\n" + req["incorrect_answers"][0])
			
		
		tca = req["correct_answer"].lower()
		
		if tca.endswith(" "):
			tca=tca[:-1]
			
		
		
		trivia = await self.bot.say(embed=embed)
		channel = ctx.message.channel
		dd = await self.bot.wait_for_message(timeout=10, author=ctx.message.author)
		if(dd==None):
			await self.bot.say("Time up! The answer was **{}**!".format(req["correct_answer"]))
		elif(dd.content=="u;tcancel"):
			await self.bot.say("Trivia game cancelled.")
		elif "u;" in dd.content and dd.content != "u;tcancel":
			await self.bot.say("**Trivia game automatically cancelled due to new command.**")
		else:
			print(dd)
			if dd.content.lower()==tca or dd.content.lower()==str(answers.index(req["correct_answer"])+1):
				addwin = open("data\\triviadubs.txt", "r")
				wins = addwin.read()
				addwin.close()
				addwin = open("data\\triviadubs.txt", "w")
				wins = str(int(wins) + 1)
				addwin.write(wins)
				addwin.close()
				
				await self.bot.say("Correct! Good job! You are winner number {}.".format(wins))
			else:
				await self.bot.say("Oof, wrong answer. The correct answer was: **{}**!".format(req["correct_answer"]))
			
			
			
		
def setup(bot):
	bot.add_cog(coolM(bot))