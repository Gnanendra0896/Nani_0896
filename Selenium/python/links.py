from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demo.guru99.com/test/newtours/")
links = driver.find_elements(By.TAG_NAME,"a")
print("Number of links",len(links)) #print the how many links are available.


for link in links:
    print(link.text)
driver.implicitly_wait(5)
time.sleep(4)
#driver.find_element(By.LINK_TEXT,"REGISTER").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"STER").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()
time.sleep(5)

