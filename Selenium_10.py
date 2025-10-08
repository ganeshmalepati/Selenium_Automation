from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
driver.implicitly_wait(10)
Drop_down = driver.find_element(By.XPATH, "//select[@id='searchLanguage']")         # find_element() will fetch only a single web element i.e searchLanguage
select = Select(Drop_down)
select.select_by_visible_text("Eesti")
Value = driver.find_elements(By.TAG_NAME, "option")             # find_elements() method will get the all elements present in that tag name


"""
    In the below code we are printing the text and the Lang from the dropdown box.
    All the text and Lang present in that dorpdown will get and print using the get_attribute() method.
"""

for option in Value:
    print("Option value is: {}".format(option.text)    +     "Lang is : {}".format(option.get_attribute("lang")))
print("Length of the language is : {}".format(len(Value)))



print("------------------------------------Printing Links and Elements Present in the Site----------------------------------------")

"""
    In the below lines of code we are trying to print the Element text and their URL
    The elements which are visible in the webbrowser will get print their name and the related URL 
    Based on this the "Tag_name" we have is "a" and for "URL link" we use "href" get_attribute() method
"""

links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print("Text : {}".format(link.text) + "--------URL---------" + "URL Link : {}".format(link.get_attribute("href")))


driver.quit()