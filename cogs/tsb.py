import discord
import asyncio
from discord.ext import commands
import datetime
from datetime import date, tzinfo, timedelta, datetime, timezone
import random
from random import randint

class tsbM():
	def __init__(self, bot):
		self.bot = bot

		
	@commands.command(pass_context=True)
	async def timesince(self, ctx, arg):
		timestamp=datetime.utcfromtimestamp(1526305073)
		now = datetime.now()
		print (now.year, now.month, now.day, now.hour, now.minute, now.second)
		yearsec = now.year * 31557600
		yess = now.year
		monthsec = now.month * 2678400
		daysec = (now.day - 1) * 86400
		hoursec = now.hour * 3600
		minutesec = now.minute * 60
		secondsec = now.second
		hihiv = int(arg)
		newysec = hihiv * 31557600
		timd = (yearsec + monthsec + daysec + hoursec + minutesec + secondsec) - newysec
		print(timd)
		await self.bot.say('Seconds since %s: %s' % (arg, timd))

	@commands.command(pass_context=True)
	async def timeuntil(self, ctx, arg):
		timestamp=datetime.utcfromtimestamp(1526305073)
		now = datetime.now()
		print (now.year, now.month, now.day, now.hour, now.minute, now.second)
		yearsec = now.year * 31557600
		yess = now.year
		monthsec = now.month * 2678400
		daysec = (now.day - 1) * 86400
		hoursec = now.hour * 3600
		minutesec = now.minute * 60
		secondsec = now.second
		hihiv = int(arg)
		newysec = hihiv * 31557600
		timd = ((yearsec + monthsec + daysec + hoursec + minutesec + secondsec) - newysec) * -1
		print(timd)
		await self.bot.say('Seconds until %s: %s' % (arg, timd))
		
	@commands.command(pass_context=True)
	async def randomtime(self, ctx, timet):
			a = int(timet)
			c = randint(0,5)
			if c == 0:
				d="years"
			elif c == 1:
				d="months"
			elif c == 2:
				d="days"
			elif c == 3:
				d="hours"
			elif c == 4:
				d="minutes"
			else:
				d="seconds"
			e=randint(0,a)
			await self.bot.say('%s %s' % (e,d)) 

def setup(bot):
	bot.add_cog(tsbM(bot))