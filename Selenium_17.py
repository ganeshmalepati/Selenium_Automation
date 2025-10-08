"""
    Capturing the ScreenShot in selenium webdriver using three differnt ways
    1. Using the direct method "save_screenshot()
    2. Using the reference name with screenshot method like :- check "element.screenshot("./screenshot/submit.png")"
    3. By creating a custom method for mutiple usecase and creating unique screenshot name
    Here "switch_to" is used to switch from one frame to another frame which are present in different DOM
    And "switch_to.default_content()" moves to main windowo or main tab

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
# import logging
import time


# # Logger setup
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# LOG = logging.getLogger(__name__)


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_submit_get")
driver.maximize_window()
driver.implicitly_wait(10)


"""
    Based on the below method we can capture the screenshot in timestramp format by changing it from ":" to "_".
    This generates a unique screenshot name for all time
    It can be used in multiple times
"""

def capture_screenshot(d, path):
    file_name = path+"screenshot_"+time.asctime().replace(":", "_")+".png"
    d.save_screenshot(file_name)


"""
    This is the beginer method to capture screenshot using save_screenshot funtion in selenium
"""

driver.save_screenshot("./screenshot/error.png")

driver.switch_to.frame("iframeResult")     
driver.execute_script("myFunction()")                  # In this line we execute the click on tab button with javascript code snippet
time.sleep(5)

element = driver.find_element(By.ID, "mySubmit")
element.screenshot("./screenshot/submit.png")
driver.execute_script("arguments[0].style.border='3px solid red'", element)   # Here we are highlighting the Submit button with red colour
time.sleep(5)
capture_screenshot(driver, "./screenshot/")

driver.switch_to.default_content()
driver.quit()

