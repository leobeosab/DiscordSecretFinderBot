import discord, os, re
from modules import helper

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in User: {0.user} | {0.user.id}".format(client))

@client.event
async def on_message(message):
    githubString = helper.get_github_string(message.content)
    if githubString is None:
        return
    
    await message.channel.send("Yo, this is a github link")

client.run(os.environ["SECRETFINDERBOTTOKEN"])


