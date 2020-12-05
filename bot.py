# bot.py
import os

import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='gasp ')

functions = ['scr.events','scr.gasp']

if __name__ == '__main__':
	for function in functions:
		bot.load_extension(function)
	bot.run(TOKEN)
