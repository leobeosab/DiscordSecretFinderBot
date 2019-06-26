import re, subprocess
from discord import guild

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
    subprocessResult = subprocess.run(['trufflehog', '--include_paths', 'include-patterns.config', '--regex', '--entropy=True', githublink], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = subprocessResult.stdout.decode('utf-8')

    if "Repository not found" in output:
        return False
    else:
        return True
    

    