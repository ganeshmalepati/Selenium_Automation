"""
    Mouse Handling events in selenium 
    We have different types of mouse events to interact with DOM 
    1. Click and Hold:- This method combines moving the mouse to the center of an element with pressing the left mouse button.
    2. Click and release:- This method combines moving to the center of an element with pressing and releasing the left mouse button. This is otherwise known as “clicking”.
    3. Context_click (Right Click):- This method combines moving to the center of an element with pressing and releasing the right mouse button (button 2). This is otherwise known as “right-clicking”.
    4. Double Click:- This method combines moving to the center of an element with pressing and releasing the left mouse button twice.
    5. Move to Element:- This method moves the mouse to the in-view center point of the element. This is otherwise known as “hovering.” Note that the element must be in the viewport or else the command will error.
    6. Move by offset:- These methods first move the mouse to the designated origin and then by the number of pixels in the provided offset. Note that the position of the mouse must be in the viewport or else the command will error.
    7. Drag and Drop on Element:- This method firstly performs a click-and-hold on the source element, moves to the location of the target element and then releases the mouse.
    ----------------Example code snippet------------------
    action.click_and_hold(menu).perfomr()
    action.click(menu).perfomr()
    action.context_click(menu).perfomr()
    action.double_click(menu).perfomr()
    action.move_to_element(menu).perform()
    ActionChains(driver).move_to_element_with_offset(mouse_tracker, 8, 0).perform()
    action.drag_and_drop(draggable, droppable).perform()
    ActionChains(driver).drag_and_drop_by_offset(slider, 200, 100).perform()

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import logging
import time


# Logger setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
LOG = logging.getLogger(__name__)


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.way2automation.com/welcome-to-cypress-test-automation/")
driver.maximize_window()
driver.implicitly_wait(5)

menu = driver.find_element(By.XPATH, "//li[@id='menu-item-27580']//span[@class='menu-text'][normalize-space()='All Courses']")
LOG.info("Message: {}".format(menu))
action = ActionChains(driver)
action.move_to_element(menu).perform()
Select_Item = driver.find_element(By.XPATH, "//li[@id='menu-item-27592']//a[@class='menu-link']")




"""
    ---------------------------------------Handling Mouse Sliders events---------------------------------
"""


driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
driver.implicitly_wait(10)

main_slider = driver.find_element(By.XPATH, "//span[1]")
location = main_slider.location
size = main_slider.size

w, h = size['width'], size['height']

print(location)
print(size)
print(w, h)


slider = driver.find_element(By.XPATH, "//span[1]")
ActionChains(driver).drag_and_drop_by_offset(slider, 200, 100).perform()



"""
    ---------------------------Handling Right Click events in mouse------------------------------------
"""

driver.get("https://static.worldsoft-cms.info/dlx/examples/deluxe-menu/deluxe-menu.com/popup-mode-sample.html")
driver.maximize_window()
driver.implicitly_wait(10)

click_img = driver.find_element(By.XPATH, "//img[@src='data-samples/images/popup_pic.gif']")
ActionChains(driver).context_click(click_img).perform()
time.sleep(5)

sub_click = driver.find_element(By.XPATH, "//td[@id='dm2m1i1tdT']")
sub_click.click()
LOG.info("Clicked on the first item: {}".format(sub_click))
time.sleep(5)

nxt_sub_click = driver.find_element(By.XPATH, "//td[@id='dm2m2i1tdT']")
nxt_sub_click.click()
LOG.info("Clicking after the first item click: {}".format(nxt_sub_click))
time.sleep(5)

nxt_Nxt_sub_click = driver.find_element(By.XPATH, "//td[@id='dm2m3i1tdT']")
nxt_sub_click.click()
LOG.info("Clicking after the first item click: {}".format(nxt_sub_click))
time.sleep(5)

