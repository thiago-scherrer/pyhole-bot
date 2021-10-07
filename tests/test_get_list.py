#!/usr/bin/env python
import unittest
import os
from context import pyholebot


class TestPihole(unittest.TestCase):
    def setUp(self):
        self.urls = pyholebot.UrlList()

    def test_endpoints_not_found(self):
        os.environ['URL_FILE'] = '42/test_endpoints.txt'
        got = self.urls.get_endpoints()

        expected = "Endpoint file not found!"

        self.assertEqual(got, expected)

    def test_endpoints(self):
        os.environ['URL_FILE'] = 'tests/test_endpoints.txt'
        got = self.urls.get_endpoints()

        expected = ['https://example.com\n']

        self.assertEqual(got, expected)

    def test_blocklist_return(self):
        got = self.urls.get_block_list('https://example.com')

        expected = 'Example Domain'

        self.assertRegex(got, expected)


if __name__ == '__main__':
    unittest.main()
