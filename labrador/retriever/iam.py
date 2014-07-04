import requests
import json
import re

import awsmeta

http_base = "http://169.254.169.254/latest/meta-data/iam/security-credentials/"

def get(iam_uri):
    """Retrieve IAM creds from AWS metadata; expressed in terms
    of the more general `awsmeta` retriever."""
    r = re.compile('iam://(?P<iam_role>\w+)(/(?P<key>\w+))?')
    m = r.match(iam_uri)
    if not (m and m.group('iam_role')):
        return [None, None]

    meta_uri = "awsmeta://iam/security-credentials/{iam_role}".format(iam_role=m.group('iam_role'))
    status, content = awsmeta.get(meta_uri)

    if status == 200:
        k = m.group('key')
        final_content = json.loads(content)[k] if k else content
        return [status, final_content]
    else:
        return [status, None]
