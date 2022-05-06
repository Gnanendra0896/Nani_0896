from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

drive = webdriver.Chrome()
drive.get("https://webdriveruniversity.com/File-Upload/index.html") 
drive.find_element(By.XPATH,'//input[@id="myFile"]').send_keys("C://Users/Gnanendra/Pictures/profile.png")
time.sleep(5)
drive.find_element(By.XPATH,'//input[@id="submit-button"]').click()
time.sleep(5)
drive.switch_to.alert.accept()
drive.close()