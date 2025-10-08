"""
    In this file we are handling the DropDowns
"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
driver.implicitly_wait(5)

#-------------------METHOD_1--------------------------
'''
    In below method we are checking whether the element is present or not 
    It's custom method that we are creating for our purpose
    Here we using ID as an arugment to pass and check with the ID 
'''

def is_element_present(ID):
    try:
        driver.find_elements(By.ID, "searchLanguage")
        return True
    except NoSuchElementException:
        return False
print(is_element_present(By.ID))



# ------------------------METHOD_2------------------------------
"""
    It's similar to the above method but we are passing two positional arguments here "how" and "What"
    In place of "what" we can pass ID or Xpath whatever related to the locator element and how is "By.ID" or"By.XPATH"
"""

def is_element_present(how, what):
    if len(driver.find_elements(by=how, value=what)) == 0:
        return False
    else:
        return True

print(is_element_present(By.ID, "searchLanguage"))

