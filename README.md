# DiscordSecretFinderBot
Searches Github using truffle hog on all github links sent in a discord server

## How to use
Any Github link that is sent to any text_channel on a server is scanned for open secrets, if secrets are found "Secret Nazi" will add an eyes reaction and output the results of the scan in a "secret-nazi-log" text channel that once created you can make private or admins only

[install on your server!](https://discordapp.com/api/oauth2/authorize?client_id=593475505286545409&permissions=83024&scope=bot)

## Tools:
*   Discord.py
*   TruffleHog

## Installation / running:
1. ```pip3 install truffle-hog, discord```
2. Make sure discord bot token env var is set ```SECRETFINDERBOTTOKEN=SECRETTOKEN```
3. ```python3 bot.py ```

Made for 2019 Discord Hack Week :)
