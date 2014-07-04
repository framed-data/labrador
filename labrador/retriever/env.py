import os
import re

env_regexp = re.compile("env://(.*)$")

def _get(env_var):
    return os.environ.get(env_var)

def get(uri):
    match = env_regexp.match(uri)
    status = match.group(0) if match else None
    value = _get(match.group(1)) if status else None
    return [status, value]
