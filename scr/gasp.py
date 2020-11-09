import discord
import random
import requests
import os.path
import youtube_dl 
from async_timeout import timeout
from scr.events import response
import asyncio

from discord.ext import commands
import opuslib

OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']

youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
            pass

        raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))

#User Comparision
def user_is_me(ctx):
    return ctx.author.id == 172475977450913792

def user_is_quad(ctx):
	return ctx.author.id == 114081086065213443 or ctx.author.id == 259321897517449217 or ctx.author.id == 403355889253220352 or ctx.author.id == 172475977450913792

class Bot(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def summon(self, ctx):
		channel = ctx.author.voice.channel
		channel = await channel.connect()

	@commands.command()
	async def stop(self, ctx):
		server = ctx.message.guild.voice_client
		await server.disconnect()

	@commands.command(pass_context=True)
	async def play(self, ctx, *, url):
		channel = ctx.author.voice.channel
		channel = await channel.connect()
		async with ctx.typing():
			voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
			player = await YTDLSource.from_url(url, loop=self.bot.loop)
			voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
		await ctx.send('Now playing: {}'.format(player.title))

	#Bot Commands
	@commands.command(name='cry')
	async def cry(self, ctx):
	    r = requests.get('https://source.unsplash.com/collection/1775931')
	    await ctx.send(r.url)

	@commands.command()
	async def invite(self, ctx):
		await ctx.author.send("Your mistake...")
		await ctx.author.send('https://discord.com/api/oauth2/authorize?client_id=770766611929366551&permissions=0&scope=bot')

	@commands.command(name='amicool')
	async def amicool(self, ctx):
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
	
	@commands.command()
	async def poll(self, ctx, phrase:str=''):
		return
		
	@commands.command()
	async def say(self, ctx, phrase:str=''):
		return

	@commands.command()
	async def noticemesenpai(self, ctx, member: discord.Member, *args):
		name = ctx.author.mention
		if len(args) == 0:
			for num in range(50):
				await member.send("{} wants ur attention :)".format(name))
				await member.send("Tell me to \'stop\' and I'll stop <3")
				await asyncio.sleep(5)
				if response == True:
					print('f')
					break
		elif int(args[0]) > 10:
			await ctx.send("Can't be spamming them so much")
		else:
			for num in range(int(args[0])):
				await member.send("{} wants ur attention :)".format(name))
				if len(args) > 1:
					await member.send("They want you to know: \"{}\"".format(args[1]))
				await asyncio.sleep(5)


	@commands.command()
	async def clip(self, ctx, *args):
		if user_is_quad(ctx):
			if len(args) == 0:
				embed=discord.Embed(title="will play a sus clip.", description="Usage: gasp clip {clip-name}", color=0x1100ff)
				embed.set_thumbnail(url="https://media.giphy.com/media/dgK22exekwOLm/giphy.gif")
				embed.set_author(name="Clip Command Usage")
				embed.add_field(name="List of avaliable clips:", value="bitch chris \n i just farted \n alex_sus \n nishant wack \n nishant_is_gay\n huuhhhh nishant\n gay_for_me\n nishidoesthedeed\n babynish\n suschris\n beepboopbop\n deathtochris", inline=True)
				await ctx.send(embed=embed)
			else:
				#If the author isn't 
				if ctx.author.voice != None:
					if os.path.isfile('res/clips/{}.mp3'.format(args[0])):
						channel = ctx.author.voice.channel
						channel = await channel.connect()
						guild = ctx.guild 
						voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
						audio_source = discord.FFmpegPCMAudio('res/clips/{}.mp3'.format(args[0]))
						if not voice_client.is_playing():
							voice_client.play(audio_source, after=None)
						while voice_client.is_playing():
							await asyncio.sleep(1)
						await voice_client.disconnect()
					else:
						await ctx.send("This clip doesn't exist doopid")
				else:
					await ctx.send("Small brain headass... not even in a vc")
		else:
			await ctx.send("Not a quad member, sorry :(")
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

def setup(bot):
    bot.add_cog(Bot(bot))
    print('Miscellaneous module loaded.')