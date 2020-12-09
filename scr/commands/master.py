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

db = firestore.client()

async def masterCommand(ctx,*args):
	if len(args) == 0:
		embed=discord.Embed(title="Master Command", description="Add/Remove users to the master document", color=0x15e5cc)
		embed.add_field(name="Add Master", value="gasp master add {user}", inline=False)
		embed.add_field(name="Remove Master", value="gasp master remove {user}", inline=False)
		embed.set_footer(text="Requested by {0}".format(ctx.author.display_name))
		await ctx.send(embed=embed)
		return
	userId = args[1].replace('<@!','')
	userId = userId.replace('>','')
	member = ctx.guild.get_member(int(userId))
	masterDoc = db.collection(u'master').document(u'master')
	doc = masterDoc.get()
	doc = doc.to_dict()
	masterExists = False
	for x in doc:
		if x == str(ctx.author.id):
			masterExists = True
			break
	if masterExists:
		if args[0] == 'add':
			masterDoc.set({userId:member.display_name},merge = True)
			embed=discord.Embed(title="Master Command", description="You've succesfully added {0} to the master document".format(member.display_name), color=0x59ff00)
			embed.set_footer(text="Requested by {0}".format(ctx.author.display_name))
			await ctx.send(embed=embed)
		elif args[0] == 'remove':
			masterDoc.update({userId: firestore.DELETE_FIELD})
			embed=discord.Embed(title="Master Command", description="You've succesfully removed {0} from the master document".format(member.display_name), color=0xff0000)
			embed.set_footer(text="Requested by {0}".format(ctx.author.display_name))
			await ctx.send(embed=embed)
		else:
			embed=discord.Embed(title="Master Command", description="Add/Remove users to the master document", color=0x15e5cc)
			embed.add_field(name="Add Master", value="gasp master add {user}", inline=False)
			embed.add_field(name="Remove Master", value="gasp master remove {user}", inline=False)
			embed.set_footer(text="Requested by {0}".format(ctx.author.display_name))
			await ctx.send(embed=embed)
	else:
		embed=discord.Embed(title="Master Error", description="You are not authorized to run this command", color=0x59ff00)
		embed.set_footer(text="Requested by {0}".format(ctx.author.display_name))
		await ctx.send(embed=embed)