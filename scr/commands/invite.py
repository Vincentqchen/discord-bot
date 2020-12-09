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

async def inviteCommand(ctx):
	await ctx.author.send("Your mistake...")
	await ctx.author.send('https://discord.com/api/oauth2/authorize?client_id=770766611929366551&permissions=0&scope=bot')