import json
import youtube_dl 
from async_timeout import timeout
import asyncio
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from discord.ext import commands
import opuslib

async def amicoolCommand(ctx, *args):
	if user_is_me(ctx):
		await ctx.send(file = discord.File("res/wavy_bro.jpg"))
		await ctx.send('ngl, your pretty wavy bro')
	else:
		if random.randint(1,10) == 2:
			await ctx.send(file = discord.File('res/wavy_bro.jpg'))
			await ctx.send('ngl, your pretty wavy bro')
		else:
			await ctx.send('https://media1.tenor.com/images/59926e8ff8929e782a58fc142769518c/tenor.gif?itemid=15200688')
			await ctx.send('Nah bro, you ain\'t it')