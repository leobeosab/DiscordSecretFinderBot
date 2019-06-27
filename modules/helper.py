import re, subprocess
from pathlib import Path
from discord import guild, utils

LOG_DELIM = '\n ------------------------------------------------'

# matches links for github repos
def get_github_string(data):
    pattern = r"(github.com)\/(\w*)\/(\w*)"
    matches = re.search(pattern, data)
    
    if matches is None:
        return None
    else:
        return "https://{0}.git".format(matches.group(0))

# link needs to be https://github.com/user/repo.git
def run_truffle_hog(githublink):
    pathToRepo = str(Path(__file__).parent.parent.absolute())
    subprocessResult = subprocess.run(['trufflehog', '--include_paths', pathToRepo+'/config/include-patterns.config', '--regex', '--entropy=True', githublink], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = subprocessResult.stdout.decode('utf-8')

    if 'Repository not found' in output:
        return None
    else:
        return output

async def message_secret_nazi_channel(guild, data, githubURL):
    if guild == None or data == None:
        return
    
    if 'secret-nazi-log' not in map(lambda channel : channel.name, guild.text_channels):
        await guild.create_text_channel('secret-nazi-log')

    channel = utils.get(guild.text_channels, name="secret-nazi-log")
    
    messages = list(filter(lambda log : log != "\n" and len(log) > 0 and len(log) < 1950, data.split("~~~~~~~~~~~~~~~~~~~~~")))
    repoName = githubURL.replace('https://github.com/', '')

    await channel.send('Found {0} possible secrets for {1} {2}'.format(len(messages), repoName, LOG_DELIM))
    for message in messages:
        await channel.send(message + LOG_DELIM)
    await channel.send('End {0} {1} '.format(repoName, LOG_DELIM))
    

    