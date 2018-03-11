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
        assert isinstance(r1[0], str)
        only = 0
        assert "<h2 class=" == r1[only][0:10]
        assert "<h2 class=" == r2[only][0:10]
        assert "<h2 class=" == r3[only][0:10]

    def test_headings(self):
        q = "John 1"
        headings = self.app.headings(q)
        assert "The Word Became Flesh" == headings[0]
        assert "The Testimony of John the Baptist" == headings[1]

    def test_get_instance(self):
        i1 = BibleUtilsApp.get_instance()
        i2 = BibleUtilsApp.get_instance()
        assert True == (i1==i2)
        i3 = BibleUtilsApp()
        assert False == (i1 == i3)
        assert False == (i2 == i3)

