from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
driver= webdriver.Chrome()
 
driver.get('https://abL.celloscope.net')
driver.maximize_window()
 
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
username.send_keys("01681866699")
password.send_keys("Asdf#123")
 
driver.find_element_by_id("login-btn").click()
wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "transferMenu")))  
driver.find_element_by_id("transferMenu").click()
time.sleep(1)
driver.find_element_by_link_text("at My Bank").click()
time.sleep(1)
driver.find_element_by_id("fromAccount").click()
time.sleep(1)
driver.find_element_by_css_selector("[aria-label='0200010000045']").click()
time.sleep(1)
driver.find_element_by_id("toAccount").click()
time.sleep(1)
driver.find_element_by_css_selector("[aria-label='0200010000046']").click() 
time.sleep(1)
amount= driver.find_element_by_id("transferAmount")
amount.click()
amount.send_keys("10")
time.sleep(1)
remarks= driver.find_element_by_id("remarks")
remarks.click()
remarks.send_keys("FT")
time.sleep(1)
driver.find_element_by_tag_name('button').click()
time.sleep(500)