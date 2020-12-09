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
import scr.gasp
import opuslib

def user_is_me(ctx):
    return ctx.author.id == 172475977450913792

def user_is_quad(ctx):
	return ctx.author.id == 114081086065213443 or ctx.author.id == 259321897517449217 or ctx.author.id == 403355889253220352 or ctx.author.id == 172475977450913792

async def shaddupCommand(ctx, member):	
	if user_is_me(ctx) or ctx.author.guild_permissions.administrator:
		await member.edit(mute=True)
		await member.edit(deafen=True)
		if member.id == 259321897517449217:
			embed=discord.Embed(title="Shhhhhhh chris", description=":(", color=0x1a285b)
			embed.set_author(name="Created by: Vincent <3")
			embed.set_thumbnail(url="https://media.giphy.com/media/I7p8K5EY9w9dC/giphy.gif")
			await ctx.send(embed=embed)
		else:
			embed=discord.Embed(title="RIP", description="Someone got salty...", color=0x1a285b)
			embed.set_author(name="Created by: Vincent <3")
			embed.set_thumbnail(url="https://media.giphy.com/media/zH72yAqrMuczC/giphy.gif")
			await ctx.send(embed=embed)
	else:
		embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
		await ctx.send(embed=embed)