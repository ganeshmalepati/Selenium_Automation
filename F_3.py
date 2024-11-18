from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
time.sleep(10)
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")           # Here we are finding the path from parent to child like "/form/div/input" like this
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@123") # For Selector we need to use "space( )" for find the path"
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys("Hello@123")
time.sleep(5)
# driver.find_element(By.XPATH, "//button[@type='submit']").click()  # In this we are finding by Path 
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()  #In this based on "X_Path also we can find the locator by using thier names insead of "id", "CSS_Selector" and "class"
time.sleep(20)
  
