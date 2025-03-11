from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ChromeDriveri asukoha määramine
service = Service('/usr/local/bin/chromedriver/chromedriver')

# Seadistage ChromeDriver
driver = webdriver.Chrome(service=service)

# Avage Google'i avaleht
driver.get("https://www.google.com")

# Leidke otsingukast
search_box = driver.find_element(By.NAME, "q")

# Sisestage otsingupäring
search_box.send_keys("Selenium testing")

# Esitage otsing
search_box.send_keys(Keys.RETURN)

# Oodake, kuni otsingutulemused laaditakse
time.sleep(5)

# Sulgege brauser
driver.quit()