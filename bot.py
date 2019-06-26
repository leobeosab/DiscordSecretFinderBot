import discord, os, re
from modules import helper

CLIENT = discord.Client()
FLAG_EMOJI = "\N{eyes}"

@CLIENT.event
async def on_ready():
    print("Logged in User: {0.user} | {0.user.id}".format(CLIENT))

@CLIENT.event
async def on_message(message):
    if message.channel.name == "secret-nazi-log":
        return

    githubString = helper.get_github_string(message.content)
    if githubString is None:
        return
    
    logs = helper.run_truffle_hog(githubString)
    if logs is not None:
        await message.add_reaction(FLAG_EMOJI)
        await helper.message_secret_nazi_channel(message.guild, logs, githubString)

CLIENT.run(os.environ["SECRETFINDERBOTTOKEN"])


