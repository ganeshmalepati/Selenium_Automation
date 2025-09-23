# In this we are selecting checkboxes based on "X_PATH" and finding the selected option using "get_attribute" function of JS.
# By iterating through this we can select the specific option in checkbox




from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


# Handling Checkboxes dynamically
# checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")         #Here we can select multiple elements
# print(len(checkboxes))
# for checkbox in checkboxes:
#     if checkbox.get_attribute("value") == "option2":
#         checkbox.click()
#         assert checkbox.is_selected()
#         break
# time.sleep(5)
# for checkbox in checkboxes:
#     if checkbox.get_attribute("value") == "option3":
#         checkbox.click()
#         assert checkbox.is_selected()
#         break
# time.sleep(5)
# for checkbox in checkboxes:
#     if checkbox.get_attribute("value") == "option1":
#         checkbox.click()
#         assert checkbox.is_selected()
#         break
# time.sleep(10)

# Handling Radio butttons

radiobutton = driver.find_elements(By.CSS_SELECTOR, '.radioButton')
print(len(radiobutton))
radiobutton[0].click()
assert radiobutton[0].is_selected()
time.sleep(5)
radiobutton[1].click()
assert radiobutton[1].is_selected()
time.sleep(5)
radiobutton[2].click()
assert radiobutton[2].is_selected()
time.sleep(10)

assert driver.find_element(By.ID, "displayed-text").is_displayed()
time.sleep(5)
driver.find_element(By.ID, "hide-textbox").click()
time.sleep(5)
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
