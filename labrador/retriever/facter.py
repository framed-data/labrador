import os
import re
import subprocess
import yaml

env_regexp = re.compile("facter://(?P<key>\S+)$")

def get(uri):
    match = env_regexp.match(uri)
    if not match:
        return [{'error': "`facter` retriever called with non-'facter://' URI"},
                None]

    try:
        output = subprocess.check_output(["facter", "--yaml"])
        yaml_output = yaml.load(output)
        return [True, yaml_output.get(match.group('key'))]
    except subprocess.CalledProcessError, e:
        return [{'exception': e}, None]
