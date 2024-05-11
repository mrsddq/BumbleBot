
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
# driver.get('https://gew3.bumble.com/get-started')
driver.get('https://bumble.com/get-started')
driver.maximize_window()
sleep(2)

Use_cell_phone_number=driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[3]/button')
# sign in using facebook
# continue_with_fb_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]')
# continue_with_fb_button.click()
sleep(5)

# bumble_window = driver.window_handles[0]
# popup_window = driver.window_handles[1]


# switch back to facebook popup window
# driver.switch_to.window(popup_window)

number_field = driver.find_element(By.XPATH,'//*[@id="phone"]')
number_field.send_keys('9540880891')


# email_field = driver.find_element(By.XPATH,'//*[@id="email"]')
# email_field.send_keys('siddiquilaraib8@gmail.com')

# password_field = driver.find_element(By.XPATH,'//*[@id="pass"]')
# password_field.send_keys('Ariba@2203')

# login_button = driver.find_element(By.NAME,"login")
# login_button.click()
# sleep(2)

# switch back to bumble window
# driver.switch_to.window(bumble_window)
# sleep(5)

def swipe_right(wait=5):
    like_button = driver.find_element(
        By.XPATH,'//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span'
    )
    like_button.click()
    sleep(wait)

# def swipe_left(wait=5):
#     dislike_button = driver.find_element(
#         By.XPATH,'//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span'
#     )
#     dislike_button.click()
#     sleep(wait)

# def close_popup(wait=5):
#     continue_with_bumble_button = driver.find_element(
#         By.XPATH,'//*[@id="main"]/div/div[1]/main/div[2]/article/div/footer/div[2]/div[2]/div/span/span/span/span'
#     )
#     continue_with_bumble_button.click()
#     sleep(wait)

# def open_chat(wait=5):
#     open_chat_button = driver.find_element(
#         By.XPATH,'//*[@id="main"]/div/div[1]/main/div[2]/article/div/footer/div[2]/div[1]/div'
#     )
#     open_chat_button.click()
#     sleep(wait)


single = True
while single:
    # try:
        swipe_right()
    # except Exception:
    #     open_chat()
    #     single = False

driver.close()