from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import random

# Generate a random integer between 1 and 1000
num = random.randint(1, 1000)

driver = webdriver.Chrome()
driver.get('https://scorecount.com/click-counter/')
driver.maximize_window()

clicking = driver.find_element(By.XPATH,'//*[@id="counter1"]/div[3]')
for _ in range(num):
    clicking.click()
    sleep(1)

driver.get('https://clickcounter.io/keyboard-counter')
driver.maximize_window()

typing = driver.find_element(By.XPATH,'/html/body')

alphabets = 'abcdefghijklmnopqrstuvwxyz'
keywords = ''.join([alphabets[i % len(alphabets)] for i in range(num)])
typing.send_keys(keywords)

# Close the browser after 5 seconds
sleep(5)
