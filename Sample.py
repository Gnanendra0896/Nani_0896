from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()
driver.get("https://webdriveruniversity.com/Popup-Alerts/index.html")
driver.find_element(By.XPATH,'//span[@id="button4"]').click()
time.sleep(5)
#driver.switch_to.alert.accept() #to click ok button
driver.switch_to.alert.dismiss() # to click the cancel button

time.sleep(5)