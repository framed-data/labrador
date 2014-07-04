import ConfigParser
import StringIO
import collections

def dumps(d):
    config = ConfigParser.ConfigParser()
    out = StringIO.StringIO()

    for section_name, section in d.iteritems():
        config.add_section(section_name)
        try:
            for k, v in section.iteritems():
                config.set(section_name, k, v)
        except AttributeError, e:
            raise Exception(
              """Expected a dict describing an INI section; got a value.
              Expected structure: {'section': {'key': 'value'}}""")
    config.write(out)

    return out.getvalue()
