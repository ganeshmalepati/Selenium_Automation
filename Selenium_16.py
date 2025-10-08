"""
    1. Frame switching in selenium using "iframes"
    2. When we fill out form or another login activites we switch the tab or window within the same or a new tab
    3. Then we need to switch the frame from main to child frame
    4. By using "switch_to" method we can move parent to child or child to parent iframe or windows
    5. When we use "swithc_to.default_content()" method it comes back to parent or main tab from any other child tab
    6. We can also find how many iframes or present in the DOM refer lines 26 to 29
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_submit_get")
driver.maximize_window()
driver.implicitly_wait(10)

frames = driver.find_elements(By.TAG_NAME, "iframe")

for frame in frames:
    print("Frame ID : {}".format(frame.id))

print(len(frames))

driver.switch_to.frame("iframeResult")
driver.find_element(By.XPATH, "//button[@onclick='myFunction()']").click()





"""
    ---------------------------- HANDLING SWITCH WINDOW -------------------------------------

    Here we are moving to child window and performing some actions like enter some text and clicking on the button
    Then we close the child window and switching back to the main window and closing the main window.

 """


driver.get("https://www.poptin.com/?adw-popup-generator&keyword=how%20to%20create%20website%20popup&gad_source=1&gad_campaignid=876656803&gbraid=0AAAAADKVm9wZAcjjigk2zHEKK3jASdzws&gclid=Cj0KCQjw0Y3HBhCxARIsAN7931U25YiNfNkZH-0W4zX_qjrF4EbSDnFuNC_QF4XBQTUaqDZjdWZzk2MaAqUsEALw_wcB")
driver.maximize_window()
driver.implicitly_wait(5)

windows = driver.window_handles
for window in windows:
    print("Window ID is: {}".format(window))
driver.find_element(By.XPATH, "//li[@id='menu-item-90']//a[contains(text(),'Log In')]").click()

driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.ID, "InputEmail").send_keys("demo123@gmail.com")
driver.find_element(By.ID, "InputPassword").send_keys("Ganesh@123")
driver.close()

