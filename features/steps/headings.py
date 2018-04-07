#import unittest
from behave import *
from BibleUtilsApp import BibleUtilsApp
from hamcrest import assert_that, equal_to

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
    the_app = context.app
    assert the_app is not None
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
@when("I ask for the subject headings from Numbers first half then second half")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.app = BibleUtilsApp.get_instance()
    app = context.app
    Q_NUMBERS_FIRST_HALF = "Numbers 1-18"
    Q_NUMBERS_SECOND_HALF = "Numbers 19-36"
    context.numbers_fn = "/home/philip/Documents/bible/numbers-{0:02d}.md"
    app.write_headings(Q_NUMBERS_FIRST_HALF, context.numbers_fn.format(1))
    headings = app.write_headings(Q_NUMBERS_SECOND_HALF, context.numbers_fn.format(2))



@then("I should get the right headings for Numbers")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    with open(context.numbers_fn.format(1)) as f:
        all_lines = f.readlines()
        assert_that(all_lines[5].rstrip(), equal_to("Redemption of the Firstborn"))
        assert_that(all_lines[10].rstrip(), equal_to("The Nazirite Vow"))
        assert_that(all_lines[-1].rstrip(), equal_to("Footnotes"))
        assert_that(all_lines[-15].rstrip(), equal_to("Miriam and Aaron Oppose Moses"))


@step("The verses should not be cached\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass