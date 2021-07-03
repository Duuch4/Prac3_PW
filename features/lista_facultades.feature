Feature: Lista Facultades
In order to keep track of facultys,
As a user
I want to see a list of all the facultys.

Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Just see a list of the facultys
    Given I login as user "user" with password "password"
    When I see the list of the facultys
      | name        |
      | Facultys  |
    Then I'm viewing the list of all the facultys
