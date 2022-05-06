from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.w3schools.com/html/html_tables.asp")
rows = len(driver.find_elements(By.XPATH,'//*[@id="customers"]/tbody/tr'))
cols = len(driver.find_elements(By.XPATH,'//*[@id="customers"]/tbody/tr[1]/th'))
print(rows)
print(cols)
print("Company"+"               "+"Contact"+"               "+"Country")

for r in range(2,rows+1):
    for c in range(1,cols+1):
        val = driver.find_element(By.XPATH,"//*[@id='customers']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(val,end= '')
    print()