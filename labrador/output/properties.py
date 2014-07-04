import jprops
import StringIO

def dumps(d):
    out = StringIO.StringIO()
    jprops.store_properties(out, d)
    return out.getvalue()
