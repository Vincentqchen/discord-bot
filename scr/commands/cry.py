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

async def cryCommand(ctx,bot):
	r = requests.get('https://source.unsplash.com/collection/1775931')
	await ctx.send(r.url)