import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from behave import *
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=Service(r"C:\Users\ameya\Downloads\chromedriver_win32\chromedriver.exe"))

URL = "https://dev.worke.io/signup"

@given(u'lands on worke page')
def step_impl(context):
    driver.get(URL)
    driver.maximize_window()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='mat-input-2']"))).is_displayed()
    # driver.find_element(By.XPATH, "//*[@id='mat-input-2']").is_displayed()
    # time.sleep(2)
    print("page")


@when(u'enters first name, last name, Phone number, Password, Confirm Password & Business type')
def step_impl(context):
    # time.sleep(2)
    # first name
    driver.find_element(By.ID, "mat-input-0").send_keys("Rachel")
    # Last name
    driver.find_element(By.ID, "mat-input-1").send_keys("Green")
    # Phone Number
    driver.find_element(By.ID, "mat-input-3").send_keys("8999488540")
    # Password
    driver.find_element(By.ID, "mat-input-4").send_keys("Rachel@1")
    # Confirm Password
    driver.find_element(By.ID, "mat-input-5").send_keys("Rachel@1")
    # Business name
    driver.find_element(By.ID, "mat-input-6").send_keys("qa1")
    # Business type
    driver.find_element(By.ID, "mat-input-7").send_keys("Software")


@when(u'enters Email ID that is already registered "{EmailID}"')
def step_impl(context, EmailID):
    print("email")
    # Sendind Existing mail to the mail field
    driver.find_element(By.ID, "mat-input-2").send_keys(EmailID)
    # time.sleep(5)
    print("clicked1")
    # time.sleep(8)
    # CheckBox
    check = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    check.click()
    time.sleep(5)
    print("clicked")


@when(u'click on Create Account CTA')
def step_impl(context):
    print("signup button")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[text()=' Create Account ']")))
    print("not clickable")
    driver.find_element(By.XPATH, "//*[text()=' Create Account ']").click()
    time.sleep(5)


@then(u'Error message should be displayed "Email Address already registered"')
def step_impl(context):
    print("already exist text")
    # driver.find_element(By.)
