from selenium import webdriver
import time

url = "https://rozetka.com.ua/"
driver = webdriver.Chrome(executable_path="C:\\Users\\nazar\\OneDrive\\Документи\\Python\\DriverChrom\\chromedriver.exe")

try:
  driver.get(url=url)
  time.sleep(5)
except Exception as ex:
  print(ex)
finally:
  driver.close
  driver.quit
