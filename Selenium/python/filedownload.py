from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.find_element(By.XPATH,'//textarea[@id="textbox"]').send_keys('Nani')
driver.find_element(By.XPATH,'//button[@id="createTxt"]').click()
driver.find_element(By.XPATH,'//a[@id="link-to-download"]').click()
time.sleep(4)

driver.find_element(By.XPATH,'//textarea[@id="pdfbox"]').send_keys('Gnanendra')
driver.find_element(By.XPATH,'//button[@id="createPdf"]').click()
driver.find_element(By.XPATH,'//a[@id="pdf-link-to-download"]').click()
time.sleep(5)
driver.close()