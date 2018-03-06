import re, os
from unittest import TestCase
from BibleUtilsApp import BibleUtilsApp


class TestBibleUtilsApp(TestCase):
    #key_fn = "__key.txt"

    def setUp(self):
        self.app = BibleUtilsApp()
        os.chdir(os.path.expanduser("~/code/esv-bible"))

    def test_api_key(self):
        key = self.app.api_key()
        self.assertIsNotNone(re.search('[0-9a-f]{40}', key))

    def test_request(self):
        self.skipTest("NYI")

    def test_get_instance(self):
        self.skipTest("NYI")

    def test_read_key_from_file(self):
        self.skipTest("NYI")

