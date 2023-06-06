from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Create a service object
serv_obj = Service(ChromeDriverManager().install())

# Configure the webdriver to use the service
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

# Rest of your code...
driver.get('https://byjus.com/ncert-solutions-class-11-english/hornbill-silk-road/')
driver.find_element(By.XPATH, '//*[@type="button"]').click()

driver.find_element(By.XPATH, '//*[@type="submit"]').click()

driver.find_element(By.NAME, 's').send_keys('Class10' + Keys.RETURN)
