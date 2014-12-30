# -*- coding: UTF-8 -*-

__version__ = '0.1.0'


def flatkeys(d, sep="."):
    """
    Flatten a dictionary: build a new dictionary from a given one where all
    non-dict values are left untouched but nested ``dict``s are recursively
    merged in the new one with their keys prefixed by their parent key.

    >>> flatkeys({1: 42, 'foo': 12})
    {1: 42, 'foo': 12}
    >>> flatkeys({1: 42, 'foo': 12, 'bar': {'qux': True}})
    {1: 42, 'foo': 12, 'bar.qux': True}
    >>> flatkeys({1: {2: {3: 4}}})
    {'1.2.3': 4}
    >>> flatkeys({1: {2: {3: 4}, 5: 6}})
    {'1.2.3': 4, '1.5': 6}
    """
    flat = {}
    dicts = [("", d)]

    while dicts:
        prefix, d = dicts.pop()
        for k, v in d.items():
            k_s = str(k)
            if type(v) is dict:
                dicts.append(("%s%s%s" % (prefix, k_s, sep), v))
            else:
                k_ = prefix + k_s if prefix else k
                flat[k_] = v
    return flat
