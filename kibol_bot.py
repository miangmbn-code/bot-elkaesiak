# This example requires the 'message_content' intent.

import discord
from discord import app_commands
from pathlib import Path

TOKEN_FILE = Path(__file__).with_name('token')

intents = discord.Intents.default()
intents.message_content = True



class MyClient(discord.Client):
	async def on_ready(self):
		await tree.sync();
		print(f'We have logged in as {client.user}')

	async def on_message(self,message):
		if message.author == client.user:
			return
			
		print(message.content)

		if message.content.startswith('$hello'):
			await message.channel.send('ŁKS!')
			
		if message.content.startswith('$legia'):
			await message.channel.send('LTSK!')
			
		if message.content.startswith('$lech'):
			await message.channel.send('Kolejorz, Kolejorz!')
			
		if message.content.startswith('$łks'):
			await message.channel.send('Niezwyciężeni, Niepokonani!')
			
		if message.content.startswith('$jaga'):
			await message.channel.send('Jagiellonia Białystok!')

client = MyClient(intents=intents)

tree = app_commands.CommandTree(client)

client.tree = tree
@tree.command(
	name="pomoc",
	description="Wyświetla pomoc")
async def pomoc(interaction: discord.Interaction):
	await interaction.response.send_message(
		"Poproś grzeczniej"
	)
	
@tree.command(
	name="poprosze_pomoc",
	description="Wyświetla pomoc teraz na pewno")
async def poprosze_pomoc(interaction: discord.Interaction):
	await interaction.response.send_message(
		"**Komendy:**\n"
		"`/poprosze pomoc` - pokazuje poniższą pomoc\n"
		"`/pomoc` - nie pokazuje poniższej pomocy\n"
		"`$`i nazwa jakiegoś klubu - różne teksty\n"
	)

def load_token():
	token = TOKEN_FILE.read_text()
	return token
	
token = load_token()
client.run(token)
