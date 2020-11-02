import discord
import asyncio
from discord.ext import commands
import itertools 

response = False

async def change_status(bot, data):
    await bot.wait_until_ready()
    msgs = itertools.cycle(data)
    while not bot.is_closed():
        current_status = next(msgs)
        await bot.change_presence(activity=discord.Game(name=current_status))
        await asyncio.sleep(5)

class Events(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.Cog.listener()
	async def on_ready(self):
		list1 = ["with my feelings :(","with my life :(","with people's feelings","with nishants feelings","a shitty game","with my sleep schedule","with my school work","...just getting played ;-;"]
		self.bot.loop.create_task(change_status(self.bot, list1))
		print(f'Up and running?')

	@commands.Cog.listener()
	async def on_member_join(member):
  		await member.send(f"lmao, {member} has joined this doo doo server")

	@commands.Cog.listener()
	async def on_message(self, message):
	    if message.author == self.bot.user:
	        return

	    if message.guild is None and message.content == "stop":
	        response = True




	    # if message.author.id == 114081086065213443:
	    # 	await message.channel.send('GAY BITCH')
def setup(bot):
    bot.add_cog(Events(bot))
    print('Miscellaneous module loaded.')