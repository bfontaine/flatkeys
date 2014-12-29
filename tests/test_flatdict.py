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
        self.assertEquals(lambda:None, flatdict(lambda:None))
