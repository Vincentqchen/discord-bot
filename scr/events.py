import discord

from discord.ext import commands


class Events(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
	    print(f'Up and running!')

	@commands.Cog.listener()
	async def on_message(self, message):
	    if message.author == self.bot.user:
	        return

	    if message.content.startswith('$hello'):
	        await message.channel.send('Hello!')

	    # if message.author.id == 114081086065213443:
	    # 	await message.channel.send('GAY BITCH')
def setup(bot):
    bot.add_cog(Events(bot))
    print('Miscellaneous module loaded.')