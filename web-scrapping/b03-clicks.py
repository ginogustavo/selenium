from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.techwithtim.net")
driver.implicitly_wait(3)
link = driver.find_element(By.LINK_TEXT,'Java Programming')

# If element selected is an input , you can clear it first.
# link.clear()

link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Input and Scanners"))
    )

    element.click()

    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Conditions and Booleans"))
    )
    button.click()

    driver.back()
    driver.back()
    driver.back()
    driver.forward()
    driver.forward()

except:
    driver.quit()

