import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver # импортируем webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://practice.automationtesting.in/')
driver.implicitly_wait(7)

###################РЕГИСТРАЦИЯ АККАУНТА

# driver.find_element_by_id('menu-item-50').click()
# email = driver.find_element_by_id('reg_email')
# email.send_keys('avtesttec@gmail.com')
# passwrd = driver.find_element_by_id('reg_password')
# passwrd.send_keys('Avt.6242833')
# driver.find_element_by_css_selector('[name="register"]').click()

#####################ЛОГИН В СИСТЕМУ

# driver.find_element_by_id('menu-item-50').click()
# email = driver.find_element_by_id('username')
# email.send_keys('avtesttec@gmail.com')
# passwrd = driver.find_element_by_id('password')
# passwrd.send_keys('Avt.6242833')
# driver.find_element_by_css_selector('[name="login"]').click()
# logout = driver.find_element_by_link_text('Logout')
# if logout is not None:
#     print('Элемент присутствует')
# else:
#     print('ОШИБКА: Элемент отсутствует')


time.sleep(7)
driver.quit()