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

async def noticemesenpaiCommand(ctx, member, *args):
	name = ctx.author.display_name
	if int(args[0]) > 10:
		await ctx.send("Can't be spamming them so much")
	else:
		await ctx.send("Attack sent succesfully")
		invitelink = await ctx.channel.create_invite(max_uses=1,unique=True)
		await member.send(invitelink)
		for num in range(int(args[0])):

			embed=discord.Embed(title="{} wants your attention ;) ".format(name), description="He/She's chillin in the server above", color=0x1ad194)
			if len(args) > 1:
				embed.add_field(name="They want you to know:", value=args[1], inline=False)
			embed.set_footer(text="Requested by {}".format(name))
			await member.send(embed=embed)
			
			await asyncio.sleep(5)