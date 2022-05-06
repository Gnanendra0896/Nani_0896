from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8080/")
driver.maximize_window()
#driver.save_screenshot("C:\\Users\\Gnanendra\\Pictures\\Saved Pictures\\jenkinshomepage.png")
time.sleep(3)
driver.get_screenshot_as_file("C:\\Users\\Gnanendra\\Pictures\\Saved Pictures\\jenkinshomepage2.png")
driver.close()
