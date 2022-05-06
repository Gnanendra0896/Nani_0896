from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
status = driver.find_element(By.XPATH,'(//input[@name="color"])[1]').is_selected()
driver.implicitly_wait(5)
print(status)
driver.find_element(By.XPATH,'(//input[@name="color"])[1]').click()
status = driver.find_element(By.XPATH,'(//input[@name="color"])[1]').is_selected()
driver.implicitly_wait(5)
time.sleep(5)
print(status)
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'(//input[@type="checkbox"])[1]').click()
driver.implicitly_wait(5)

#driver.find_element(By.XPATH,'(//input[@type="checkbox"])[3]').clear()

driver.find_element(By.XPATH,'(//input[@type="checkbox"])[4]').click()
driver.implicitly_wait(6)
time.sleep(5)


