from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.service import Service

#ser = Service("C:\\Users\Gnanendra\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome()
#driver = webdriver.Chrome(service=ser)


driver.get("https://www.flipkart.com/")
# driver.refresh()
# time.sleep(3)
# print('open amazon website')
# driver.maximize_window()
# print('maximize the window')
# account = driver.find_element(By.XPATH,'//a[@id="nav-link-accountList"]')
# sigin = driver.find_element(By.XPATH,'//span[contains(text(),"Sign in")]')
#
# actions = ActionChains(driver)
# actions.move_to_element(account).move_to_element(sigin).click().perform()
#
# driver.find_element(By.XPATH,'//input[@id="ap_email"]').send_keys('+91 8106406494')
# driver.find_element(By.XPATH,'//input[@id="continue"]').click()
# driver.implicitly_wait(4)
# driver.find_element(By.XPATH,'//input[@id="ap_password"]').send_keys('MYRA1325abhi')
# driver.find_element(By.XPATH,'//input[@id="signInSubmit"]').click()
# time.sleep(5)
#
# driver.find_element(By.XPATH,'//a[text() = "Mobiles"]').click()
# print('clicking mobile dashboard')
# driver.execute_script("window.scrollBy(0,850)","")
# time.sleep(3)
# driver.implicitly_wait(4)
# driver.find_element(By.XPATH,'//a[@aria-label="1"]').click()
# print('selecting the mobile')
# driver.execute_script("window.scrollBy(0,600)","")
# time.sleep(3)
# driver.find_element(By.XPATH,'//input[@id="add-to-cart-button"]').click()
# print('add mobile to cart')
# time.sleep(3)
# driver.find_element(By.XPATH,'//a[contains(text(),"Go to Cart")]').click()
# print('go to the cart')
# time.sleep(3)
# driver.find_element(By.XPATH,'//input[@class="a-color-link"]').click()
# print('remove mobile from cart')
# time.sleep(5)
driver.implicitly_wait(5)
#driver.find_element(By.XPATH,'//a[text()="Login"]').click()
driver.implicitly_wait(3)
driver.find_element(By.XPATH,'//input[@class="_2IX_2- VJZDxU"]').send_keys("7989007575")
driver.find_element(By.XPATH,'//input[@class="_2IX_2- _3mctLh VJZDxU"]').send_keys('Gnani@1233')
driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _2HKlqd _3AWRsL"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'(//img[@class="_396cs4  _3exPp9"])[3]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//div[@class="_2kgArB _2CP_Bu"]').click()
driver.find_element(By.XPATH,'(//div[@class="_HYyiu"])[6]').click()
driver.find_element(By.XPATH,'//div[text()="APPLE iPhone 11 (White, 64 GB)"]').click()
driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _2U9uOA _3v1-ww"]').click()
time.sleep(6)

