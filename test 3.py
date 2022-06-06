from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
driver= webdriver.Chrome()
driver.get('https://abl.celloscope.net/onboarding-registration/')
driver.maximize_window()
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
username.send_keys("moon.verifier")
password.send_keys("asdf1234")
driver.find_element_by_id("login-btn").click()
wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Customer_Registration")))  
driver.find_element_by_id("Customer_Registration").click()
time.sleep(100)