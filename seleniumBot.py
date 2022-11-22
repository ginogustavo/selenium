# import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# PATH = r"/opt/chromedriver"
# driver = webdriver.Chrome(PATH)

chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

driver.get("https://www.seleniumeasy.com/")

driver.implicitly_wait(3)  # time.sleep(30) is inefficient, bc not always we want to wail 30 secs.

my_element = driver.find_element(By.LINK_TEXT,"View All...")
my_element.click()

# title = driver.find_element(By.CLASS_NAME, "panel-body")
# # print(title.text)
# print(f"{'Factory' in title.text}")

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME,"panel-body"), # Element filtration
        'Factory'# the expected text
    )
)

# driver.close() # close the tab
# driver.quit() # close the entire browser
