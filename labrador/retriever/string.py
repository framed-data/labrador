import os
import re

r = re.compile('string://(?P<content>\S+)$')

def get(uri):
    m = r.match(uri)

    if not m:
        return [False, None]
    else:
        return [True, m.group('content')]
