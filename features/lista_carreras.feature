Feature: Lista Carreras
In order to keep track of careers,
As a user
I want to see a list of all the careers.

Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Just see a list of the careers 
    Given I login as user "user" with password "password"
    When I see the list of the careers
    Then I'm viewing the list of all the careers by "faculty"
