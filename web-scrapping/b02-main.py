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

driver.get("https://www.techwithtim.net/?s=java")
driver.implicitly_wait(3)  # time.sleep(30) is inefficient, bc not always we want to wail 30 secs.

# my_element = driver.find_element(By.ID,"edit-search-block-form--2")
# my_element.send_keys("Selenium")
# my_element.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "main")))
    # print(main.text)

    articles = driver.find_elements(By.TAG_NAME, 'article')
    for article in articles:
        header = article.find_element(By.CLASS_NAME, 'entry-header')
        print(header.text)
finally:
    driver.quit()

# main = driver.find_element(By.ID, "main")



