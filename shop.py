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

##########ОТОБРАЖЕНИЕ СТРАНИЦЫ ТОВАРА

# driver.find_element_by_id('menu-item-50').click()
# email = driver.find_element_by_id('username')
# email.send_keys('avtesttec@gmail.com')
# passwrd = driver.find_element_by_id('password')
# passwrd.send_keys('Avt.6242833')
# driver.find_element_by_css_selector('[name="login"]').click()
# driver.find_element_by_id('menu-item-40').click()
# driver.find_element_by_class_name('post-181').click()
# title = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, 'product_title.entry-title'), "HTML5 Forms"))

##########КОЛИЧЕСТВО ТОВАРОВ В КАТЕГОРИИ

# driver.find_element_by_id('menu-item-50').click()
# email = driver.find_element_by_id('username')
# email.send_keys('avtesttec@gmail.com')
# passwrd = driver.find_element_by_id('password')
# passwrd.send_keys('Avt.6242833')
# driver.find_element_by_css_selector('[name="login"]').click()
# driver.find_element_by_id('menu-item-40').click()
# driver.find_element_by_link_text('HTML').click()
# time.sleep(7)
# items = driver.find_elements_by_class_name('product.type-product.product_cat-html')
# if len(items) == 3:
#     print('OK, 3 products in page')
# else:
#     print('ERROR')

##########СОРТИРОВКА ТОВАРОВ

# driver.find_element_by_id('menu-item-50').click()
# email = driver.find_element_by_id('username')
# email.send_keys('avtesttec@gmail.com')
# passwrd = driver.find_element_by_id('password')
# passwrd.send_keys('Avt.6242833')
# driver.find_element_by_css_selector('[name="login"]').click()
# driver.find_element_by_id('menu-item-40').click()
# sort = driver.find_element_by_class_name('orderby')
# sortcheck = sort.get_attribute('value')
# if sortcheck == "menu_order":
#     print('Default')
# else:
#     print('NOT Default')
# sortslct = Select(sort)
# sortslct.select_by_value('price-desc')
# sort = driver.find_element_by_class_name('orderby')
# sortcheck = sort.get_attribute('value')
# if sortcheck == "price-desc":
#     print('price hight - low')
# else:
#     print('NOT price hight - low')

##########ОТОБРАЖЕНИЕ, СКИДКА ТОВАРА

# driver.find_element_by_id('menu-item-50').click()
# email = driver.find_element_by_id('username')
# email.send_keys('avtesttec@gmail.com')
# passwrd = driver.find_element_by_id('password')
# passwrd.send_keys('Avt.6242833')
# driver.find_element_by_css_selector('[name="login"]').click()
# driver.find_element_by_id('menu-item-40').click()
# driver.find_element_by_class_name('post-169').click()
# oldprice = driver.find_element_by_css_selector('del > span')
# oldprice_get_text = oldprice.text
# assert "600" in oldprice_get_text
# newprice = driver.find_element_by_css_selector('ins > span')
# newprice_get_text = newprice.text
# assert "450" in newprice_get_text
# driver.find_element_by_css_selector('div.images > a > img').click()
# driver.find_element_by_class_name('pp_close').click()

##########ПРОВЕРКА ЦЕНЫ В КОРЗИНЕ

# driver.find_element_by_id('menu-item-40').click()
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_css_selector('[data-product_id="182"]').click()
# time.sleep(2)
# items = driver.find_element_by_class_name('cartcontents')
# itemscheck = items.text
# assert itemscheck == "1 Item"
# cartprice = driver.find_element_by_xpath('//li[@id="wpmenucartli"]/a/span[2]')
# cartpricecheck = cartprice.text
# assert '180' in cartpricecheck
# items.click()
# subtotal = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, 'cart-subtotal'), '180'))
# total = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, 'order-total'), '183'))

##########РАБОТА В КОРЗИНЕ

# driver.find_element_by_id('menu-item-40').click()
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_css_selector('[data-product_id="182"]').click()
# time.sleep(2)
# driver.execute_script("window.scrollBy(0, 200);")
# driver.find_element_by_css_selector('[data-product_id="180"]').click()
# time.sleep(2)
# driver.find_element_by_class_name('wpmenucart-contents').click()
# time.sleep(2)
# driver.find_element_by_css_selector('.remove[data-product_id="182"]').click()
# time.sleep(2)
# driver.find_element_by_link_text('Undo?').click()
# quantity = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
# quantity.clear()
# quantity.send_keys('3')
# driver.find_element_by_css_selector('[name="update_cart"]').click()
# qua = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
# quacheck = qua.get_attribute("value")
# assert quacheck == '3'
# time.sleep(2)
# driver.find_element_by_css_selector('[name="apply_coupon"]').click()
# mess = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-error'), "Please enter a coupon code."))

##########ПОКУПКА ТОВАРА

# driver.find_element_by_id('menu-item-40').click()
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_css_selector('[data-product_id="182"]').click()
# time.sleep(2)
# driver.find_element_by_class_name('wpmenucart-contents').click()
# checkout = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, 'checkout-button'))).click()
# FN = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, 'billing_first_name')))
# FN.send_keys("Artur")
# LN = driver.find_element_by_id('billing_last_name')
# LN.send_keys('Pirozhkov')
# email = driver.find_element_by_id('billing_email')
# email.send_keys('avtesttec@gmail.com')
# phone = driver.find_element_by_css_selector('[name="billing_phone"]')
# phone.send_keys('+77777777777')
# driver.find_element_by_class_name('select2-container.country_to_state.country_select').click()
# country = driver.find_element_by_id('s2id_autogen1_search')
# country.send_keys('Russia')
# driver.find_element_by_class_name('select2-result-label').click()
# adress = driver.find_element_by_css_selector('[name="billing_address_1"]')
# adress.send_keys('Nevskiy prospect')
# city = driver.find_element_by_css_selector('[name="billing_city"]')
# city.send_keys("St.Petersburg")
# state = driver.find_element_by_css_selector('[name="billing_state"]')
# state.send_keys("St.Petersburg")
# postcode = driver.find_element_by_css_selector('[name="billing_postcode"]')
# postcode.send_keys('777777')
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(2)
# driver.find_element_by_id('payment_method_cheque').click()
# driver.find_element_by_id('place_order').click()
# message = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-thankyou-order-received'), "Thank you. Your order has been received."))
# PayMet = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, 'method'), "Check Payments"))















time.sleep(5)
driver.quit()