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

################ДОБАВЛЕНИЕ КОММЕНТАРИЯ

# driver.execute_script("window.scrollBy(0, 600);")
# driver.find_element_by_id('text-22-sub_row_1-0-2-0-0').click()
# driver.find_element_by_class_name('reviews_tab').click()
# driver.find_element_by_class_name('star-5').click()
# comment = driver.find_element_by_id('comment')
# comment.send_keys('Nice book!')
# name = driver.find_element_by_id('author')
# name.send_keys('Artur Pirozhkov')
# email = driver.find_element_by_id('email')
# email.send_keys('avtesttec@gmail.com')
# driver.find_element_by_class_name('form-submit').click()





time.sleep(7)
driver.quit()
