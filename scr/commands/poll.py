import discord
import random
import requests
import os
from dotenv import load_dotenv
from gtts import gTTS
import json
import youtube_dl 
from async_timeout import timeout
import asyncio
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from discord.ext import commands
import opuslib

async def pollCommand(ctx,*args):
	if len(args) == 0:
		embed=discord.Embed(title="Poll Usage", description="Creates a poll using reactions as poll data", color=0xce1adb)
		embed.set_thumbnail(url="https://media.giphy.com/media/KzPQHtlTajSTVPRcCz/giphy.gif")
		embed.add_field(name="To create a poll", value="gasp poll \"{Poll Question}\" \"arg1\" \"arg2\" ... ", inline=True)
		await ctx.send(embed=embed)
	elif len(args) == 1:
		embed=discord.Embed(title="Poll Usage", description="Creates a poll using reactions as poll data", color=0xce1adb)
		embed.set_thumbnail(url="https://media.giphy.com/media/KzPQHtlTajSTVPRcCz/giphy.gif")
		embed.add_field(name="To create a poll", value="gasp poll \"{Poll Question}\" \"arg1\" \"arg2\" ... ", inline=True)
		await ctx.send(embed=embed)
	else:
		reactions = ['🇦','🇧','🇨','🇩','🇪','🇫','🇬','🇭','🇮']
		#Create the embed with the first argument as the title
		embed=discord.Embed(title=args[0], description="React to choose an answer",color=0x2b5df3)
		for n in range(97,len(args)+96):
			x = "regional_indicator_{0}".format(chr(n))
			embed.add_field(name=":regional_indicator_{0}: - {1}".format(chr(n), args[n-96]), value="\u200b", inline=False)
			
		message = await ctx.send(embed=embed)
		for num in range(len(args)-1):
			await message.add_reaction(reactions[num])