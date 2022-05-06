from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://demo.automationtesting.in/Windows.html")
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//button[text()="    click   "]').click()
time.sleep(5)
print(driver.current_window_handle) #CDwindow-804BDF07270EF4C13504A5D699E66344--parent
handles =driver.window_handles      # it will return the multiple handle value of opened browser windows


for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == 'Frames & windows':
        driver.close()
driver.quit()