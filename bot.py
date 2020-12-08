# bot.py
import os

import discord

from discord.ext import commands
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("firestore-services.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='gasp ', intents=intents)


functions = ['scr.events','scr.gasp']

if __name__ == '__main__':
	for function in functions:
		bot.load_extension(function)
	bot.run(TOKEN)
