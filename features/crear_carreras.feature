Feature: Crear Carreras
In order to save information of a career,
As a user
I want to create a career.

Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Create just career name
    Given I login as user "user" with password "password"
    When I create career
      | name        |
      | GEI  |
    Then I'm viewing the details page for career by "user"
