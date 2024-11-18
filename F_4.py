from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
# driver.find_element(By.NAME, "name").send_keys("Ganesh Malepati")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Ganesh Malepati")
driver.find_element(By.NAME, "email").send_keys("Example@gmail.com")
driver.find_element(By.ID, 'exampleInputPassword1').send_keys("Ganesh@1234")
driver.find_element(By.ID, "exampleCheck1").click()

# Static Dropdowns
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(5)
dropdown.select_by_index(0)
# driver.find_element(By.ID, "exampleFormControlSelect1").send_keys("Male")
time.sleep(10)
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.NAME, "bday").send_keys("06-08-2001")
# driver.find_element(By.CLASS_NAME, "btn-success").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Ganesh")
driver.find_element(By.XPATH, "(//input[@type='text'])[1]").clear()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
time.sleep(20)
assert "Success" in message