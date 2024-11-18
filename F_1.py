from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Sai_Pallavi")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(30)


