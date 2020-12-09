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

async def sayCommand(ctx, bot, *args):
	# If the user provides a language
	if len(args) > 1:
		tts = gTTS(args[0], lang=args[1])
	# If the user wants the default language
	elif len(args) == 1 and args[0] != 'help':
		tts = gTTS(args[0], lang='en')
	# If the user wants a random phrase played back to them
	elif len(args) == 0:
		all_phrases = open("res/say/phrases.txt").readlines()
		random.shuffle(all_phrases)
		lang = ['en-au','en-uk','zh-CN','ja','es']
		tts = gTTS(all_phrases[0], lang=random.choice(lang))

	# If the user requests help
	if len(args) == 1 and args[0] == 'help':
		embed=discord.Embed(title="Say command usage", description="Convert your text into speech and play that speech in your current voice channel", color=0x1fb2a8)
		embed.set_thumbnail(url="https://media.giphy.com/media/UttGj6RdxHlpkiWzEF/giphy.gif")
		embed.add_field(name="Default english accent", value="gasp say \"text\"", inline=False)
		embed.add_field(name="Custom accent", value="gasp say \"text\" \{language\}", inline=False)
		embed.add_field(name="Random joke/fun fact/phrase", value="gasp say", inline=False)
		await ctx.send(embed=embed)
	elif len(args) == 1 and args[0] == 'tts':
		ttsMode = True
		print(ttsMode)
	else:
		tts.save("res/say/saved_file.mp3")
		if ctx.author.voice != None:
			embed=discord.Embed(title="Success!", description="Relaying your message ", color=0x18d825)
			embed.set_footer(text="Requested by {}".format(ctx.author.display_name))
			await ctx.send(embed=embed)
			channel = ctx.author.voice.channel
			channel = await channel.connect()
			guild = ctx.guild 
			voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
			audio_source = discord.FFmpegPCMAudio('res/say/saved_file.mp3')
			if not voice_client.is_playing():
				voice_client.play(audio_source, after=None)
			while voice_client.is_playing():
				await asyncio.sleep(1)
			await voice_client.disconnect()
		else:
			await ctx.send("Must be in a VC to use this command")