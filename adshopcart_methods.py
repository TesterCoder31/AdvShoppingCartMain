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

    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.advantage_url and driver.title == (u'\xa0' + "Advantage Shopping"):
        print(f'We\'re at Advantage shopping cart homepage -- {driver.current_url}')
        print(f'We\'re seeing title message -- "Advantage Shopping"')
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


# Create new user account at advantage shopping cart and validate my account
def create_new_user():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(4)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(2)
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.advantage_first_name)
    sleep(0.25)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.advantage_email)
    sleep(0.25)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.advantage_password)
    sleep(0.25)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.advantage_password)
    sleep(0.25)
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.advantage_first_name)
    sleep(0.25)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.advantage_last_name)
    sleep(0.25)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.advantage_phone_number)
    sleep(0.25)
    Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text('Canada')
    sleep(0.25)
    driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.advantage_city)
    sleep(0.25)
    driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.advantage_address)
    sleep(0.25)
    driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.advantage_state)
    sleep(0.25)
    driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.advantage_postal_code)
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="formCover"]/sec-view/div/input').click()
    sleep(0.25)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(0.25)
    print(f"New user is created successfully with username: {locators.advantage_full_name}")
    sleep(0.25)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(4)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
    sleep(0.25)
    content = driver.find_element(By.XPATH, '//*[@id="myAccountContainer"]/div[1]/div/div[1]/label')
    print(f"User name validate with {content.text}")
    driver.find_element(By.ID, 'menuUser').click()
    sleep(4)
    driver.find_element(By.XPATH, '//div[@id="loginMiniTitle"]/label[2]').click()
    sleep(2)
    content = driver.find_element(By.XPATH, '/html/body/div[3]/section/article/div[3]/div/div/label')
    print(f"In my order {content.text} is displayed")


# Log out user from the advantage shopping website page


def log_out():


    if driver.current_url == 'https://advantageonlineshopping.com/#/MyOrders':
        driver.find_element(By.ID, 'menuUser').click()
        sleep(4)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
        sleep(4)
        print(f"User successfully log out at : {datetime.datetime.now()}")
        sleep(2)


# Log in with new user's credentials
def login_with_new_user():

    driver.find_element(By.ID, 'menuUser').click()
    sleep(4)
    driver.find_element(By.NAME, 'username').send_keys(locators.advantage_username)
    sleep(2)
    driver.find_element(By.NAME, 'password').send_keys(locators.advantage_password)
    sleep(2)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(2)
    print(f"Log in with new user name {locators.advantage_full_name} successfully")
    sleep(3)


# Delete user from website and also checking by credential log in
def del_user():
    #if driver.current_url == locators.advantage_url:
    driver.find_element(By.ID, 'menuUser').click()
    sleep(4)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
    sleep(3)

    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    #driver.find_element(By.XPATH, '//div[@id="myAccountContainer"]/div[6]/button/div').click()
    sleep(3)
    driver.find_element(By.XPATH, '//div[text()="yes"]').click()
    #driver.find_element(By.XPATH, '//div[@id="deleteAccountPopup"]/div[3]/div').click()
    sleep(5)
    print("User successfully deleted")
    sleep(3)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(4)
    driver.find_element(By.NAME, 'username').send_keys(locators.advantage_username)
    sleep(2)
    driver.find_element(By.NAME, 'password').send_keys(locators.advantage_password)
    sleep(2)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(2)
    contain = driver.find_element(By.XPATH, '//*[@id="signInResultMessage"]')
    print(f'{contain.text} text is displayed')
    print("-------Test scenario:Check user created and deleted------is passed")


# Check user's account empty or not
# def check_my_account():
#     if driver.current_url == locators.advantage_url:
#         driver.find_element(By.ID, 'menuUser').click()
#         sleep(4)
#         driver.find_element(By.XPATH, '//div[@id="loginMiniTitle"]/label[2]').click()
#         sleep(2)
#         print('Your cart is empty')
#         detail = driver.find_element(By.XPATH, '/html/body/div[3]/section/article/div[3]/div/div/label')
#         print(detail.text)


# Try to log in with already deleted credentials
def check_login_del_acc():
    if driver.current_url == locators.advantage_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(4)
        driver.find_element(By.NAME, 'username').send_keys(locators.advantage_username)
        sleep(2)
        driver.find_element(By.NAME, 'password').send_keys(locators.advantage_password)
        sleep(2)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(2)
        print(f"Log in with user name {locators.advantage_username} successfully")
    else:
        contain = driver.find_element(By.XPATH, '//*[@id="signInResultMessage"]')
        print(contain.text)
        print("Incorrect user name or password.")


def new():
    #if driver.current_url == locators.advantage_url:
    driver.find_element(By.ID, 'menuUser').click()
    sleep(4)
    driver.find_element(By.NAME, 'username').send_keys(locators.advantage_username)
    sleep(2)
    driver.find_element(By.NAME, 'password').send_keys(locators.advantage_password)
    sleep(2)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(2)
    contain = driver.find_element(By.XPATH, '//*[@id="signInResultMessage"]')
    print(contain.text)
    print("Incorrect user name or password.")


def check_text_displayed():

    content = driver.find_element(By.ID, 'speakersTxt')
    print(f"On advantage shopping website {content.text} text is displayed")
    content = driver.find_element(By.ID, 'tabletsTxt')
    print(f"On advantage shopping website {content.text} text is displayed")
    content = driver.find_element(By.ID, 'laptopsTxt')
    print(f"On advantage shopping website {content.text} text is displayed")
    content = driver.find_element(By.ID, 'miceTxt')
    print(f"On advantage shopping website {content.text} text is displayed")
    content = driver.find_element(By.ID, 'headphonesTxt')
    print(f"On advantage shopping website {content.text} text is displayed")
    content1 = driver.find_element(By.XPATH, '/html/body/header/nav/div/a/span[1]')
    #print(f"On advantage shopping website {content.text} text is displayed")
    content2 = driver.find_element(By.XPATH, '/html/body/header/nav/div/a/span[2]')
    print(f"On advantage shopping website {content2.text} {content1.text} text is displayed")
    # content = driver.find_element(By.XPATH, '//*[@id="Layer_1"]/path')
    # print(f"On advantage shopping website {content.text} text is displayed")
    driver.find_element(By.LINK_TEXT, 'OUR PRODUCTS').click()
    driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()
    driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
    print("All links are clickable for Advantage shopping website")
    sleep(2)
    # Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Laptops')
    # sleep(2)
    # Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_visible_text('HP Chromebook 14 G1(ENERGY STAR)')
    driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.advantage_email)
    sleep(1)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys('Hi')
    sleep(1)
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(1)
    content = driver.find_element(By.XPATH, '//*[@id="registerSuccessCover"]/div/a')
    print(f"{content.text} is displayed")
    driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').click()





setup()
# create_new_user()
# #log_out()
# #login_with_new_user()
# del_user()
# tearDown()
check_text_displayed()