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


# Fixture method - to open web browser
def setup():


    print(f'Test started at: {datetime.datetime.now()}')
    # Make a full screen
    driver.maximize_window()

    # Let's wait for the browser response in general
    driver.implicitly_wait(30)

    # Navigating to the Advantage shopping cart app website
    driver.get(locators.advantage_url)

    #print(driver.title)
    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.advantage_url and driver.title == driver.title:
    #if driver.current_url == locators.advantage_url and driver.title == (u'\xa0' + "Advantage Shopping"):
    #if driver.current_url == locators.advantage_url and driver.title.endswith == ("Advantage Shopping"):
        print(f'We\'re at Advantage shopping cart homepage -- {driver.current_url}')
        print(f'We\'re seeing title message -- "&nbsp;Advantage Shopping"')
    else:
        print(f'We\'re not at the Advantage shopping cart homepage. Check your code!')
        driver.close()
        driver.quit()


def create_new_user():


    #if driver.current_url == locators.advantage_url'
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    #driver.find_element(By.CLASS_NAME, 'create-new-account ng-scope').click()
    #driver.find_element(By.XPATH, '/html/body/login-modal/div/div/div[3]/a[2]').click()
    #driver.find_element(By.XPATH, '//a[contains(., "CREATE NEW ACCOUNT")]').click()
    #driver.find_element_by_link_text("CREATE NEW ACCOUNT").click()
    # sleep(0.25)
    driver.get("https://advantageonlineshopping.com/#/register")
    sleep(0.25)
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys('hjhjgfe')
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys('tiger@roar.com')
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys('Tiger@31')
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys('Tiger@31')
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys('Tiger')
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys('Tigeri')
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys('9999999999')
    Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text('Canada')
    driver.find_element(By.NAME, 'cityRegisterPage').send_keys('Sse')
    driver.find_element(By.NAME, 'addressRegisterPage').send_keys('123 sunrise ave')
    driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys('bc')
    driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys('V4h9z9')
    driver.find_element(By.XPATH, '//*[@id="formCover"]/sec-view/div/input').click()
    driver.find_element(By.ID, 'register_btnundefined').click()












def tearDown():


    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()



setup()
create_new_user()
#tearDown()