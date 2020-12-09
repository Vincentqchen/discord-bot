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

async def scaremeCommand(ctx, bot):
	await ctx.message.delete()
	timeFrame = random.randint(20, 600)
	if ctx.author.voice.channel == None:
		channel = ctx.author.voice.channel
		channel = await channel.connect()
	await asyncio.sleep(timeFrame)
	guild = ctx.guild 
	voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
	audio_source = discord.FFmpegPCMAudio('res/scareme/scream1.mp3')
	if not voice_client.is_playing():
		voice_client.play(audio_source, after=None)
	while voice_client.is_playing():
		await asyncio.sleep(1)
	await voice_client.disconnect()