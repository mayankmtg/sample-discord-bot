##   Primary Author: Mayank Mohindra <github.com/mayankmtg>
##
##   Description: Main file. Contains logic to handle all commands and start the bot
##
import discord
from discord.ext import commands
from search import perform_search
from config import Config
from cache import save_search_query, find_search_history
from db import Connection
from error import ErrorMessage

Config.load()

client = discord.Client()
conn = Connection(Config.DATABASE)

# bot starts
@client.event
async def on_ready():
	print ("bot is running")

# bot receives any messages
@client.event
async def on_message(command):
	# Ignore string from self
	if command.author == client.user:
		return

	# 1. Handle Greeting: 'hi' -> 'hey'
	if command.content == 'hi':
		await command.channel.send('hey')
	
	cmd_tokens = command.content.split()
	cmd_userid = command.author.id
	cmd_type = cmd_tokens[0]
	cmd_args = cmd_tokens[1:]
	
	# if command does not have the right number of tokens
	if len(cmd_args) < 1:
		await command.channel.send(ErrorMessage.INCORRECT_COMMAND)
		return
	
	# 2. Handle Google Search command. Response contains top 5 newline separated search results
	if cmd_type == '!google':
		query = ' '.join(cmd_args)
		if not save_search_query(conn, cmd_userid, query):
			print ("ERROR")
		result = perform_search(query)
		await command.channel.send('\n'.join(result))

	# 3. Handle Recent search command.
	#    Response contains all the previous search queries containing the passed substring (newline separated)
	if cmd_type == '!recent':
		query = ' '.join(cmd_args)
		result = find_search_history(conn, cmd_userid, query)
		await command.channel.send('\n'.join(result))


# Starting the bot
client.run(Config.DISCORD_TOKEN)

# close connection to database
conn.shutdown()
