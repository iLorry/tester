# -*- coding: utf-8 -*-

import main
import unittest2 as unittest


class Case(unittest.TestCase):
    @classmethod
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hi(self):
        content = 'hi'
        self.assertEqual(main.hi(content), content, 'test [hi] fail!')


if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, verbosity=2, exit=False)

# vim: noai:ts=4:sw=4
