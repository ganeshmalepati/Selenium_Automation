import pytest
from selenium import webdriver
import time



def test_launch_pallavi_page():
    driver = webdriver.Chrome()
    driver.get("https://en.wikipedia.org/wiki/Sai_Pallavi")
    driver.maximize_window()
    print(driver.title)
    print(driver.current_url)
    assert "Sai Pallavi" in driver.title
    time.sleep(30)






# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager



# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#     yield driver
#     driver.quit()

# def test_open_wikipedia(driver):
#     driver.get("https://en.wikipedia.org/wiki/Sai_Pallavi")
#     driver.maximize_window()
#     assert "Sai Pallavi" in driver.title
