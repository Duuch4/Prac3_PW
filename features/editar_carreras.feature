Feature: Editar Carreras
In order to change information of the careers,
As a user
I want to edit the careers.

Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Just edit a career name
    Given I login as user "user" with password "password"
    When I edit a career
      | name        |
      | GEI  |
    Then I'm viewing the details page for career by "user"
      | name        |
      | GEM |
    And There are 1 career edited
    
