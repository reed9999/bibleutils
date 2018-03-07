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
        #Is anything else necessary and secure? Read in an md5sum (from a .gitignored file!) and check against it?

    def test_request(self):
        q = "John 1"
        r1 = self.app.request(q)
        q = "Jn 17.1"
        r2 = self.app.request(q)
        q = "Gen 1:17-25"
        r3 = self.app.request(q)
        assert type(r1) == float
        assert r1 == "In the arxe was the logos"
        assert r2 == "some prayer"
        assert r3 == "a great verse"

    def test_get_instance(self):
        self.skipTest("NYI")

    def test_read_key_from_file(self):
        self.skipTest("NYI")

