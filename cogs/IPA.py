import discord
from discord.ext import commands
import asyncio
import platform
import datetime
import random
from random import randint
from datetime import date, tzinfo, timedelta, datetime, timezone
import time
import json

class IPAm(object):
	def __init__(self, bot):
		self.bot = bot
	@commands.command(pass_context=True)
	async def eval(self, ctx, *, arg11):
		eval(arg11)

	@commands.command(pass_context=True)
	async def ipa(self, ctx, *, arg):
		ag = arg.lower()
		print('Got command IPA')
		print('Got jailbreak ' + (ag))
		print('-------------------------------')
		if ag == "liberios" :
			await self.bot.say('http://newosxbook.com/liberios/')
		elif ag == "electra" :
			await self.bot.say('https://coolstar.org/electra/')
		elif ag == "phoenix" :
			await self.bot.say('https://phoenixpwn.com/')
		elif ag == "goblin" :
			await self.bot.say('https://g0blin.sticktron.net/')
		elif ag == "g0blin" :
			await self.bot.say('https://g0blin.sticktron.net/')
		elif ag == "doubleh3lix" :
			await self.bot.say('https://doubleh3lix.tihmstar.net/')
		elif ag == "h3lix" :
			await self.bot.say('https://h3lix.tihmstar.net/')
		elif ag == "helix" :
			await self.bot.say('https://h3lix.tihmstar.net/')
		elif ag == "etasonjb" :
			await self.bot.say('https://etasonjb.tihmstar.net/')
		elif ag == "etason" :
			await self.bot.say('https://etasonjb.tihmstar.net/')
		elif ag == "etas0n" :
			await self.bot.say('https://etasonjb.tihmstar.net/')
		elif ag == "etas0njb" :
			await self.bot.say('https://etasonjb.tihmstar.net/')
		elif ag == "yalu" :
			await self.bot.say('https://yalu.qwertyoruiop.com/')
		elif ag == "extra_recipe" :
			await self.bot.say('https://yalu.qwertyoruiop.com/')
		elif ag == "extra_recipe" :
			await self.bot.say('https://yalu.qwertyoruiop.com/')
		elif ag == "home depot" :
			await self.bot.say('http://wall.supplies/')
		elif ag == "home depot 8.4.1" :
			await self.bot.say('http://wall.supplies/OLD%20iPhone%20HACKED.html')
		elif ag == "pangu" :
			await self.bot.say('http://en.pangu.io/')
		elif ag == "meridian" :
			await self.bot.say('https://meridian.sparkes.zone/')
		elif ag == "cydeload" :
			await self.bot.say('https://yakz.cf/ios/Cydeload_Alpha-2.1.ipa')
		elif ag == "c0f3" :
			await self.bot.say('https://iabem97.github.io/saigon_website/')
		elif ag == "yalu 8.4.1" :
			await self.bot.say('https://github.com/DylbinHax/yalu841')
		elif ag == "yalu841" :
			await self.bot.say('https://github.com/DylbinHax/yalu841')
		elif ag == "yalu 841" :
			await self.bot.say('https://github.com/DylbinHax/yalu841')
		elif ag == "absinthe" :
			await self.bot.say('https://mega.nz/#F!OrI3CDaB!bpEcHoXXL7ASajFaFb7OTQ')
		elif ag == "1.1.1" :
			await self.bot.say('https://mega.nz/#F!m65HQDIY!56und99LOzEmzR6DbUxdPQ')
		elif ag == "24kpwn" :
			await self.bot.say('https://mega.nz/#F!PmIAQRwJ!kopiw0m3ZXLaniCoVxcwBw')
		elif ag == "blackra1n" :
			await self.bot.say('https://mega.nz/#F!rr5kTL5a!no6WrFO7_yWdUb4x_LA9RQ')
		elif ag == "evasi0n6" :
			await self.bot.say('https://mega.nz/#F!j2AXTQ6Q!ZpFGUkSPUBUG9UTpPIDJhg')
		elif ag == "evasi0n7" :
			await self.bot.say('https://mega.nz/#F!7rw1ATLb!kngG_RRJ3FCHvE5JK3hwAA')
		elif ag == "evasi0n" :
			await self.bot.say('Error: specify `evasi0n6` or `evasi0n7`')
		elif ag == "geeksn0w" :
			await self.bot.say('https://mega.nz/#F!evYXgTgL!1zW5XjVb2qlZIoCAlGGYvQ')
		elif ag == "greeng0blin" :
			await self.bot.say('https://nito.tv/')
		elif ag == "houdini" :
			await self.bot.say('https://iabem97.github.io/houdini_website/')
		elif ag == "torngat" :
			await self.bot.say('https://1gamerdev.github.io/Torngat/')
		elif ag == "ibrickr" :
			await self.bot.say('https://mega.nz/#F!Py5gXLwK!gRC03OKhyzACZRu0ZD6JUw')
		elif ag == "libertv" :
			await self.bot.say('http://newosxbook.com/libertv/')
		elif ag == "idevicererestore" :
			await self.bot.say('https://downgrade.party/')
		elif ag == "futurerestore" :
			await self.bot.say('https://github.com/tihmstar/futurerestore/releases')
		elif ag == "limera1n" :
			await self.bot.say('http://limera1n.com/')
		elif ag == "blackra1n" :
			await self.bot.say('http://blackra1n.com/')
		elif ag == "nitotv" :
			await self.bot.say('https://nito.tv/')
		elif ag == "p0sixspwn" :
			await self.bot.say('https://mega.nz/#F!WjhEUbxb!baJ59QNui6Wc9X28wY1hsw')
		elif ag == "pangu7" :
			await self.bot.say('http://en.7.pangu.io/')
		elif ag == "pangu8" :
			await self.bot.say('https://mega.nz/#F!a7xxxCCZ!L8pdrbt0-MsoqnFdWLJVKg')
		elif ag == "pangu9" :
			await self.bot.say('http://web.archive.org/web/20170803101455/http://en.9.pangu.io:80/')
		elif ag == "seas0npass" :
			await self.bot.say('https://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "taig" :
			await self.bot.say('http://taig.com/')
		elif ag == "to.panga" :
			await self.bot.say('https://github.com/iabem97/topanga')
		elif ag == "topanga" :
			await self.bot.say('https://github.com/iabem97/topanga')
		elif ag == "redsn0w" :
			await self.bot.say('https://mega.nz/#F!D6ZDzTrS!SA0sqIS-0vPuq0yi1SIVgw')
		elif ag == "greenpoison" :
			await self.bot.say('https://mega.nz/#F!7qJkESyJ!0fPBTozkiwWUAiM8rbi9-A')
		elif ag == "greenpois0n" :
			await self.bot.say('https://mega.nz/#F!7qJkESyJ!0fPBTozkiwWUAiM8rbi9-A')
		elif ag == "osiris" :
			await self.bot.say('https://github.com/GeoSn0w/Osiris-Jailbreak')
			
		else:
			await self.bot.say('Jailbreak IPA not found!')

	@commands.command(pass_context=True)
	async def ios(self, ctx, ag):
		print('Got command IOS')
		print('Got version' + (ag))
		print('-------------------------------')
		if ag == "11.4" :
			await self.bot.say('**No jailbreak found**')
		elif ag == "11.3.1" :
			await self.bot.say('**Osiris (DEVELOPER JB UNSTABLE) **\nhttps://github.com/GeoSn0w/Osiris-Jailbreak')
		elif ag == "11.3" :
			await self.bot.say('**Osiris (DEVELOPER JB UNSTABLE) **\nhttps://github.com/GeoSn0w/Osiris-Jailbreak')
		elif ag == "11.2.5" :
			await self.bot.say('**Osiris (DEVELOPER JB UNSTABLE) **\nhttps://github.com/GeoSn0w/Osiris-Jailbreak')
		elif ag == "11.2.2" :
			await self.bot.say('**Osiris (DEVELOPER JB UNSTABLE) **\nhttps://github.com/GeoSn0w/Osiris-Jailbreak')
		elif ag == "11.2.1" :
			await self.bot.say('**Osiris (DEVELOPER JB UNSTABLE) **\nhttps://github.com/GeoSn0w/Osiris-Jailbreak')
		elif ag == "11.2" :
			await self.bot.say('**Osiris (DEVELOPER JB UNSTABLE) **\nhttps://github.com/GeoSn0w/Osiris-Jailbreak')
		elif ag == "11.1.2" :
			await self.bot.say('**Electra**\nhttps://coolstar.org/electra/')
		elif ag == "11.1.1" :
			await self.bot.say('**Electra**\nhttps://coolstar.org/electra/')
		elif ag == "11.1" :
			await self.bot.say('**Electra**\nhttps://coolstar.org/electra/')
		elif ag == "11.0.3" :
			await self.bot.say('**Electra**\nhttps://coolstar.org/electra/')
		elif ag == "11.0.2" :
			await self.bot.say('**Electra**\nhttps://coolstar.org/electra/')
		elif ag == "11.0.1" :
			await self.bot.say('**Electra**\nhttps://coolstar.org/electra/')
		elif ag == "11.0" :
			await self.bot.say('**Electra**\nhttps://coolstar.org/electra/')
		elif ag == "11" :
			await self.bot.say('**11.0-11.1.2: Electra**\nhttps://coolstar.org/electra/')
			await self.bot.say('**11.0-11.1.2: Liberios**\nhttp://newosxbook.com/liberios/')
		elif ag == "10.3.3" :
			await self.bot.say('**64 bit: DoubleH3lix**\nhttps://doubleh3lix.tihmstar.net/')
			await self.bot.say('**32 bit: H3lix**\nhttps://h3lix.tihmstar.net/')
		elif ag == "10.3.2" :
			await self.bot.say('**64 bit: DoubleH3lix**\nhttps://doubleh3lix.tihmstar.net/')
			await self.bot.say('**32 bit: H3lix**\nhttps://h3lix.tihmstar.net/')
		elif ag == "10.3.1" :
			await self.bot.say('**64 bit: DoubleH3lix**\nhttps://doubleh3lix.tihmstar.net/')
			await self.bot.say('**32 bit: H3lix**\nhttps://h3lix.tihmstar.net/')
		elif ag == "10.3" :
			await self.bot.say('**64 bit: DoubleH3lix**\nhttps://doubleh3lix.tihmstar.net/')
			await self.bot.say('**32 bit: H3lix**\nhttps://h3lix.tihmstar.net/')
		elif ag == "10.2.1" :
			await self.bot.say('**64 bit: DoubleH3lix**\nhttps://doubleh3lix.tihmstar.net/')
			await self.bot.say('**32 bit: H3lix**\nhttps://h3lix.tihmstar.net/')
		elif ag == "10.2" :
			await self.bot.say('**64 bit: DoubleH3lix**\nhttps://doubleh3lix.tihmstar.net/')
			await self.bot.say('**32 bit: H3lix**\nhttps://h3lix.tihmstar.net/')
		elif ag == "10.1.1" :
			await self.bot.say('**64 bit: DoubleH3lix**\nhttps://doubleh3lix.tihmstar.net/')
			await self.bot.say('**32 bit: H3lix**\nhttps://h3lix.tihmstar.net/')
		elif ag == "10.1" :
			await self.bot.say('**64 bit: DoubleH3lix**\nhttps://doubleh3lix.tihmstar.net/')
			await self.bot.say('**32 bit: H3lix**\nhttps://h3lix.tihmstar.net/')
		elif ag == "10.0.2" :
			await self.bot.say('**64 bit: DoubleH3lix**\nhttps://doubleh3lix.tihmstar.net/')
			await self.bot.say('**32 bit: H3lix**\nhttps://h3lix.tihmstar.net/')
		elif ag == "10.0.1" :
			await self.bot.say('**64 bit: DoubleH3lix**\nhttps://doubleh3lix.tihmstar.net/')
			await self.bot.say('**32 bit: H3lix**\nhttps://h3lix.tihmstar.net/')
		elif ag == "10.0" :
			await self.bot.say('**64 bit: DoubleH3lix**\nhttps://doubleh3lix.tihmstar.net/')
			await self.bot.say('**32 bit: H3lix**\nhttps://h3lix.tihmstar.net/')
		elif ag == "10" :
			await self.bot.say('**64 bit: DoubleH3lix**\nhttps://doubleh3lix.tihmstar.net/')
			await self.bot.say('**32 bit: H3lix**\nhttps://h3lix.tihmstar.net/')
		elif ag == "9.3.5" :
			await self.bot.say('**64 bit: No Jailbreak Found**')
			await self.bot.say('**32 bit: Phoenix**\nhttps://phoenixpwn.com/')
		elif ag == "9.3.4" :
			await self.bot.say('**64 bit: No Jailbreak Found**')
			await self.bot.say('**32 bit: Home Depot**\nhttp://wall.supplies/')
		elif ag == "9.3.3" :
			await self.bot.say('**64 bit: Pangu**\nhttp://en.pangu.io')
			await self.bot.say('**32 bit: Home Depot**\nhttp://wall.supplies/')
		elif ag == "9.3.2" :
			await self.bot.say('**64 bit: Pangu**\nhttp://en.pangu.io')
			await self.bot.say('**32 bit: Home Depot**\nhttp://wall.supplies/')
		elif ag == "9.3.1" :
			await self.bot.say('**64 bit: Pangu**\nhttp://en.pangu.io')
			await self.bot.say('**32 bit: Home Depot**\nhttp://wall.supplies/')
		elif ag == "9.3" :
			await self.bot.say('**64 bit: Pangu**\nhttp://en.pangu.io')
			await self.bot.say('**32 bit: Home Depot**\nhttp://wall.supplies/')
		elif ag == "9.2.1" :
			await self.bot.say('**64 bit: Pangu**\nhttp://en.pangu.io')
			await self.bot.say('**32 bit: Home Depot**\nhttp://wall.supplies/')
		elif ag == "9.2" :
			await self.bot.say('**64 bit: Pangu**\nhttp://en.pangu.io')
			await self.bot.say('**32 bit: Home Depot**\nhttp://wall.supplies/')
		elif ag == "9.1" :
			await self.bot.say('**64 bit: Pangu**\nhttp://en.9.pangu.io')
			await self.bot.say('**32 bit: Home Depot**\nhttp://wall.supplies/')
		elif ag == "9.0.2" :
			await self.bot.say('**Pangu**\nhttp://en.9.pangu.io')
		elif ag == "9.0.1" :
			await self.bot.say('**Pangu**\nhttp://en.9.pangu.io')
		elif ag == "9.0" :
			await self.bot.say('**Pangu**\nhttp://en.9.pangu.io')
		elif ag == "9" :
			await self.bot.say('**9.3.5 32 bit: Phoenix**\nhttps://phoenixpwn.com/')
			await self.bot.say('**9.3.4-9.3.5 64 bit: No Jailbreak Found**')
			await self.bot.say('**9.2-9.3.3 64 bit: Pangu**\nhttp://en.pangu.io')
			await self.bot.say('**9.1-9.3.4 32 bit: Home Depot**\nhttp://wall.supplies/')
			await self.bot.say('**9.0-9.0.2, 9.1 for 64 bit: Pangu**\nhttp://en.9.pangu.io')
		elif ag == "8.4.1" :
			await self.bot.say('**64 bit: No Jailbreak Found**')
			await self.bot.say('**32 bit: EtasonJB**\nhttps://etasonjb.tihmstar.net/')
			await self.bot.say('**32 bit: Home Depot**\nhttp://wall.supplies/OLD%20iPhone%20HACKED')
		elif ag == "8.4" :
			await self.bot.say('**TaiG**\nhttp://taig.com/')
		elif ag == "8.3" :
			await self.bot.say('**TaiG**\nhttp://taig.com/')
		elif ag == "8.2" :
			await self.bot.say('**TaiG**\nhttp://taig.com/')
		elif ag == "8.1.3" :
			await self.bot.say('**TaiG**\nhttp://taig.com/')
		elif ag == "8.1.2" :
			await self.bot.say('**TaiG**\nhttp://taig.com/')
		elif ag == "8.1.1" :
			await self.bot.say('**TaiG**\nhttp://taig.com/')
		elif ag == "8.1" :
			await self.bot.say('**TaiG**\nhttp://taig.com/')
		elif ag == "8.0.2" :
			await self.bot.say('**TaiG**\nhttp://taig.com/')
		elif ag == "8.0.1" :
			await self.bot.say('**TaiG**\nhttp://taig.com/')
		elif ag == "8.0" :
			await self.bot.say('**TaiG**\nhttp://taig.com/')
		elif ag == "8" :
			await self.bot.say('**8.4.1 64 bit: No Jailbreak Found**')
			await self.bot.say('**8.4.1 32 bit: EtasonJB**\nhttps://etasonjb.tihmstar.net/')
			await self.bot.say('**8.4.1 32 bit: Home Depot**\nhttp://wall.supplies/OLD%20iPhone%20HACKED')
			await self.bot.say('**8.0-8.4 TaiG**\nhttp://taig.com/')
		elif ag == "7.1.2" :
			await self.bot.say('**Pangu7**\nhttp://en.7.pangu.io/')
		elif ag == "7.1.1" :
			await self.bot.say('**Pangu7**\nhttp://en.7.pangu.io/')
		elif ag == "7.1" :
			await self.bot.say('**Pangu7**\nhttp://en.7.pangu.io/')
		elif ag == "7.0.6" :
			await self.bot.say('**Evasi0n7**\nhttps://mega.nz/#F!7rw1ATLb!kngG_RRJ3FCHvE5JK3hwAA')
		elif ag == "7.0.5" :
			await self.bot.say('**Evasi0n7**\nhttps://mega.nz/#F!7rw1ATLb!kngG_RRJ3FCHvE5JK3hwAA')
		elif ag == "7.0.4" :
			await self.bot.say('**Evasi0n7**\nhttps://mega.nz/#F!7rw1ATLb!kngG_RRJ3FCHvE5JK3hwAA')
		elif ag == "7.0.3" :
			await self.bot.say('**Evasi0n7**\nhttps://mega.nz/#F!7rw1ATLb!kngG_RRJ3FCHvE5JK3hwAA')
		elif ag == "7.0.2" :
			await self.bot.say('**Evasi0n7**\nhttps://mega.nz/#F!7rw1ATLb!kngG_RRJ3FCHvE5JK3hwAA')
		elif ag == "7.0.1" :
			await self.bot.say('**Evasi0n7**\nhttps://mega.nz/#F!7rw1ATLb!kngG_RRJ3FCHvE5JK3hwAA')
		elif ag == "7.0" :
			await self.bot.say('**Evasi0n7**\nhttps://mega.nz/#F!7rw1ATLb!kngG_RRJ3FCHvE5JK3hwAA')
		elif ag == "7" :
			await self.bot.say('**7.1-7.1.2: Pangu7**\nhttp://en.7.pangu.io/')
			await self.bot.say('**7.0-7.0.6: Evasi0n7**\nhttps://mega.nz/#F!7rw1ATLb!kngG_RRJ3FCHvE5JK3hwAA')
		elif ag == "6.1.6" :
			await self.bot.say('**p0sixspwn**\nhttps://mega.nz/#F!WjhEUbxb!baJ59QNui6Wc9X28wY1hsw')
		elif ag == "6.1.5" :
			await self.bot.say('**p0sixspwn**\nhttps://mega.nz/#F!WjhEUbxb!baJ59QNui6Wc9X28wY1hsw')
		elif ag == "6.1.4" :
			await self.bot.say('**p0sixspwn**\nhttps://mega.nz/#F!WjhEUbxb!baJ59QNui6Wc9X28wY1hsw')
		elif ag == "6.1.3" :
			await self.bot.say('**p0sixspwn**\nhttps://mega.nz/#F!WjhEUbxb!baJ59QNui6Wc9X28wY1hsw')
		elif ag == "6.1.2" :
			await self.bot.say('**evasi0n6**\nhttps://mega.nz/#F!j2AXTQ6Q!ZpFGUkSPUBUG9UTpPIDJhg')
		elif ag == "6.1.1" :
			await self.bot.say('**evasi0n6**\nhttps://mega.nz/#F!j2AXTQ6Q!ZpFGUkSPUBUG9UTpPIDJhg')
		elif ag == "6.1" :
			await self.bot.say('**evasi0n6**\nhttps://mega.nz/#F!j2AXTQ6Q!ZpFGUkSPUBUG9UTpPIDJhg')
		elif ag == "6.0.1" :
			await self.bot.say('**evasi0n6**\nhttps://mega.nz/#F!j2AXTQ6Q!ZpFGUkSPUBUG9UTpPIDJhg')
		elif ag == "6.0" :
			await self.bot.say('**evasi0n6**\nhttps://mega.nz/#F!j2AXTQ6Q!ZpFGUkSPUBUG9UTpPIDJhg')
		elif ag == "6" :
			await self.bot.say('**6.1.3-6.1.6: p0sixspwn**\nhttps://mega.nz/#F!WjhEUbxb!baJ59QNui6Wc9X28wY1hsw')
			await self.bot.say('**6.0-6.1.2: p0sixspwn**\nhttps://mega.nz/#F!j2AXTQ6Q!ZpFGUkSPUBUG9UTpPIDJhg')
		elif ag == "5.1.1" :
			await self.bot.say('**Absinthe**\nhttps://mega.nz/#!mioSxaxS!1x8FGIprCXOwmGbURvnyoPVRjT8oHHvUnPyv-T_NTJ8')
		elif ag == "5.1" :
			await self.bot.say('**redsn0w**\nhttps://mega.nz/#!C6hkxbwb!ybglu448nUW8Wk33LivnYn9HLVm0_MQSYHieGFrZi4w')
		elif ag == "5.0.1" :
			await self.bot.say('**Absinthe**\nhttps://mega.nz/#!OmAFQZTT!BOsR1fa7VBpN3pKHXwF2TYbXeFpeN-I4U9iXw-Svih4')
		elif ag == "5.0" :
			await self.bot.say('**Absinthe**\nhttps://mega.nz/#!OmAFQZTT!BOsR1fa7VBpN3pKHXwF2TYbXeFpeN-I4U9iXw-Svih4')
		elif ag == "5" :
			await self.bot.say('**5.1.1: Absinthe**\nhttps://mega.nz/#!mioSxaxS!1x8FGIprCXOwmGbURvnyoPVRjT8oHHvUnPyv-T_NTJ8')
			await self.bot.say('**5.1: redsn0w**\nhttps://mega.nz/#!C6hkxbwb!ybglu448nUW8Wk33LivnYn9HLVm0_MQSYHieGFrZi4w')
			await self.bot.say('**5.0-5.0.1: Absinthe**\nhttps://mega.nz/#!OmAFQZTT!BOsR1fa7VBpN3pKHXwF2TYbXeFpeN-I4U9iXw-Svih4')
		elif ag == "4.3.5" :
			await self.bot.say('**redsn0w**\nhttps://mega.nz/#!C6hkxbwb!ybglu448nUW8Wk33LivnYn9HLVm0_MQSYHieGFrZi4w')
		elif ag == "4.3.4" :
			await self.bot.say('**redsn0w**\nhttps://mega.nz/#!C6hkxbwb!ybglu448nUW8Wk33LivnYn9HLVm0_MQSYHieGFrZi4w')
		elif ag == "4.3.3" :
			await self.bot.say('**JailbreakMe**\nhttps://www.jailbreakme.com/')
		elif ag == "4.3.2" :
			await self.bot.say('**JailbreakMe**\nhttps://www.jailbreakme.com/')
		elif ag == "4.3.1" :
			await self.bot.say('**JailbreakMe**\nhttps://www.jailbreakme.com/')
		elif ag == "4.3" :
			await self.bot.say('**JailbreakMe**\nhttps://www.jailbreakme.com/')
		elif ag == "4.2.10" :
			await self.bot.say('**JailbreakMe**\nhttps://www.jailbreakme.com/')
		elif ag == "4.2.9" :
			await self.bot.say('**JailbreakMe**\nhttps://www.jailbreakme.com/')
		elif ag == "4.2.8" :
			await self.bot.say('**JailbreakMe**\nhttps://www.jailbreakme.com/')
		elif ag == "4.2.7" :
			await self.bot.say('**JailbreakMe**\nhttps://www.jailbreakme.com/')
		elif ag == "4.2.6" :
			await self.bot.say('**JailbreakMe**\nhttps://www.jailbreakme.com/')
		elif ag == "4.2.5" :
			await self.bot.say('**JailbreakMe Star**\nhttps://www.jailbreakme.com/star/')
		elif ag == "4.2.1" :
			await self.bot.say('**JailbreakMe Star**\nhttps://www.jailbreakme.com/star/')
		elif ag == "4.1" :
			await self.bot.say('**JailbreakMe Star**\nhttps://www.jailbreakme.com/star/')
		elif ag == "4.0.2" :
			await self.bot.say('**JailbreakMe Star**\nhttps://www.jailbreakme.com/star/')
		elif ag == "4.0.1" :
			await self.bot.say('**JailbreakMe Star**\nhttps://www.jailbreakme.com/star/')
		elif ag == "4.0" :
			await self.bot.say('**JailbreakMe Star**\nhttps://www.jailbreakme.com/star/')
		elif ag == "4" :
			await self.bot.say('**4.3.4-4.3.5: redsn0w**\nhttps://mega.nz/#!C6hkxbwb!ybglu448nUW8Wk33LivnYn9HLVm0_MQSYHieGFrZi4w')
			await self.bot.say('**4.2.6-4.3.3: JailbreakMe**\nhttps://www.jailbreakme.com/')
			await self.bot.say('**4.0-4.2.5: JailbreakMe Star**\nhttps://www.jailbreakme.com/star/')
		elif ag == "3.2.2" :
			await self.bot.say('**greenpois0n**\nhttps://mega.nz/#F!7qJkESyJ!0fPBTozkiwWUAiM8rbi9-A')
		elif ag == "3.2.1" :
			await self.bot.say('**JailbreakMe Star**\nhttps://www.jailbreakme.com/star/')
		elif ag == "3.2" :
			await self.bot.say('**JailbreakMe Star**\nhttps://www.jailbreakme.com/star/')
		elif ag == "3.1.3" :
			await self.bot.say('**JailbreakMe Star**\nhttps://www.jailbreakme.com/star/')
		elif ag == "3.1.2" :
			await self.bot.say('**JailbreakMe Star**\nhttps://www.jailbreakme.com/star/')
		elif ag == "3.1.1" :
			await self.bot.say('**blackra1n**\nhttps://mega.nz/#!vyYCxBJR!pSvS0gLlQ5LbsdpotjjntDYjn10LYSKKaIJ1dy3h2SQ')
		elif ag == "3.1" :
			await self.bot.say('**blackra1n**\nhttps://mega.nz/#!vyYCxBJR!pSvS0gLlQ5LbsdpotjjntDYjn10LYSKKaIJ1dy3h2SQ')
		elif ag == "3.0.1" :
			await self.bot.say('**redsn0w**\nhttps://mega.nz/#!72hzyaoa!VWJxjDYY8pGHBX2uTUUTvQ8JULypaqbnzfmz2I7fSEI')
		elif ag == "3.0" :
			await self.bot.say('**redsn0w**\nhttps://mega.nz/#!72hzyaoa!VWJxjDYY8pGHBX2uTUUTvQ8JULypaqbnzfmz2I7fSEI')
		elif ag == "3" :
			await self.bot.say('**3.2.2: greenpois0n**\nhttps://mega.nz/#F!7qJkESyJ!0fPBTozkiwWUAiM8rbi9-A')
			await self.bot.say('**3.1.2-3.2.1: JailbreakMe Star**\nhttps://www.jailbreakme.com/star/')
			await self.bot.say('**3.1-3.1.1: blackra1n**\nhttps://mega.nz/#!vyYCxBJR!pSvS0gLlQ5LbsdpotjjntDYjn10LYSKKaIJ1dy3h2SQ')
			await self.bot.say('**3.0: redsn0w**\nhttps://mega.nz/#!72hzyaoa!VWJxjDYY8pGHBX2uTUUTvQ8JULypaqbnzfmz2I7fSEI')
		elif ag == "2.2.1" :
			await self.bot.say('**2.x jailbreaks**\nhttps://www.theiphonewiki.com/wiki/Jailbreak#2.x')
		elif ag == "2.2" :
			await self.bot.say('**2.x jailbreaks**\nhttps://www.theiphonewiki.com/wiki/Jailbreak#2.x')
		elif ag == "2.1.1" :
			await self.bot.say('**2.x jailbreaks**\nhttps://www.theiphonewiki.com/wiki/Jailbreak#2.x')
		elif ag == "2.1" :
			await self.bot.say('**2.x jailbreaks**\nhttps://www.theiphonewiki.com/wiki/Jailbreak#2.x')
		elif ag == "2.0.2" :
			await self.bot.say('**2.x jailbreaks**\nhttps://www.theiphonewiki.com/wiki/Jailbreak#2.x')
		elif ag == "2.0.1" :
			await self.bot.say('**2.x jailbreaks**\nhttps://www.theiphonewiki.com/wiki/Jailbreak#2.x')
		elif ag == "2.0" :
			await self.bot.say('**2.x jailbreaks**\nhttps://www.theiphonewiki.com/wiki/Jailbreak#2.x')
		elif ag == "2" :
			await self.bot.say('**2.x jailbreaks**\nhttps://www.theiphonewiki.com/wiki/Jailbreak#2.x')
		elif ag == "1.1.5" :
			await self.bot.say('**1.x jailbreaks**\nhttps://www.theiphonewiki.com/wiki/Jailbreak#1.x')
		elif ag == "1.1.4" :
			await self.bot.say('**1.x jailbreaks**\nhttps://www.theiphonewiki.com/wiki/Jailbreak#1.x')
		elif ag == "1.1.3" :
			await self.bot.say('**1.x jailbreaks**\nhttps://www.theiphonewiki.com/wiki/Jailbreak#1.x')
		elif ag == "1.1.2" :
			await self.bot.say('**1.x jailbreaks**\nhttps://www.theiphonewiki.com/wiki/Jailbreak#1.x')
		elif ag == "1.1.1" :
			await self.bot.say('**1.x jailbreaks**\nhttps://www.theiphonewiki.com/wiki/Jailbreak#1.x')
		elif ag == "1.1" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "1.0.2" :
			await self.bot.say('**1.x jailbreaks**\nhttps://www.theiphonewiki.com/wiki/Jailbreak#1.x')
		elif ag == "1.0.1" :
			await self.bot.say('**1.x jailbreaks**\nhttps://www.theiphonewiki.com/wiki/Jailbreak#1.x')
		elif ag == "1.0" :
			await self.bot.say('**1.x jailbreaks**\nhttps://www.theiphonewiki.com/wiki/Jailbreak#1.x')
		elif ag == "1" :
			await self.bot.say('**1.x jailbreaks**\nhttps://www.theiphonewiki.com/wiki/Jailbreak#1.x')
		else:
			await self.bot.say('**No Jailbreak Found**')

	@commands.command(pass_context=True)
	async def tvos(self, ctx, ag):
		print('Got command TVOS')
		print('Got jailbreak ' + (ag))
		print('-------------------------------')
		if ag == "4.0" :
			await self.bot.say('**Older Versions of Seas0npass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "4.1" :
			await self.bot.say('**Older Versions of Seas0npass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "4.1.1" :
			await self.bot.say('**Older Versions of Seas0npass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "4.2" :
			await self.bot.say('**Older Versions of Seas0npass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "4.2.1" :
			await self.bot.say('**Older Versions of Seas0npass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "4.2.2" :
			await self.bot.say('**Older Versions of Seas0npass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "4.3" :
			await self.bot.say('**Older Versions of Seas0npass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "4.4" :
			await self.bot.say('**Seas0npass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "4.4.1" :
			await self.bot.say('**Seas0nPass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "4.4.2" :
			await self.bot.say('**Seas0nPass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "4.4.3" :
			await self.bot.say('**Seas0nPass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "4.4.4" :
			await self.bot.say('**Seas0nPass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "4" :
			await self.bot.say('**4.4-4.4.4: Seas0npass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
			await self.bot.say('**5.3: Older Versions of Seas0npass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "5.0" :
			await self.bot.say('**Seas0nPass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "5.0.1" :
			await self.bot.say('**Seas0nPass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "5.0.2" :
			await self.bot.say('**Seas0nPass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "5.1" :
			await self.bot.say('**Seas0nPass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "5.1.1" :
			await self.bot.say('**Seas0nPass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "5.2" :
			await self.bot.say('**Seas0nPass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "5.2.1" :
			await self.bot.say('**p0sixspwn**\nhttps://mega.nz/#F!WjhEUbxb!baJ59QNui6Wc9X28wY1hsw')
		elif ag == "5.3" :
			await self.bot.say('**Seas0nPass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "5" :
			await self.bot.say('**5.3: Seas0nPass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
			await self.bot.say('**5.2.1: p0sixspwn**\nhttps://mega.nz/#F!WjhEUbxb!baJ59QNui6Wc9X28wY1hsw')
			await self.bot.say('**5.0-5.2: Seas0nPass**\nhttps://support.firecore.com/hc/en-us/articles/215090347-Jailbreaking-101-Seas0nPass')
		elif ag == "6.0" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "6.0.1" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "6.0.2" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "6.1" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "6.1.1" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "6.2" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "6.2.1" :
			await self.bot.say('**Seas0npass 0.9.8 for macOS**\nhttps://github.com/firecore/Seas0nPass/releases/download/0.9.8/Seas0nPass.zip')
		elif ag == "6" :
			await self.bot.say('**6.2.1: Seas0npass 0.9.8 for macOS**\nhttps://github.com/firecore/Seas0nPass/releases/download/0.9.8/Seas0nPass.zip')
			await self.bot.say('**6.0-6.2: No Jailbreak Found**')
		elif ag == "7.0" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "7.0.1" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "7.0.2" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "7.0.3" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "7.1" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "7.2" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "7.2.1" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "7.2.2" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "7" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "9.0" :
			await self.bot.say('**Pangu9**\nhttp://en.9.pangu.io/')
		elif ag == "9.0.1" :
			await self.bot.say('**Pangu9**\nhttp://en.9.pangu.io/')
		elif ag == "9.1" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "9.1.1" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "9.2" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "9.2.1" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "9.2.2" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "9" :
			await self.bot.say('**9.1-9.2.2: No Jailbreak Found**')
			await self.bot.say('**9.0-9.0.1: Pangu9**\nhttp://en.9.pangu.io/')
		elif ag == "10.0" :
			await self.bot.say('**LiberTV**\nhttps://mega.nz/#!62BSQBoA!140CkCwY84tML979m13E8A14ADF1PXb7nrbfumZ3PV4')
		elif ag == "10.0.1" :
			await self.bot.say('**LiberTV**\nhttps://mega.nz/#!62BSQBoA!140CkCwY84tML979m13E8A14ADF1PXb7nrbfumZ3PV4')
		elif ag == "10.1" :
			await self.bot.say('**LiberTV**\nhttps://mega.nz/#!62BSQBoA!140CkCwY84tML979m13E8A14ADF1PXb7nrbfumZ3PV4')
		elif ag == "10.1.1" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "10.2" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "10.2.1" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "10.2.2" :
			await self.bot.say('**greeng0blin**\nhttps://nito.tv/')
		elif ag == "10" :
			await self.bot.say('**10.2.2: greeng0blin**\nhttps://nito.tv/')
			await self.bot.say('**10.1.1-10.2.1: No Jailbreak Found**')
			await self.bot.say('**10.0-10.1: LiberTV**\nhttps://mega.nz/#!62BSQBoA!140CkCwY84tML979m13E8A14ADF1PXb7nrbfumZ3PV4')
		elif ag == "11.0" :
			await self.bot.say('**LiberTV**\nhttp://newosxbook.com/LiberTV/')
		elif ag == "11.1" :
			await self.bot.say('**LiberTV**\nhttp://newosxbook.com/LiberTV/')
		elif ag == "11.2" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "11.2.1" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "11.2.5" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "11.2.6" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "11.3" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "11.4" :
			await self.bot.say('**No Jailbreak Found**')
		elif ag == "11" :
			await self.bot.say('**11.2-11.4: No Jailbreak Found**')
			await self.bot.say('**11.0-11.1: LiberTV**\nhttp://newosxbook.com/LiberTV')
		else:
			await self.bot.say('**No Jailbreak Found**')

	@commands.command(pass_context=True)
	async def help(self, ctx, arg):
		print('Got command HELP')
		print('-------------------------------')
		embed = discord.Embed(title="Unit", colour=discord.Colour(0x000000), description="in awe at the size of this lad.", icon_url="https://i.imgur.com/YGoOBaw.png", timestamp=datetime.utcfromtimestamp(1526316493))
		embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/1kA_jFsb9X46SG_exCVzErqvsX1F1qWs1f1hHpmis8I/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/457654628343873537/7f73fc9a11992444867c2cc3bfe1e2df.png?width=300&height=300")
		if(arg=="ipa"):
			embed.add_field(name="~u;ipa <jailbreak>", value="Grabs any one of a range of jailbreaks and provides a link. MEGA links originally provided by CetaceanNation. Thanks man!")
		if(arg=="ios"):
			embed.add_field(name="u;ios <version>", value="Links the most effective jailbreak per specified iOS version.")
		if(arg=="tvos"):
			embed.add_field(name="u;tvos <version>", value="Links the most effective jailbreak per specified tvOS version.")
		if(arg=="ipsw"):
			embed.add_field(name="u;ipsw <model> <version>", value="Tells if a specific IPSW is still signed by Apple or not and then links it.")
		if(arg=="timesince"):
			embed.add_field(name="u;timesince <year>", value="Time that has passed since a specified year in seconds.")
		if(arg=="timeuntil"):
			embed.add_field(name="u;timeuntil <year>", value="Time that will pass until a specified year in seconds.")
		if(arg=="randomtime"):
			embed.add_field(name="u;randomtime <range>", value="Random time value")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def about(self, ctx):
		print('Got command ABOUT')
		print('-------------------------------')
		embed = discord.Embed(title="Unit", colour=discord.Colour(0x000000), description="Unit is a bot that is, as the name suggests, an absolute fucking unit. It can do a lot, from iOS to time measurements to image manipulation. Made in discord.py by Yak#7474", icon_url="https://i.imgur.com/YGoOBaw.png", timestamp=datetime.utcfromtimestamp(1526316493))
		embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/1kA_jFsb9X46SG_exCVzErqvsX1F1qWs1f1hHpmis8I/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/457654628343873537/7f73fc9a11992444867c2cc3bfe1e2df.png?width=300&height=300")
		embed.add_field(name="Special Thanks", value="Exofeel#3333 (exo) - helped with commands\nGarrett#8026 (bren) - tested commands\nDevinThePancake#5559 (devin) - inspiration\nclemente#7106 (clem) - free code\nZach17#7213 (zach) - emotional support\nwanderingbox#3500 (wandering) - wojaks\nPadraig#1020 (padraig) - regards\nM1staAwesome#0117 (m1sta) - spammed commands\nJames Luke#9069 (ethan) - literally nothing\nSpecial thanks to Rusty_Balboa#6969 (stackoverflow)\n\nIn loving memory of the old Several Gang.\n")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def ipsw(self, ctx, arg1, arg2):
		a=0
		with open('firmwares.json') as fw:
			jdata = json.load(fw)
			for i in jdata['devices'][arg1]['firmwares']:
				if i['version'] == arg2:
					a=1
					print('Got command IPSW')
					print('Got model ' + (arg1))
					print('Got iOS ' + (arg2))
					print(i['signed'])
					print(i['url'])
					print('-------------------------------')
					gaa = str(i['signed'])
					await self.bot.say(jdata["devices"][arg1]["name"] + ": **" + gaa + "**\n" + i['url'])
					break
			if(a==0):
				await self.bot.say('**Error: No IPSW found for this combination!**')

	@commands.command(pass_context=True)
	async def failbreak(self, ctx, fb):
		fb=fb.lower()
		await self.bot.say("Unit PSA: This command is just if you're curious. seriously don't use this jailbreak")
		if fb == "cydeload":
			await self.bot.say("https://yakz.cf/ios/Cydeload_Alpha-2.1.ipa")
		elif fb == "spring":
			await self.bot.say("https://goo.gl/kX9VEV")
		elif fb == "topanga":
			await self.bot.say("https://github.com/iabem97/topanga")
		elif fb == "to.panga":
			await self.bot.say("https://github.com/iabem97/topanga")
		elif fb == "fracture":
			await self.bot.say("https://cdn.discordapp.com/attachments/456104053802532866/457740587861278720/fracture.ipa")
		elif fb == "c0f3":
			await self.bot.say("https://github.com/JosephShenton/C0F3")
		else:
			await self.bot.say("nothing found")

	@ipa.error
	async def ipa_error(self, error, ctx):
		if isinstance(error, discord.ext.commands.MissingRequiredArgument):
			await self.bot.say('**Error:** Argument `jailbreak` missing')

	@help.error
	async def ipa_error(self, error, ctx):
		if isinstance(error, discord.ext.commands.MissingRequiredArgument):
			embed = discord.Embed(title="Unit", colour=discord.Colour(0x000000), description="in awe at the size of this lad", icon_url="https://i.imgur.com/YGoOBaw.png", timestamp=datetime.utcfromtimestamp(1526316493))
			embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/1kA_jFsb9X46SG_exCVzErqvsX1F1qWs1f1hHpmis8I/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/457654628343873537/7f73fc9a11992444867c2cc3bfe1e2df.png?width=300&height=300")
			embed.add_field(name="iOS", value="`u;ios`, `u;ipa`, `u;tvos`, `u;ipsw`, `u;failbreak`")
			embed.add_field(name="Time Since", value="`u;timesince`, `u;timeuntil`, `u;randomtime`")
			embed.add_field(name="Fun", value="`u;say`, `u;reverse`, `u;urban`, `u;dictionary`, `u;img`, `u;doggo`, `u;cat`, `u;bird`, `u;shibe`, `u;duck`, `u;fox`, `u;redpanda`, `u;fortune`, `u;catinfo`, `u;avatar`, `u;wojak` :star:")
			await self.bot.say(embed=embed)
	@ios.error
	async def ios_error(self, error, ctx):
		if isinstance(error, discord.ext.commands.MissingRequiredArgument):
			await self.bot.say('**Error:** Argument `iOS` missing')

	@tvos.error
	async def tvos_error(self, error, ctx):
		if isinstance(error, discord.ext.commands.MissingRequiredArgument):
			await self.bot.say('**Error:** Argument `tvOS` missing')

	@eval.error
	async def eval_error(self, error, ctx):
		if isinstance(error, discord.ext.commands.MissingRequiredArgument):
			await self.bot.say('**Error:** Nothing to evaluate.')

	@ipsw.error
	async def ipsw_error(self, error, ctx):
		if isinstance(error, discord.ext.commands.MissingRequiredArgument):
			await self.bot.say('**Error:** Argument missing. Please specify both Model and iOS.')
		

def setup(bot):
    bot.add_cog(IPAm(bot))