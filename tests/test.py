# -*- coding: UTF-8 -*-
import sys
import platform

if platform.python_version() < '2.7':
    import unittest2 as unittest
else:
    import unittest

from os.path import dirname

if __name__ == '__main__':
    here = dirname(__file__)
    sys.path.insert(0, here+'/..')

import flatkeys

class TestflatkeysVersion(unittest.TestCase):
    def test_version(self):
        self.assertRegexpMatches(flatkeys.__version__, r'^\d+\.\d+\.\d+')

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover(here)
    t = unittest.TextTestRunner().run(suite)
    if not t.wasSuccessful():
        sys.exit(1)
