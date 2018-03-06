#Attempting a better singleton idiom than the one from
# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
#because I don't like having every method be a passthrough to the inner class.

from yaml import load, dump
import csv, re, datetime

class BibleUtilsApp(object):
    __api_key = None
    __instance = None

    def __init__(self):
        pass

    @classmethod
    def api_key(cls):
        if not cls.__api_key:
            cls.__api_key = cls.read_key_from_file()
        return cls.__api_key

    def request(self, q):

        print(self.api_key())
        html = issue_rest_request(self.api_key(), q)
        headings = process_passage_html(html)
        return headings

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = BibleUtilsApp()
        return cls.__instance

    @classmethod
    def read_key_from_file(cls):
        HARDCODED_FILENAME = "__key.txt"
        with open(HARDCODED_FILENAME, 'r') as key_file:
            _ = key_file.readline()
            key = key_file.readline()
        return key


def singleton_demo():
    i1 = BibleUtilsApp.get_instance()
    print (i1)
    i2 = BibleUtilsApp.get_instance()
    print (i2)
    print (i1==i2)
    i3 = BibleUtilsApp()
    print (i3)
    print(i1 == i3)
    print(i2 == i3)

if __name__ == "__main__":
    singleton_demo()
