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
import labrador.retriever.facter

import json
import yaml
import labrador.output.properties
import labrador.output.ini

class Labrador:
    def __init__(self,
                 retrievers={
                     'string': labrador.retriever.string.get,
                     'env': labrador.retriever.env.get,
                     'facter': labrador.retriever.facter.get,
                     'file': labrador.retriever.file.get,
                     'http': labrador.retriever.http.get,
                     'https': labrador.retriever.http.get,
                     'iam': labrador.retriever.iam.get,
                     'awsmeta': labrador.retriever.awsmeta.get},
                 cache=None):
        self.retrievers = retrievers
        self.regexp = re.compile("(?P<protocol>.*)://(\S+)$")
        self.cache = cache

    def get(self, uri):
        match = self.regexp.match(uri)
        protocol = match.group('protocol') if match else 'string'

        cache_retriever = self.cache.get if self.cache else None
        retriever = self.retrievers.get(protocol)

        # check cache first if one registered
        if cache_retriever:
            status, value = cache_retriever(uri)
            if value:
                return ['cache', status, value]

        if retriever:
            status, value = retriever(uri)
            if value:
                if self.cache:
                    self.cache.put(uri, value)
                return [protocol, status, value]

        return [None, None, None]

    def g(self, uri):
        """Convenient caller than only returns a value, not status info"""
        return self.get(uri)[2]

def get(uri):
    """Module-level convenience caller"""
    return Labrador().g(uri)

def g(uri):
    """Module-level convenience caller"""
    return Labrador().g(uri)

def dumps(d,
        fmts={
            'json': json.dumps,
            'yaml': yaml.dump,
            'properties': labrador.output.properties.dumps,
            'ini': labrador.output.ini.dumps},
        fmt='json'):
    return fmts[fmt](d) 
