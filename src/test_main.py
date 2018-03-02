# -*- coding: utf-8 -*-

import os
import unittest2 as unittest
import main

runtime = './runtime/'


class Case(unittest.TestCase):
    @classmethod
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_mkdir_true(self):
        target = runtime + 'test_mkdir/'
        expected = True
        if os.path.exists(target):
            os.removedirs(target)
        self.assertEqual(
            main.mkdir(target), expected, 'test [mkdir_true] fail!')

    def test_mkdir_false(self):
        target = runtime + 'test_mkdir/'
        expected = False
        if not os.path.exists(target):
            os.makedirs(target)
        self.assertEqual(
            main.mkdir(target), expected, 'test [mkdir_false] fail!')


if __name__ == '__main__':
    main.mkdir(runtime)

    import xmlrunner

    #unittest.main(module=__name__, buffer=True, verbosity=2, exit=False)

    with open(runtime + 'test-results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            module=__name__,
            buffer=True,
            verbosity=2,
            exit=False)

# vim: noai:ts=4:sw=4
