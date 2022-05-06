from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

drive = webdriver.Chrome()
drive.get("https://webdriveruniversity.com/Actions/index.html#")
drive.maximize_window()
source = drive.find_element(By.XPATH,'//b[text()="DRAG ME TO MY TARGET!"]')
drive.implicitly_wait(4)
destination = drive.find_element(By.XPATH,'//div[@id="droppable"]')
actions = ActionChains(drive)
actions.drag_and_drop(source,destination).perform()
time.sleep(5)
drive.close()
