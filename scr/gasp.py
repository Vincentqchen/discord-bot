import discord
import random
import requests
import youtube_dl

from discord.ext import commands


players = {}

#User Comparision
def user_is_me(ctx):
    return ctx.author.id == 172475977450913792

class Bot(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	#Bot Commands
	@commands.command(name='cry')
	async def cry(self, ctx):
	    r = requests.get('https://source.unsplash.com/collection/1775931')
	    await ctx.send(r.url)

	@commands.command(name='amicool')
	async def amicool(self, ctx):
		if user_is_me(ctx):
			await ctx.send(file = discord.File("res/wavy_bro.jpg"))
			await ctx.send('ngl, your fucking wavy bro')
		else:
			if random.randint(1,10) == 2:
				await ctx.send(file = discord.File('/res/wavy bro.jpeg'))
				await ctx.send('ngl, your fucking wavy bro')
			else:
				await ctx.send('https://media1.tenor.com/images/59926e8ff8929e782a58fc142769518c/tenor.gif?itemid=15200688')
				await ctx.send('Nah bro, you ain\'t it')
	
	@commands.command()
	async def say(self, ctx, phrase:str=''):
		return

	@commands.command()
	async def clip(self, ctx, clip:str=''):
		channel = ctx.author.voice.channel
		channel = await channel.connect()
		channel.play(source("/res/clips/{0}.mp3".format(clip)))
		await ctx.voice_client.disconnect()

	@commands.command()
	async def play(self, ctx, url):
		channel = ctx.author.voice.channel
		channel = await channel.connect()
		guild = ctx.message.guild
		voice_client = guild.voice_client
		player = await voice_client.create_ffmpeg_player('res/clips/alex_sus.mp3')
		players[server.id] = player
		player.start()


	@commands.command()
	async def shaddup(self, ctx, member: discord.Member):
		if user_is_me(ctx) or ctx.author.guild_permissions.administrator:
			await member.edit(mute=True)
			await member.edit(deafen=True)
			if member.id == 259321897517449217:
				embed=discord.Embed(title="FUCK YOU CHRIS", description="Bitch Boi", color=0x1a285b)
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



	@commands.command()
	async def swearat(self, ctx, name:str='', num_times:str=''):
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

def setup(bot):
    bot.add_cog(Bot(bot))
    print('Miscellaneous module loaded.')