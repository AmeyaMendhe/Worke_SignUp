Feature: Sign Up page

  Scenario Outline: To verify for existing Email ID
    Given lands on worke page
    When enters first name, last name, Phone number, Password, Confirm Password & Business type
    And enters Email ID that is already registered "<EmailID>"
    And click on Create Account CTA
    Then Error message should be displayed "<Email_already registered_Error_Text>"
    Examples:
    |EmailID                |Email_already registered_Error_Text                      |
    |ameyamendhe13@gmail.com|Email Address already registered|


  Scenario Outline: To verify for existing Business Name
    Given lands on worke page
    When enters first name, last name, Phone number, Password, Confirm Password & Business type
    And enters Business Name that is already registered "<BusinessName>"
    And click on Create Account CTA
    Then Error message should be displayed "<Business_already_registered_Error_Text>"
    Examples:
    |BusinessName                |Business_already_registered_Error_Text                      |
    |tester1|Business Name has already registered|