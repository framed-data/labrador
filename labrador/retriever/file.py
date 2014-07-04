import os
import re

env_regexp = re.compile("file://(?P<path>\S+)$")

def get(uri):
    match = env_regexp.match(uri)
    if not match:
        return [{'error': "`file` retriever called with non-'file://' URI"},
                None]

    try:
        with open(match.group('path'), 'r') as f:
            value = f.read().strip()
            return [True, value]
    except IOError, e:
        return [{'exception': e}, None]
