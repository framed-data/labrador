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
    'host': l.get(
}

print l.dumps(config, fmt='yaml')
```

You can also use it straight off the command line:

```bash
$ lab iam://my-iam-role/AccessKeyId
```

Extension via Dependency Injection
----------------------------------
