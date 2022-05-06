from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.maximize_window()
# driver.find_element(By.XPATH,'//input[@id="txtUsername"]').send_keys("Admin")
# driver.find_element(By.XPATH,'//input[@id="txtPassword"]').send_keys("admin123")
# driver.find_element(By.XPATH,'//input[@id="btnLogin"]').click()
# time.sleep(5)
# driver.implicitly_wait(5)
# admin = driver.find_element(By.XPATH,'//a[@id="menu_admin_viewAdminModule"]')
# userAdmin = driver.find_element(By.XPATH,'//a[@id="menu_admin_UserManagement"]')
# user = driver.find_element(By.XPATH,'//a[@id="menu_admin_viewSystemUsers"]')
# actions = ActionChains(driver)  #actions class object
# actions.move_to_element(admin).move_to_element(userAdmin).move_to_element(user).click().perform()
#
# time.sleep(5)
driver.get("https://webdriveruniversity.com/Actions/index.html#")
driver.maximize_window()
Hover = driver.find_element(By.XPATH,'//button[@class="dropbtn"]')
link = driver.find_element(By.XPATH,'//a[text()="Link 1"]')
actions = ActionChains(driver)
actions.move_to_element(Hover).move_to_element(link).click().perform()
#time.sleep(5)
driver.switch_to.alert.accept()
driver.close()

