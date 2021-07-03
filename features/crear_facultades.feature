Feature: Crear Facultades
In order to save information of falcutys,
As a user
I want to create facultys.

Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Create just a faculty name
    Given I login as user "user" with password "password"
    When I create faculty
      | name        |
      | EPS  |
    Then I'm viewing the details page for faculty by "user"
