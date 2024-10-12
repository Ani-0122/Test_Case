import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.google.com/")
time.sleep(5)
search_field=driver.find_element(By.NAME,"q")
search_field.send_keys("Nike")
enter_button=driver.find_element(By.NAME,"q")
enter_button.send_keys(Keys.ENTER)
time.sleep(5)
first_text=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[12]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3")
first_text.click()
time.sleep(5)
