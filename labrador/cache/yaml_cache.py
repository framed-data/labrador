import os
import yaml

class YamlCache:
    def __init__(self, cache_path):
        self.cache_path = cache_path
        try:
            if not os.path.exists(self.cache_path):
                with open(self.cache_path, 'w') as f:
                    f.write(yaml.dump({}))
            else:
                with open(self.cache_path, 'r') as f:
                    yaml.load(f.read())
        except IOError, e:
            print "Couldn't initialize cache path '%s'" % self.cache_path
            print e
            raise
        except yaml.YAMLError, e:
            print "Specified cache path is not a valid YAML map"
            print self.cache_path
            print e
            raise

    def get(self, uri):
        with open(self.cache_path, 'r') as f:
            cache = yaml.load(f.read()) or {}
            return [True, cache.get(uri)]

    def put(self, uri, value):
        f = open(self.cache_path, 'r')
        cache = yaml.load(f.read()) or {}
        f.close()

        cache[uri] = value

        with open(self.cache_path, 'w') as fw:
            fw.write(yaml.dump(cache))
