import re

def get_github_string(data):
    pattern = r"(github.com)\/(\w*)\/(\w*)"
    matches = re.search(pattern, data)
    
    if matches is None:
        return None
    else:
        return matches.group(0)