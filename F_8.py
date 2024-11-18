from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
actual_items = []
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(1)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
print(count)
for result in results:
    actual_items.append(result.find_element(By.CLASS_NAME, "product-name").text)
    result.find_element(By.XPATH, "div/button").click()  # In this the search element is within the result 
print(actual_items)
    
driver.find_element(By.CSS_SELECTOR, ".search-keyword").clear()

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("Ca")
time.sleep(5)
Ca_items = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(Ca_items)
print(count)
actual_items_Ca = []
for item in Ca_items:
    actual_items_Ca.append(item.find_element(By.CLASS_NAME, "product-name").text)
    item.find_element(By.XPATH, "div/button").click()
print(actual_items_Ca)
# driver.find_element(By.XPATH, "(//div[@class='products']/div/div/button)[1]").click()  # It is a normal method
# driver.find_element(By.XPATH, "(//div[@class='products']/div/div/button)[2]").click()
# driver.find_element(By.XPATH, "(//div[@class='products']/div/div/button)[3]").click()
time.sleep(5)

# driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "div[class='cart-preview active'] button[type='button']").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
time.sleep(10)
driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']").click()
driver.find_element(By.XPATH, "(//select)[1]").click()
driver.find_element(By.XPATH, "(//select)[1]").send_keys("India")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "div[class='wrapperTwo'] button").click()
time.sleep(5)


#If we have written any element with driver.find_element it will search the entire web driver
#If we want to search any element with the div or any particular tag we can go with result.find_element the we can get those particular element inside that tag
