# In this we can select elements by five froms like "By.Id", "By.name", "By.Class_Name", "By.CSS_SELECTOR", "By.XPATH"
#If you want to select any radio button we can use direct "CSS_SELECTOR" like "#inlineRadio1" (#id) or ".classname"
#If you have multiple X_PATH and you need to select some specific one we can use "(//input[@type=text])[number]"
#syntax for X_PATH = //input[@type=text] for single path 
#syntax for CSS_SELECTOR = input[type=text]

# So based on the below locators we can find and get interact with any element in the webbrowser
#-----------------------------LOCATORS--------------------------
# id = 
# name = 
# css selector = 
# xpath = 
# tagName =
# className = 
# linkText = 
# partialLinkText =


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
driver.implicitly_wait(20)                    # It's applicable for all the elements in the DOM or web-browser.
Wait = WebDriverWait(driver, 5)

# driver.find_element(By.NAME, "name").send_keys("Ganesh Malepati")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Ganesh Malepati")  # 1st Method  Best pratices
username = driver.find_element(By.CSS_SELECTOR, "input[name='name']")                    # 2nd Method 
username.send_keys("Ganesh Malepati")

driver.find_element(By.NAME, "email").send_keys("Example@gmail.com")
driver.find_element(By.ID, 'exampleInputPassword1').send_keys("Ganesh@1234")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.ID, "exampleFormControlSelect1").send_keys("Male")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.NAME, "bday").send_keys("06-08-2001")
# driver.find_element(By.CLASS_NAME, "btn-success").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Ganesh")
driver.find_element(By.XPATH, "(//input[@type='text'])[1]").clear()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message