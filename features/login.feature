Feature: Check the functionality of the login page

# Scenariul 1: username corect + parola corecta
# Scenariul 2: username corect + parola incorecta
# Scenariul 3: username incorect + parola corectabehave

# Scenariul 4: username incorect + parola incorecta
# Scenariul 5: username None + parola corecta
# Scenariul 6: username None + parola incorecta
# Scenariul 7: username corect + parola None
# Scenariul 8: username incorect + parola None
# Scenariul 9: username None + parola None
# Scenraiul 10: username blocat (locked_out_user) + parola corecta

  Scenario: Check that you can login into the application when providing correct credentials
    Given I am on the saucedemo login page
    When I insert correct username and correct password
    And I click the login button
    Then I can login into the application and see the list of products

  Scenario: Check that you can not login into the application when providing correct username and incorrect password
    Given I am on the saucedemo login page
    When I insert correct username and incorrect password
    And I click the login button
    Then I cannot login into the application and I receive Epic sadface: Username and password do not match any user in this service error

  Scenario: Check that you can not login into the application when providing incorrect username and correct password
    Given I am on the saucedemo login page
    When I insert incorrect username and correct password
    And I click the login button
    Then I cannot login into the application and I receive Epic sadface: Username and password do not match any user in this service error



