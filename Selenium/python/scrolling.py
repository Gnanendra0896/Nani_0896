from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()
driver.get("https://webdriveruniversity.com/")
driver.maximize_window()
#scroll down page by pixel
#driver.execute_script("window.scrollBy(0,200)","")
#driver.execute_script("window.scrollBy(0,1020)","")
time.sleep(5)
#scroll down page till the element is visible

flag = driver.find_element(By.XPATH,'//h1[text()="PAGE OBJECT MODEL"]')
driver.execute_script("arguments[0].scrollIntoView();",flag)
time.sleep(5)
#scroll down page till end

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
