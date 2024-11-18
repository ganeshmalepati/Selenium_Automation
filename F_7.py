# Browser based alret messages in  Java and Js with the help of accept/dismiss and "switch_to" methods.

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
name = "Ganesh Malepati"

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
time.sleep(5)
alertmsg = driver.switch_to.alert
Alerttext = alertmsg.text
print(Alerttext)
assert name in Alerttext
alertmsg.accept()
# print(Alerttext)
time.sleep(10)