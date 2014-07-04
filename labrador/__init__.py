"""Labrador (Retriever)

A library for conveniently retrieving configuration data
from a variety of sources.

defines abstraction:
- get(uri) => (status, value)
"""

import re
import labrador.retriever.string
import labrador.retriever.file
import labrador.retriever.env
import labrador.retriever.http
import labrador.retriever.iam

import json
import yaml
import labrador.output.properties
import labrador.output.ini

class Labrador:
    def __init__(self,
                 retrievers={
                     'string': labrador.retriever.string.get,
                     'env': labrador.retriever.env.get,
                     'file': labrador.retriever.file.get,
                     'http': labrador.retriever.http.get,
                     'https': labrador.retriever.http.get,
                     'iam': labrador.retriever.iam.get,
                     'awsmeta': labrador.retriever.awsmeta.get}):
        self.retrievers = retrievers
        self.regexp = re.compile("(?P<protocol>.*)://(\S+)$")

    def get(self, uri):
        match = self.regexp.match(uri)
        protocol = match.group('protocol') if match else 'string'
        retriever = self.retrievers.get(protocol)

        if retriever:
            status, value = retriever(uri)
            return [protocol, status, value]
        else:
            return [None, None, None]

def get(uri):
    """Convenience caller"""
    l = Labrador()
    return l.get(uri)[2]

def dumps(d,
        fmts={
            'json': json.dumps,
            'yaml': yaml.dump,
            'properties': labrador.output.properties.dumps,
            'ini': labrador.output.ini.dumps},
        fmt='json'):
    return fmts[fmt](d) 
