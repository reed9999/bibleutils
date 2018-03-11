# Created by philip at 3/5/18
Feature: Parse headings from arbitrary ESV passage
  We should be able to return the ESV subject headings

  Scenario: Retrieve Matthew 5 and parse the Sermon on the Mount

  When I ask for the subject headings from Matthew 5
    Then I should get the right headings for Matthew 5


  Scenario: Retrieve first halves of Matthew, Mark, Luke, John, Acts, and Obadiah

  When I ask for the subject headings from the first half of Matthew, Mark, Luke, John, Acts, and Obadiah
    Then I should get the right headings for the first half of Matthew, Mark, Luke, John, Acts, and Obadiah

#  Scenario: Code base is solid at the unit-test level
#
#    Then Unit tests pass

