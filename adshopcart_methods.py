import sys
import datetime
import adshopcart_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
s = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=s)
# s = Service(executable_path='./chromedriver')
#
#
# driver = webdriver.Chrome(service=s)


# Fixture method - to open web browser
def setup():


    print(f'Test started at: {datetime.datetime.now()}')
    # Make a full screen
    driver.maximize_window()

    # Let's wait for the browser response in general
    driver.implicitly_wait(30)

    # Navigating to the Advantage shopping cart app website
    driver.get(locators.advantage_url)

    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.advantage_url and driver.title == (u'\xa0' + "Advantage Shopping"):
        print(f'We\'re at Advantage shopping cart homepage -- {driver.current_url}')
        print(f'We\'re seeing title message -- "&nbsp;Advantage Shopping"')
    else:
        print(f'We\'re not at the Advantage shopping cart homepage. Check your code!')
        driver.close()
        driver.quit()




def tearDown():


    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()



setup()
tearDown()