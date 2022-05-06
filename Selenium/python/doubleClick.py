from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

drive = webdriver.Chrome()
drive.get("https://webdriveruniversity.com/Actions/index.html#")
drive.maximize_window()
ele = drive.find_element(By.XPATH,'//div[@class="div-double-click"]')
actions = ActionChains(drive)
actions.double_click(ele).perform()
time.sleep(7)
#drive.close()