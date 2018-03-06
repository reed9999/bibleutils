from behave import *
from BibleUtilsApp import BibleUtilsApp

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
    return

    key = read_key_from_file()
    #This looks like implementation details that shouldn't be in the behavioral test.
    html = issue_rest_request(key, q)
    headings = process_passage_html(html)



@then("I should get a sequence containing Sermon on the Mount, the Beatitudes, etc\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    print("The variable value is: " + str(context.app))

