Feature: Editar Facultades
In order to change information of a faculty,
As a user
I want to edit the faculty.

Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Just edit a faculty name
    Given I login as user "user" with password "password"
    When I edit a faculty
      | name        |
      | EPS  |
    Then I'm viewing the details page for faculty by "user"
      | name        |
      | ETSEA |
    And There are 1 faculty edited
