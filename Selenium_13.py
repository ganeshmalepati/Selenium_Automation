"""
    Here we are dealing with the CheckBoxes 
    We can Click multiple checkboxes 
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("http://www.tizag.com/htmlT/htmlcheckboxes.php")
driver.maximize_window()
driver.implicitly_wait(5)

def is_element_present(how, what):
    if len(driver.find_elements(by=how, value=what)) == 0:
        return False
    else:
        return True
    
i = 1
while is_element_present(By.XPATH, "//div[4]//input["+str(i)+"]"):
    driver.find_element(By.XPATH, "//div[4]//input["+str(i)+"]").click()
    i += 1
print("Lenght of the CheckBoxs are: {}".format(i-1))

CheckBox = driver.find_element(By.XPATH, "//tbody//tr//div[4]")
Click_CheckBox = CheckBox.find_elements(By.NAME, "sports")
for check in Click_CheckBox:
    print("Before Clicking the CheckBox: {}".format(check.is_selected()))
    check.click()
    print("After Clicking the CheckBox: {}".format(check.is_selected()))
