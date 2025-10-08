"""
    Handling Alerts in Selenium 
    1. To capture the alret message we need to import Alert "from selenium.webdriver.common.alert" 
    2. Methods used to interacte with alerts are "switch_to.alert"
    3. To get the text present in the alert pop-up we can use "alert.text".
    Mehtods in alert are :
    alert.text
    alert.accept()
    alert.dismiss()
"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
import logging
import time


# Logger setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
LOG = logging.getLogger(__name__)


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.selenium.dev/selenium/web/alerts.html#")
driver.maximize_window()
driver.implicitly_wait(5)


pop_up = driver.find_element(By.XPATH, "//a[@id='prompt']").click()
LOG.info("Clicked on the prompt alert button.")

alert = driver.switch_to.alert
print(alert.text)
LOG.info("Warning Message: {}".format(alert.text))
time.sleep(5)
alert.send_keys("Ganesh")
time.sleep(5)
alert.accept()
LOG.info("Accepted the alert.")