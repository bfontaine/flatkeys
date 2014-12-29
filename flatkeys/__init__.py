# -*- coding: UTF-8 -*-

__version__ = '0.0.1'


def flatkeys(d):
    if type(d) is not dict:
        return d

    flat = {}
    for k, v in d.items():
        if type(v) is dict:
            d2 = flatkeys(v)
            for k2, v2 in d2.items():
                flat["%s.%s" % (k, k2)] = flatkeys(v2)
        else:
            flat[k] = v
    return flat
