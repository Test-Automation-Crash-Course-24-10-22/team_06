from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--incognito")

# Add the webdriver to the PATH and you don't need to clarify the way(path) to the file.
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

driver.get("https://rozetka.com.ua/ua/")
time.sleep(10)

driver.quit()