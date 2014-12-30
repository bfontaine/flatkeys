# -*- coding: UTF-8 -*-

import platform

if platform.python_version() < '2.7':
    import unittest2 as unittest
else:
    import unittest

from flatkeys import flatkeys

class Testflatkeys(unittest.TestCase):

    def test_empty(self):
        self.assertEquals({}, flatkeys({}))

    def test_nested_empty(self):
        self.assertEquals({}, flatkeys({2: {}}))
        self.assertEquals({}, flatkeys({2: {3: {4: {5: {6: {}}}}}}))
        self.assertEquals({}, flatkeys({2: {3: {}, 4: {5: {6: {}}}}}))

    def test_already_flat(self):
        d = {
            1: 42,
            2: True,
            3: None,
            4: [],
            5: "y"
        }
        self.assertEquals(d, flatkeys(d))

    def test_already_flat_with_nested_empty_dict(self):
        d = { 1: 42, 3: None, 4: [] }
        d2 = d.copy()
        d2[2] = {}
        d2[5] = {}
        self.assertEquals(d, flatkeys(d2))

    def test_nested_dict(self):
        self.assertEquals({"1.2.3": 42}, flatkeys({1:{2:{3: 42}}}))

    def test_deeply_nested_dict(self):
        d = {"foo": "bar"}
        n = 1000
        for _ in range(n):
            d = {"x": d}
        k = "x." * n + "foo"
        self.assertEquals({k: "bar"}, flatkeys(d))

    def test_custom_separator(self):
        d = {"a": {"c": 42}}
        self.assertEquals({"abc": 42}, flatkeys(d, sep="b"))
