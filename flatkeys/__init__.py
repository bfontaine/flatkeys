# -*- coding: UTF-8 -*-

__version__ = '0.0.1'


def flatkeys(d):
    if type(d) is not dict:
        return d

    flat = {}
    dicts = [("", d)]

    while dicts:
        prefix, d = dicts.pop()
        for k, v in d.items():
            k_s = str(k)
            if type(v) is dict:
                dicts.append(("%s%s." % (prefix, k_s), v))
            else:
                k_ = prefix + k_s if prefix else k
                flat[k_] = v
    return flat
