#!/usr/bin/env python
import unittest
import os
from context import pyholebot


class TestPihole(unittest.TestCase):
    def setUp(self):
        self.urls = pyholebot.UrlList()

    def test_endpoints_not_found(self):
        os.environ['URL_FILE'] = '42/mock_endpoints.txt'
        got = self.urls.get_endpoints()

        expected = "Endpoint file not found!"

        self.assertEqual(got, expected)

    def test_endpoints(self):
        os.environ['URL_FILE'] = 'tests/mock_endpoints.txt'
        got = self.urls.get_endpoints()

        expected = ['https://example.com\n']

        self.assertEqual(got, expected)

    def test_blocklist_return(self):
        got = self.urls.get_block_list('https://example.com')

        expected = 'Example Domain'

        self.assertRegex(got, expected)

    def test_create_blocklist(self):
        got = self.urls.create_blocklist('42')

        expected = 2

        self.assertEqual(got, expected)

    def test_url_normalize_1(self):
        mock = '127.0.0.1 api4.1mobile.com'
        got = self.urls.url_normalizer(mock)

        expected = '\n\napi4.1mobile.com'

        self.assertEqual(got, expected)

    def test_url_normalize_2(self):
        mock = '# [1mobile.com]'
        got = self.urls.url_normalizer(mock)

        expected = '\n'

        self.assertEqual(got, expected)

    def test_url_uniq(self):
        os.environ['BLOCKLIST_OUTPUT'] = '/tmp/uniq.out'
        self.urls.tmpfile = 'tests/mock_uniq_test.txt'

        self.urls.url_uniq()

        f = open('/tmp/uniq.out', 'r')
        got = f.readlines()
        expected = ['example1.com.br\n', 'example3.com.br\n', 'example2.com.br\n']

        self.assertEqual(got, expected)
        os.remove('/tmp/uniq.out')

    def test_cleanup(self):
        os.environ['URL_FILE'] = 'tests/mock_endpoints.txt'
        os.environ['BLOCKLIST_OUTPUT'] = '/tmp/uniq.out'

        got = self.urls.cleanup()

        expected = False

        self.assertEqual(got, expected)

    def test_env_setup(self):
        os.environ['URL_FILE'] = 'tests/mock_endpoints.txt'
        os.environ['BLOCKLIST_OUTPUT'] = '/tmp/uniq.out'

        self.urls.env_setup()

        endpoint = self.urls.endpoint
        output = self.urls.output

        self.assertEqual(endpoint, 'tests/mock_endpoints.txt')
        self.assertEqual(output, '/tmp/uniq.out')


if __name__ == '__main__':
    unittest.main()
