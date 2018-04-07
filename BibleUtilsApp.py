#Attempting a better singleton idiom than the one from
# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
#because I don't like having every method be a passthrough to the inner class.

#from yaml import load, dump
#import csv, re, datetime, requests, json
import requests
import json
from bs4 import BeautifulSoup

ESV_URL = 'https://api.esv.org/v3/passage/html/'
class BibleUtilsApp(object):
    __api_key = None
    __instance = None

    def __init__(self, output_file=None):
        self.output_file = output_file

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

    def headings(self, q):
        list_of_dicts = self.request(q)
        if len(list_of_dicts) > 1:
            raise RuntimeError("Multiple queries per request not handled yet. Len: {}".format(len(list_of_dicts)))
        return self.__class__.headings_from_html(list_of_dicts[0])

    def request(self, q):
        json_bytes = self.__class__.issue_rest_request(self.api_key(), q).content
        json_str = json_bytes.decode('utf-8')
        list_of_dicts = self.__class__.process_passage_json(json_str)
        return list_of_dicts

    def write_headings(self, q, param_fn=None):
        default_fn = "/home/philip/Documents/bible/bible-headings.md"
        fn = param_fn or (self.output_file or default_fn)
        headings = self.headings(q)
        with open(fn, 'a') as f:
            f.writelines(map(lambda x: x + '\n', headings))

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
    def process_passage_json(cls, json_str):
        the_json = json.loads(json_str)
        return the_json['passages']

    @classmethod
    def headings_from_html(cls, html):
        soup = BeautifulSoup(html, "html5lib")
        return [h3_tag.contents[0] for h3_tag in soup.find_all('h3')]

if __name__ == "__main__":
    instance = BibleUtilsApp.get_instance()
