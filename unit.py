import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import platform
from os import listdir
from os.path import isfile, join
import traceback

bot = commands.Bot(command_prefix='u;')
bot.remove_command("help")

number_of_servers = len(bot.servers)


@bot.event
async def on_ready():

	print('----------------------------------------')
	print("UNIT")
	print('----------------------------------------')

	number_of_servers = len(bot.servers)
	await bot.change_presence(game=discord.Game(name='A bot by Yak#7474 | u;help'.format(number_of_servers)))

for extension in [f.replace('.py', "") for f in listdir("cogs") if isfile(join("cogs", f))]:
	try:
		if not "__init__" in extension:
			print("loading cog {}".format(extension))
			bot.load_extension("cogs." + extension)
	except Exception as e:
		print("Error: cog {} not loaded!".format(extension))
		traceback.print_exc()
			
@bot.command(pass_context=True)
async def reload(ctx):
	if ctx.message.author.id == "232133184404455424":
		for cogload in [f.replace('.py', "") for f in listdir("cogs") if isfile(join("cogs", f))]:
			try:
				if not "__init__" in cogload:
					bot.unload_extension("cogs." + cogload)
					bot.load_extension("cogs." + cogload)
			except Exception as e:
				await bot.say("cog reload failed of {}. try again regard".format(cogload))
				traceback.print_exc()
				await bot.say("```{}```".format(e))
		await bot.say("done")
	else:
		await bot.say("you do not have permission to do this")

@bot.command(pass_context=True)
async def servers(ctx):
	if ctx.message.author.id == "232133184404455424":
		for x in bot.servers:
			print(x)

bot.run('bigFatL')