# Instead of downloading the chromebrowsers we can directly run them using this service import for the chrome driver and using the ChromeDriverManager
# So this webdriver.chrome.service will the update the and install all the latest version of chrome driver and run the test.




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://en.wikipedia.org/wiki/Sai_Pallavi")
driver.maximize_window()
driver.implicitly_wait(10)
print(driver.title)
print(driver.current_url)
assert "Sai Pallavi" in driver.title


