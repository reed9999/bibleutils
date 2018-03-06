#Attempting a better singleton idiom than the one from
# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
#because I don't like having every method be a passthrough to the inner class.

from yaml import load, dump
import csv, re, datetime

class BibleUtilsApp(object):
    __instance = None

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = BibleUtilsApp()
        return cls.__instance


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
