import requests

def get(uri):
    try:
        r = requests.get(uri, timeout=0.5)
        content = r.text if r.status_code == 200 else None
        return [r.status_code, content]
    except Exception, e:
        return [{'exception': e}, None]
