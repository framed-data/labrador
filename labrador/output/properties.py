import jprops
import StringIO

def dumps(d):
    out = StringIO.StringIO()
    stringified_d = dict((k, str(v)) for k, v in d.iteritems())
    jprops.store_properties(out, stringified_d)
    return out.getvalue()
