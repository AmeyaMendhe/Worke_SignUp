import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=Service(r"C:\Users\ameya\Downloads\chromedriver_win32\chromedriver.exe"))

URL = "https://dev.worke.io/signup"

@given(u'lands on worke page')
def step_impl(context):
    driver.get(URL)
    driver.maximize_window()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "mat-input-2"))).is_displayed()

    print("page")


@when(u'enters first name, last name, Password, Confirm Password')
def step_impl(context):
    # first name
    driver.find_element(By.ID, "mat-input-0").send_keys("Rachel")
    # Last name
    driver.find_element(By.ID, "mat-input-1").send_keys("Green")
    # Password
    driver.find_element(By.ID, "mat-input-4").send_keys("Rachel@1")
    # Confirm Password
    driver.find_element(By.ID, "mat-input-5").send_keys("Rachel@1")
    # Scrolling down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # Clicking on DropDown
    driver.find_element(By.ID, "mat-select-value-3").click()
    # Selecting Business Name
    driver.find_element(By.ID, "mat-option-223").click()


@when(u'enters Email ID that is already registered "{EmailID}"')
def step_impl(context, EmailID):
    print("email")
    # Sending Existing mail to the mail field
    driver.find_element(By.ID, "mat-input-2").send_keys(EmailID)
    # Business name
    driver.find_element(By.ID, "mat-input-6").send_keys("qa1")
    # Phone Number
    driver.find_element(By.ID, "mat-input-3").send_keys("8999488540")
    driver.find_element(By.ID, "exampleCheck1").click()


@when(u'click on Create Account CTA')
def step_impl(context):
    print("signup button")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[text()=' Create Account ']")))
    driver.find_element(By.XPATH, "//*[text()=' Create Account ']").click()


@then(u'Error message should be displayed for Email ID"{Email_Error_Text}"')
def step_impl(context,Email_Error_Text):
    print("already exist text")

    Current_error_text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "toast-container"))).text

    print(Current_error_text)
    time.sleep(3)
    assert Email_Error_Text == Current_error_text
# --------------------------------------------------------------------------------------------------

@when(u'enters Business Name that is already registered "{BusinessName}"')
def step_impl(context, BusinessName):
    # Sending Business Name
    driver.find_element(By.ID, "mat-input-6").send_keys(BusinessName)
    # Email ID
    driver.find_element(By.ID, "mat-input-2").send_keys("rossgeller@gmail.com")
    # Phone Number
    driver.find_element(By.ID, "mat-input-3").send_keys("8999488540")
    # Scrolling to the Bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.find_element(By.ID, "exampleCheck1").click()


@then(u'Error message should be displayed for Business Name"{Business_Name_Error_Text}"')
def step_impl(context,Business_Name_Error_Text):
    print("already exist text")

    Current_error_text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "toast-container"))).text

    print(Current_error_text)
    time.sleep(3)
    assert Business_Name_Error_Text == Current_error_text

    # ----------------------------------------------------


@when(u'enters Phone Number that is already registered"{PhoneNumber}"')
def step_impl(context, PhoneNumber):
    # Sending Business Name
    driver.find_element(By.ID, "mat-input-6").send_keys("testing9")
    # Email ID
    driver.find_element(By.ID, "mat-input-2").send_keys("joey.bing@gmail.com")
    # Phone Number
    driver.find_element(By.ID, "mat-input-3").send_keys(PhoneNumber)
    # Scrolling to the Bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.find_element(By.ID, "exampleCheck1").click()


@then(u'Error message should be displayed for Phone Number"{Phone_Number_Error_Text}"')
def step_impl(context,Phone_Number_Error_Text):
    print("already exist text")

    Current_error_text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "toast-container"))).text

    print(Current_error_text)
    time.sleep(3)
    assert Phone_Number_Error_Text == Current_error_text