from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
#driver.
driver.switch_to.frame('packageListFrame')  #first frame
time.sleep(5)
driver.execute_script('window.scrollBy(0,250)','')
#driver.find_element(By.LINK_TEXT,"org.openqa.selenium.devtools.events")
#driver.find_element(By.XPATH,'//a[text()="org.openqa.selenium.events"]').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'events').click()
time.sleep(5)
driver.switch_to.default_content()
time.sleep(5)
driver.switch_to.frame('packageFrame')  #second Frame
#driver.find_element(By.PARTIAL_LINK_TEXT,'WrapsDriver').click()
driver.find_element(By.XPATH,'//a[text()="CdpEventTypes"]').click()
time.sleep(5)
driver.switch_to.default_content()
driver.switch_to.frame('classFrame')  #third frame
driver.find_element(By.XPATH,'//a[text()="Deprecated"]').click()
time.sleep(5)
