#import unittest
from behave import *
from BibleUtilsApp import BibleUtilsApp
#from tests.test_bibleUtilsApp import TestBibleUtilsApp

use_step_matcher("re")

def read_key_from_file():
    pass

@when("I ask for the subject headings from Matthew 5")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.app = BibleUtilsApp.get_instance()
    Q_MATTHEW_5 = "Matthew 5"
    context.app.request(Q_MATTHEW_5)

@then("I should get the right headings for Matthew 5")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.app is not None
    print(type(context.app))

@when("I ask for the subject headings from the first half of Matthew, Mark, Luke, John, Acts, and Obadiah")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass

@then("I should get the right headings for the first half of Matthew, Mark, Luke, John, Acts, and Obadiah")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass

# There's probably a good case to be made that mixing unit tests into BDD tests here is incoherent.
# Anyway, at present pyunit seems to be passing the tests then exiting ungracefully.
# CF my budget-reed project where this technique seemed to work. Weird.

# @then("Unit tests pass")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     test = TestBibleUtilsApp()
#     #result = unittest.main(TestBibleUtilsApp)
#     assert 0 != "Why is trying to execute unittest.main() exiting unceremoniously???"
#     assert test is not None
#     assert 'intentional fail' == unittest.main(test)
