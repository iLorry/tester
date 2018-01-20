# -*- coding: utf-8 -*-

import main
import unittest2 as unittest

# pip install unittest2
# pip install xmlrunner
# pip install unittest-xml-reporting


class Case(unittest.TestCase):
    @classmethod
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hi(self):
        content = 'ping'
        expected = 'pong'
        self.assertEqual(main.hi(content), expected, 'test [hi] fail!')


if __name__ == '__main__':
    runtime = './runtime/'
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
