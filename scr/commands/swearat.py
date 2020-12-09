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

async def swearatCommand(ctx):	
	all_words = open("res/swearwords.txt").readlines()
	selected_words = all_words[random.randrange(165)][:-1]

	# see if "twice" or "thrice" is written in the command
	if 'twice' in num_times:
	    selected_words += ' ' + all_words[random.randrange(165)][:-1]
	elif 'thrice' in num_times:
	    selected_words += ' ' + all_words[random.randrange(165)][:-1] \
	                    + ' ' + all_words[random.randrange(165)][:-1]
	elif 'random' in num_times:
	    for i in range(random.randint(1, 10)):
	        selected_words += ' ' + all_words[random.randrange(165)][:-1]

	elif num_times.isdigit():
	    if int(num_times) > 1000: num_times = 1000

	    for i in range(int(num_times)):
	        selected_words += ' ' + all_words[random.randrange(165)][:-1]

	if name == '':
	    name = random.choice(ctx.guild.members).mention
	elif not name.startswith('<@'):
	    try:
	        name = ctx.guild.get_member_named(name).mention
	    except:
	        name = ctx.author.mention

	# check for long messages
	if len(name + ' is a ' + selected_words) <= 2000:
	    await ctx.send(name + ' is a ' + selected_words, delete_after=30)
	else:
	    curr_msg = name + ' is a' # build up message up to 2000 characters

	    for word in selected_words.split():
	        if len(curr_msg + ' ' + word) <= 2000:
	            curr_msg += ' ' + word
	        else:  # we've reached the limit
	            await ctx.send(curr_msg, delete_after=30)
	            curr_msg = name + ' is a ' + word  # start it over again

	    # send anything left over
	    if len('and finally ' + curr_msg) <= 2000: await ctx.send('and finally ' + curr_msg, delete_after=30)
	    else:
	        second_last_msg, last_word = curr_msg.rsplit(' ', 1)
	        await ctx.send(second_last_msg, delete_after=30)
	        await ctx.send('and finally ' + name + ' is a ' + last_word, delete_after=30)