#Attempting a better singleton idiom than the one from
# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
#because I don't like having every method be a passthrough to the inner class.

from yaml import load, dump
import csv, re, datetime, requests

ESV_URL = 'https://api.esv.org/v3/passage/html/'
class BibleUtilsApp(object):
    __api_key = None
    __instance = None

    def __init__(self):
        pass

    #I wrongly had this as a singleton. If we had two different app instances (i.e. didn't use get_instance()) then we
    # might want them to have two different user accounts hence two keys.
    def api_key(self):
        if not self.__api_key:
            self.__api_key = self.read_key_from_file()
        return self.__api_key

    @classmethod
    def issue_rest_request(cls, key, q):

        json = requests.get("{}?q={}".format(ESV_URL, q), headers={'Authorization': 'Token {}'.format(key)})
        return json



    def request(self, q):
        json = self.__class__.issue_rest_request(self.api_key(), q).content
        headings = self.__class__.process_passage_json(json)
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
            key = key_file.readline()[:-1]
        return key

    @classmethod
    def process_passage_json(cls, json):
        print ("Here's the json" + json)
        pass


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
