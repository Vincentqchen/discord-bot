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

def user_is_me(ctx):
    return ctx.author.id == 172475977450913792

def user_is_quad(ctx):
	return ctx.author.id == 114081086065213443 or ctx.author.id == 259321897517449217 or ctx.author.id == 403355889253220352 or ctx.author.id == 172475977450913792

async def clipCommand(ctx, bot, *args):
	if user_is_quad(ctx):
		if len(args) == 0:
			embed=discord.Embed(title="will play a sus clip.", description="Usage: gasp clip {clip-name}", color=0x1100ff)
			embed.set_thumbnail(url="https://media.giphy.com/media/dgK22exekwOLm/giphy.gif")
			embed.set_author(name="Clip Command Usage")
			embed.add_field(name="List of avaliable clips:", value="bitch chris \n i just farted \n alex_sus \n nishant wack \n nishant_is_gay\n slurpslurpalex\n huuhhhh nishant\n gay_for_me\n nishidoesthedeed\n babynish\n suschris\n beepboopbop\n deathtochris\n nishant likes asshole\n chrisextrasus", inline=True)
			await ctx.send(embed=embed)
		else:
			#If the author isn't 
			if ctx.author.voice != None:
				if os.path.isfile('res/clips/{}.mp3'.format(args[0])):
					channel = ctx.author.voice.channel
					channel = await channel.connect()
					guild = ctx.guild 
					voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
					audio_source = discord.FFmpegPCMAudio('res/clips/{}.mp3'.format(args[0]))
					if not voice_client.is_playing():
						voice_client.play(audio_source, after=None)
					while voice_client.is_playing():
						await asyncio.sleep(1)
					await voice_client.disconnect()
				else:
					await ctx.send("This clip doesn't exist")
			else:
				await ctx.send("Must be in a VC to use this command")
	else:
		await ctx.send("Not a quad member, sorry :(")