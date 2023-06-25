Feature: Sign Up page

  Scenario Outline: To verify for existing Email ID
    Given lands on worke page
    When enters first name, last name, Password, Confirm Password
    And enters Email ID that is already registered "<EmailID>"
    And click on Create Account CTA
    Then Error message should be displayed for Email ID"<Email_Error_Text>"
    Examples:
    |EmailID                |Email_Error_Text                |
    |ameyamendhe13@gmail.com|User with mail already exists   |


  Scenario Outline: To verify for existing Business Name
    Given lands on worke page
    When enters first name, last name, Password, Confirm Password
    And enters Business Name that is already registered "<BusinessName>"
    And click on Create Account CTA
    Then Error message should be displayed for Business Name"<Business_Name_Error_Text>"
    Examples:
    |BusinessName                |Business_Name_Error_Text|
    |tester1|Organisations name already exists|


  Scenario Outline: To verify for existing Phone number
    Given lands on worke page
    When enters first name, last name, Password, Confirm Password
    And enters Phone Number that is already registered"<PhoneNumber>"
    And click on Create Account CTA
    Then Error message should be displayed for Phone Number"<Phone_Number_Error_Text>"
    Examples:
    |PhoneNumber                |Phone_Number_Error_Text|
    |9503535683|Phone Number already exists|
