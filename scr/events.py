import discord
import asyncio
from gtts import gTTS
from discord.ext import commands
import itertools 

#import scr.gasp
ttsMode = False

async def change_status(bot, data):
    await bot.wait_until_ready()
    msgs = itertools.cycle(data)
    while not bot.is_closed():
        current_status = next(msgs)
        await bot.change_presence(activity=discord.Game(name=current_status))
        await asyncio.sleep(5)

class Events(commands.Cog):
	def __init__(self, bot):
		self.ttsMode = False
		self.userId = 0
		self.bot = bot


	@commands.Cog.listener()
	async def on_ready(self):
		list1 = ["with my feelings :(","with my life :(","with people's feelings","with nishants feelings","a shitty game","with my sleep schedule","with my school work","...just getting played ;-;"]
		self.bot.loop.create_task(change_status(self.bot, list1))
		print(f'Up and running?')

	@commands.Cog.listener()
	async def on_member_join(member):
  		await self.bot.send(f"lmao, {member} has joined this doo doo server")

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.send('You can use this command again in %.2d seconds' % error.retry_after)
		elif isinstance(error, commands.CommandNotFound):
			embed=discord.Embed(title="Command doesn't exist", description="To find a list of all commands, please do \"gasp help\"", color=0xd31d1d)
			embed.set_footer(text="Error created by {}".format(ctx.message.author.display_name))
			await ctx.send(embed=embed)
		elif isinstance(error, commands.MissingRequiredArgument):
			if str(ctx.command) == "noticemesenpai":
				embed=discord.Embed(title="Spams a user with an optional message and an invite link to the channel", description="NOTE: Has a 30 second cooldown and can only spam 10 messages", color=0x1c49ce)
				embed.set_author(name="noticemesenpai command usage")
				embed.set_thumbnail(url="https://media.giphy.com/media/ASd0Ukj0y3qMM/giphy.gif")
				embed.add_field(name="Spam user with default message", value="gasp noticemesenpai \{name\} \{number of times\}", inline=False)
				embed.add_field(name="Spam user with custom message", value="gasp noticemesenpai \{name\} \{number of times\} \"\{message\}\"", inline=False)
				await ctx.send(embed=embed)
		raise error  # re-raise the error so all the errors will still show up in console


	@commands.Cog.listener()
	async def on_message(self, message):
		ctx = await self.bot.get_context(message)

		if message.author == self.bot.user:
			return

		if "bruh" in message.content.lower():
			await message.channel.send("bruh moment")

		if message.content == "gasp say tts":
			self.userId = message.author.id
			self.ttsMode = True
			tts = gTTS("Starting TTS session", lang='en')
			tts.save("res/say/saved_file.mp3")
			if ctx.author.voice != None:
				channel = ctx.author.voice.channel
				channel = await channel.connect()
				guild = ctx.guild 
				voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
				audio_source = discord.FFmpegPCMAudio('res/say/saved_file.mp3')
				if not voice_client.is_playing():
					voice_client.play(audio_source, after=None)
				await ctx.send("Starting TTS Session\nType: \"Stop TTS\"")
			else:
				await ctx.send("Must be in a VC to use this command")
		if message.content.lower() == "stop tts":
			self.ttsMode = False
			voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
			await voice_client.disconnect()
			await ctx.send("Ending TTS Session")	


		if self.ttsMode and message.author.id == self.userId and message.content != "gasp say tts":
			tts = gTTS(message.content, lang='en')
			tts.save("res/say/saved_file.mp3")
			if ctx.author.voice != None:
				guild = ctx.guild 
				voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
				audio_source = discord.FFmpegPCMAudio('res/say/saved_file.mp3')
				if not voice_client.is_playing():
					voice_client.play(audio_source, after=None)
				else:
					await ctx.send("Please wait till the bot has finished her sentence")
			else:
				await ctx.send("Must be in a VC to use this command")

		





			#await ctx.invoke(self.bot.get_command('say'), message.content)

def setup(bot):
    bot.add_cog(Events(bot))
    print('Events module loaded.')