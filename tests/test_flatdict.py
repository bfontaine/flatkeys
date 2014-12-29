# -*- coding: UTF-8 -*-

import platform

if platform.python_version() < '2.7':
    import unittest2 as unittest
else:
    import unittest

from flatdict import flatdict

class TestFlatdict(unittest.TestCase):

    def test_empty(self):
        self.assertEquals({}, flatdict({}))

    def test_not_a_dict(self):
        self.assertEquals(2, flatdict(2))
        self.assertEquals(False, flatdict(False))
        self.assertEquals([], flatdict([]))
        self.assertEquals(dict, flatdict(dict))
        l = lambda:None
        self.assertEquals(l, flatdict(l))

    def test_nested_empty(self):
        self.assertEquals({}, flatdict({2: {}}))
        self.assertEquals({}, flatdict({2: {3: {4: {5: {6: {}}}}}}))
        self.assertEquals({}, flatdict({2: {3: {}, 4: {5: {6: {}}}}}))

    def test_already_flat(self):
        d = {
            1: 42,
            2: True,
            3: None,
            4: [],
            5: "y"
        }
        self.assertEquals(d, flatdict(d))

    def test_already_flat_with_nested_empty_dict(self):
        d = { 1: 42, 3: None, 4: [] }
        d2 = d.copy()
        d2[2] = {}
        d2[5] = {}
        self.assertEquals(d, flatdict(d2))

    def test_nested_dict(self):
        self.assertEquals({"1.2.3": 42}, flatdict({1:{2:{3: 42}}}))
