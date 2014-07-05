import requests
import json
import re

http_base = "http://169.254.169.254/latest/meta-data/"

def get(iam_uri):
    r = re.compile('awsmeta://(?P<meta_path>\S+)$')
    m = r.match(iam_uri)
    if not m:
        return [None, None]

    try:
        http_uri = http_base + m.group('meta_path')
        r = requests.get(http_uri, timeout=0.1)
        content = r.text if r.status_code == 200 else None
        return [r.status_code, content]
    except Exception, e:
        return [{'exception': e}, None]
