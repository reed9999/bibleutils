# Created by philip at 3/5/18
Feature: Parse headings from arbitrary passage
  We should be able to return the ESV subject headings

  Scenario: Retrieve Matthew 5 and parse the Sermon on the Mount

  When I ask for the subject headings from Matthew 5
    Then I should get a sequence containing Sermon on the Mount, the Beatitudes, etc.
