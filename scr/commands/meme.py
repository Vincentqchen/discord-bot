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

async def memeCommand(ctx, *args):
	response = requests.get("https://api.imgflip.com/get_memes")
	memetemplates = ["","","","","",""]
	memedic = {}  #{num: (id,boxcount)}b


	# post = {
	#     "template_id": "",
	#     "username": "boyuchen",
	#     "password": "kfq9aWrP#KFtviR",
	#     "boxes":[],
	# }

	post2 = {
	    "template_id": "112126428",
	    "username": "boyuchen",
	    "password": "kfq9aWrP#KFtviR",
	    "boxes[0][type]":"text",
	    "boxes[1][type]":"text",
	    "boxes[0][text]":"text1",
	    "boxes[1][text]":"text1",
	}

	box = {
	"text": "",
	"x": 10,
	"y": 10,
	"width": 548,
	"height": 100,
	"color": "#ffffff",
	"outline_color": "#000000"
	}

	if response.status_code == 200: # ok
	    res = response.json()
	    count = 0
	    pointer = 0
	    for num,temp in enumerate(res["data"]["memes"]):
	        if count < len(res["data"]["memes"])//5:
	            memetemplates[pointer] = memetemplates[pointer] + str(num)+":  "+temp["name"]+"\n"
	            memedic[num] = (temp["id"],temp["box_count"])
	            count += 1
	        else:
	            pointer += 1
	            count = 0
	                
	else:
	    print("network issue")


	if len(args) == 0:    
	    for i in range(len(memetemplates)):
	        if len(memetemplates[i]) != 0:
	            p = "```{0}```".format(memetemplates[i])
	            await ctx.send(p,delete_after = 40)
	            await ctx.author.send(p)

	elif len(args) == 1:
	    memeid = memedic[int(args[0])][0]
	    post2["template_id"] = memeid


	    text = ""
	    for i in range(memedic[int(args[0])][1]):
	        text += (" text"+str(i))
	        post2[f"boxes[{i}][text]"] = f"text{i}"
	        post2[f"boxes[{i}][type]"] = "text"
	       

	    postresponse = requests.request('POST', url='https://api.imgflip.com/caption_image',params=post2).json()
	    image = postresponse["data"]["url"].replace("\\","")
	    await ctx.send(image)

	elif len(args) >= 3 and len(args) < 10:
	    memeid = memedic[int(args[0])][0]
	    post2["template_id"] = memeid
	    for i in range(memedic[int(args[0])][1]):
	        post2[f"boxes[{i}][text]"] = args[i+1]
	        post2[f"boxes[{i}][type]"] = "text"
	    postresponse = requests.request('POST', url='https://api.imgflip.com/caption_image',params=post2).json()
	    image = postresponse["data"]["url"].replace("\\","")
	    await ctx.send(image)
	    
	else:
	    await ctx.send("ur kind of a meme")