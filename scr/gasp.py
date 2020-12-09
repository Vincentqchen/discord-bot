import discord
import random
import requests
import os
from dotenv import load_dotenv
from gtts import gTTS
import json
import youtube_dl 
import asyncio
from discord.ext import commands
import opuslib

#Fire base
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Command imports
from scr.commands.cry import cryCommand
from scr.commands.invite import inviteCommand
from scr.commands.play import playCommand
from scr.commands.summon import summonCommand
from scr.commands.stop import stopCommand
from scr.commands.meme import memeCommand
from scr.commands.amicool import amicoolCommand
from scr.commands.poll import pollCommand
from scr.commands.scareme import scaremeCommand
from scr.commands.say import sayCommand
from scr.commands.noticemesenpai import noticemesenpaiCommand
from scr.commands.clip import clipCommand
from scr.commands.shaddup import shaddupCommand
from scr.commands.swearat import swearatCommand
from scr.commands.usage import usageCommand
from scr.commands.master import masterCommand

db = firestore.client()

#User Comparision
def user_is_me(ctx):
    return ctx.author.id == 172475977450913792

def user_is_quad(ctx):
	return ctx.author.id == 114081086065213443 or ctx.author.id == 259321897517449217 or ctx.author.id == 403355889253220352 or ctx.author.id == 172475977450913792

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

class Bot(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def master(self, ctx, *args):
		if await usageHelper(ctx, ctx.author.id,'master') == False:
			return
		await masterCommand(ctx, *args)

	@commands.command()
	async def usage(self,ctx, member: discord.Member, *args):
		await usageCommand(ctx,member,*args)

	@commands.command()
	async def meme(self,ctx,*args):
		if await usageHelper(ctx, ctx.author.id,'meme') == False:
			return
		await memeCommand(ctx, *args)

	@commands.command()
	async def summon(self, ctx):
		if await usageHelper(ctx, ctx.author.id,'summon') == False:
			return
		await summonCommand(ctx)

	@commands.command()
	async def stop(self, ctx):
		if await usageHelper(ctx, ctx.author.id,'stop') == False:
			return
		await stopCommand(ctx)

	@commands.command(pass_context=True)
	async def play(self, ctx, *, url):
		if await usageHelper(ctx, ctx.author.id,'play') == False:
			return
		await playCommand(ctx,self.bot)

	@commands.command(name='cry')
	async def cry(self, ctx):
		if await usageHelper(ctx, ctx.author.id,'cry') == False:
			return
		await cryCommand(ctx, self.bot)

	@commands.command()
	async def invite(self, ctx):
		if await usageHelper(ctx, ctx.author.id,'meme') == False:
			return
		await inviteCommand(ctx)

	@commands.command(name='amicool')
	async def amicool(self, ctx):
		if await usageHelper(ctx, ctx.author.id,'amicool') == False:
			return
		await amicoolCommand(ctx, *args)
	
	@commands.command()
	async def poll(self, ctx, *args):
		if await usageHelper(ctx, ctx.author.id,'poll') == False:
			return
		await pollCommand(ctx, *args)

	@commands.command()
	async def scareme(self,ctx):
		if await usageHelper(ctx, ctx.author.id,'scareme') == False:
			return
		await scaremeCommand(ctx, self.bot)

	@commands.command()
	async def say(self, ctx, *args):
		if await usageHelper(ctx, ctx.author.id,'say') == False:
			return
		await sayCommand(ctx, self.bot, *args)

	@commands.command()
	@commands.cooldown(1, 30, commands.BucketType.user)
	async def noticemesenpai(self, ctx, member: discord.Member, *args):
		if await usageHelper(ctx, ctx.author.id,'noticemesenpai') == False:
			return
		user = member
		await noticemesenpaiCommand(ctx, user, *args)

	@commands.command()
	async def clip(self, ctx, *args):
		if await usageHelper(ctx, ctx.author.id,'clip') == False:
			return
		await clipCommand(ctx, self.bot, *args)

	@commands.command()
	async def shaddup(self, ctx, member: discord.Member):
		if await usageHelper(ctx, ctx.author.id,'shaddup') == False:
			return
		await shaddupCommand(ctx, member)

	@commands.command()
	async def swearat(self, ctx, name:str='', num_times:str=''):
		if await usageHelper(ctx, ctx.author.id,'swearat') == False:
			return
		await swearatCommand(ctx)

def setup(bot):
    bot.add_cog(Bot(bot))
    print('Gasp module loaded.')