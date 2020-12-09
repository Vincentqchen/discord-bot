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

async def usageHelper(ctx,memberId,command):
	userDoc = db.collection(u'users').document(str(memberId))
	doc = userDoc.get()
	if (doc.exists == False):
		userDoc.set({u'meme':True, u'summon':True, u'stop':True, u'master':True, u'play':True, u'cry':True, u'invite':True, u'amicool':True, u'poll':True, u'scareme':True, u'say':True, u'noticemesenpai':True, u'clip':True, u'shaddup':True, u'swearat':True})
		return True
	else:
		doc = doc.to_dict()
		if doc[command]:
			return True
		else:
			embed=discord.Embed(title="Usage", description="You've been blocked from using this command", color=0xff0000)
			embed.set_footer(text="Rejection message sent by {0}".format(ctx.author.display_name))
			await ctx.send(embed=embed)
			return False

async def usageCommand(ctx, member, *args):
	userDoc = db.collection(u'users').document(str(member.id))
	masterDoc = db.collection(u'master').document(u'master')
	mDoc = masterDoc.get()
	mDoc = mDoc.to_dict()
	doc = userDoc.get()
	docDict = doc.to_dict()
	# Create document if user doesn't exist
	if (doc.exists == False):
		userDoc.set({u'meme':True, u'master':False, u'summon':True, u'stop':True, u'play':True, u'cry':True, u'invite':True, u'amicool':True, u'poll':True, u'scareme':True, u'say':True, u'noticemesenpai':True, u'clip':True, u'shaddup':True, u'swearat':True})
		docDict = userDoc.get().to_dict()
	masterExists = False
	for x in mDoc:
		if x == str(ctx.author.id):
			masterExists = True
			break
	if masterExists:
		if docDict != None and args[0] in docDict:
			if (args[1] == 'disable'):
				userDoc.set({args[0]:False}, merge = True)
				embed=discord.Embed(title="Usage Command", description="You've disabled the {0} command for {1}".format(args[0], member.display_name), color=0xff0000)
				embed.set_footer(text="Requested by {0}".format(ctx.author.display_name))
				await ctx.send(embed=embed)
			elif (args[1] == 'enable'):
				userDoc.set({args[0]:True}, merge = True)
				embed=discord.Embed(title="Usage Command", description="You've enabled the {0} command for {1}".format(args[0], member.display_name), color=0x59ff00)
				embed.set_footer(text="Requested by {0}".format(ctx.author.display_name))
				await ctx.send(embed=embed)
			else:
				embed=discord.Embed(title="Usage Command", description="Prevent specific users from using commands", color=0x1553e5)
				embed.add_field(name="Enable usage", value="gasp usage \{user\} \{ommand\} enable", inline=False)
				embed.add_field(name="Disable usage", value="gasp usage \{user\} \{command\} disable", inline=False)
				embed.set_footer(text="Requested by {0}".format(ctx.author.display_name))
				await ctx.send(embed=embed)
		elif args[0] == 'all':
			if args[1] == 'enable':
				userDoc.set({u'meme':True, u'master':False, u'summon':True, u'stop':True, u'play':True, u'cry':True, u'invite':True, u'amicool':True, u'poll':True, u'scareme':True, u'say':True, u'noticemesenpai':True, u'clip':True, u'shaddup':True, u'swearat':True})
			elif args[1] == 'disable':
				userDoc.set({u'meme':False, u'master':False, u'summon':False, u'stop':False, u'play':False, u'cry':False, u'invite':False, u'amicool':False, u'poll':False, u'scareme':False, u'say':False, u'noticemesenpai':False, u'clip':False, u'shaddup':False, u'swearat':False})
			else:
				embed=discord.Embed(title="Usage Command", description="Prevent specific users from using commands", color=0x1553e5)
				embed.add_field(name="Enable usage", value="gasp usage \{user\} \{ommand\} enable", inline=False)
				embed.add_field(name="Disable usage", value="gasp usage \{user\} \{command\} disable", inline=False)
				embed.set_footer(text="Requested by {0}".format(ctx.author.display_name))
				await ctx.send(embed=embed)
		else:
			embed=discord.Embed(title="Usage Command", description="The {} command does not exist".format(args[0]), color=0x59ff00)
			embed.set_footer(text="Requested by {0}".format(ctx.author.display_name))
			await ctx.send(embed=embed)
	else:
		embed=discord.Embed(title="Master Error", description="You are not authorized to run this command", color=0x59ff00)
		embed.set_footer(text="Requested by {0}".format(ctx.author.display_name))
		await ctx.send(embed=embed)
