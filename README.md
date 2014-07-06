Labrador (Retriever)
====================

A library for pulling strings from a variety of places:

- Files!
- Environment variables!
- AWS Metadata!

This makes it easy to generate configuration data, with some amounts
of smarts since _it's just Python_.  We also include built-in
output formatters to get your data out conveniently.

```python
import labrador as l

config = {
    'hostname': l.get('file:///etc/hostname'),
    'iam_access_key': l.get('iam://my-iam-role/AccessKeyId') or "12345"
}

print l.dumps(config, fmt='yaml')
```

You can also use it straight off the command line as a
Labrador-powered templating engine:

```bash
$ pip install labrador
$ echo 'hello ${file:///etc/hostname}' | lab
```


Built-in Retrievers
-------------------

```python
import labrador as l

l.get('file://test')               # relative file path
l.get('file:///etc/test')          # absolute file path /etc/test

l.get('env://FOO')                 # environment variable `FOO`

l.get('awsmeta://local-ipv4')      # retrieve AWS metadata
l.get('iam://my-role/AccessKeyId') # retrieve IAM credentials

l.get('facter://ipaddress')        # retrieve facter keys
```


Built-in Outputters
-------------------

```python
import labrador as l

l.dumps({'foo': 'bar'}, fmt='json')
l.dumps({'foo': 'bar'}, fmt='yaml')
l.dumps({'foo': 'bar'}, fmt='properties')
l.dumps({'mysection': {'foo': 'bar'}}, fmt='ini')
```


Extension via Dependency Injection
----------------------------------

Both retrievers and outputters are dependency injected, i.e. you
can get your own Labrador instance that inputs or outputs whatever
you want with your own handler:

```python

import labrador

def myhandler(uri):
    status = True
    value = "retrieved from: " + uri
    return (status, value)

l = labrador.Labrador(retrievers={'myprotocol': myfunc})
l.get('myprotocol://myresourceuri')
# => (True, "retrived from: myresoureuri")
```

In other words, a protocol handler is just a function that:

1. Takes a URI
2. Returns a 2-tuple of status information and the retrieved value.

Status information and the retrieved value can be whatever you want.
The only required protocol is that `None` or `False` for `status` or
`value` are always considered failure/lack of information present.


Caching
-------

Labrador comes with built-in caching support.  It is disabled by
default but is enableable by dependency-injecting the cache object:

```python
import labrador
import labrador.cache.yaml_cache

l = labrador.Labrador(
      cache=labrador.cache.yaml_cache.YamlCache('/home/me/.labcache.yml'))

l.get('https://github.com/torvalds.keys') # first time is slow; HTTPS request
l.get('https://github.com/torvalds.keys') # second time is fast; local disk access
```

The built-in local YAML cache is persistent by default; it's just a
file stored on disk that can be re-read.

The caches are modular; they just have the interface:

```python
class MyCache:
    def get(self, key):
        ...

    def put(self, key, value):
        ...
```

So you can make any kind of cache (local, shared, expiring, excluding
certain types of URIs) that you like.
