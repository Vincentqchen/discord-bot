# bot.py
import os
import random
import requests
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='gasp ')

client = discord.Client()

#Client events
@client.event
async def on_ready():
    print(f'We have logged in as {0}'.format(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        await client.process_commands(message)

    if message.author.id == 114081086065213443:
    	await message.channel.send('GAY BITCH')
#User Comparision
def user_is_me(ctx):
    return ctx.author.id == 172475977450913792

class Bot(commands.Bot):
	#Bot Commands
	@bot.command(name='cry')
	async def cry(ctx):
	    r = requests.get('https://source.unsplash.com/collection/1775931')
	    await ctx.send(r.url)

	@bot.command(name='coolness_level')
	async def coolness_level(ctx):
		if user_is_me(ctx):
			await ctx.send()
			await ctx.send('ngl, your fucking wavy bro')
		else:
			if random.randint(1,10) == 2:
				await ctx.send('hello',file = discord.file('/mnt/c/Users/vinyc/Dropbox/Discord Bot/res/wavy bro.jpeg'))
				await ctx.send('ngl, your fucking wavy bro')
			else:
				await ctx.send('https://media1.tenor.com/images/59926e8ff8929e782a58fc142769518c/tenor.gif?itemid=15200688')
				await ctx.send('Nah bro, you ain\'t it')
				
	@bot.command()
	async def swearat(ctx, name:str='', num_times:str=''):
	    all_words = open("/mnt/c/Users/vinyc/Dropbox/Discord Bot/res/swearwords.txt").readlines()
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
client.run(TOKEN)