from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
element = driver.find_element(By.XPATH,'//select[@id="dropdowm-menu-1"]')
drp = Select(element)
driver.implicitly_wait(4)
# select by using visible text
drp.select_by_visible_text('Python')
time.sleep(5)
# select by using index number
drp.select_by_index(3)
time.sleep(5)
# select by using value
drp.select_by_value('c#')
time.sleep(5)

# capturing the how many options are available
print(len(drp.options))

# to fetch the options then print as output
driver.implicitly_wait(5)
all_options = drp.options
for option in all_options:
    print(option.text)
time.sleep(6)




