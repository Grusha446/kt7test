import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import allure
import logging
from mainObject import MainObject
from cartObject import CartObject
from productObject import ProductObject
from registrationObject import RegistrationObject

#################################1##################################
@allure.feature("First test")
@allure.title("screenshot")
def test_screenshot(driver,logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    driver.implicitly_wait(1)
    product_page = ProductObject(driver, logger)
    driver.implicitly_wait(1)
    product_page.open_product()
    driver.implicitly_wait(1)
    product_page.image_click()
    driver.implicitly_wait(1)
    product_page.next_image()
    driver.implicitly_wait(1)
    product_page.next_image()
    driver.implicitly_wait(1)

#################################2##################################
@allure.feature("Second test")
@allure.title("cart")
def test_cart(driver,logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    driver.implicitly_wait(2)
    cart_page = CartObject(driver, logger)
    driver.implicitly_wait(1)
    cart_page.add_cart_button()
    driver.implicitly_wait(1)
    buy_message = driver.find_element(By.CSS_SELECTOR, "body:nth-child(2) div.container:nth-child(4) > div.alert.alert-success.alert-dismissible")
    if "iPhone добавлен в корзину покупок!" in buy_message.text:
        print("Товар добавлен в корзину")
    driver.implicitly_wait(1)

#################################3##################################
@allure.feature("Third test")
@allure.title("category")
def test_category(driver,logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    driver.implicitly_wait(1)
    main_page.open_pc_category()
    driver.implicitly_wait(2)
    nothing_message = driver.find_element(By.CSS_SELECTOR, "body:nth-child(2) div.container:nth-child(4) div.row div.col-sm-9 > p:nth-child(2)")
    if "В данной категории нет товаров." in nothing_message.text:
        print("Проверка на категорию пройдена пройдена!")

#################################4##################################
@allure.feature("Fourth test")
@allure.title("registration")
def test_registration(driver,logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    driver.implicitly_wait(2)
    register_page = RegistrationObject(driver, logger)
    driver.implicitly_wait(1)
    register_page.open_registration_page()
    driver.implicitly_wait(1)
    register_page.registration_user("aaaaaa", "aaaaaa", "aaaaaa@gmail.com", "5214125", "aaAAaa@")
    driver.implicitly_wait(1)

#################################5##################################
@allure.feature("Fifth test")
@allure.title("input")
def test_main_input(driver,logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    driver.implicitly_wait(2)
    main_page.search("Iphone")
    driver.implicitly_wait(1)

#################################6##################################
@allure.feature("Sixth test")
@allure.title("wishlist")
def test_add_to_wishlist(driver,logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    driver.implicitly_wait(1)
    product_page = ProductObject(driver, logger)
    driver.implicitly_wait(1)
    product_page.add_to_wishlist(2)
    driver.implicitly_wait(1)

#################################7##################################
@allure.feature("Seventh test")
@allure.title("camera")
def test_add_camera(driver,logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    product_page = ProductObject(driver, logger)
    driver.implicitly_wait(1)
    product_page.add_cart_button(4)
    driver.implicitly_wait(1)
    product_page.camera()
    driver.implicitly_wait(1)

#################################8##################################
@allure.feature("Eigth test")
@allure.title("clipboard")
def test_add_clipboard(driver,logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    driver.implicitly_wait(1)
    main_page.open_category("Планшеты")
    driver.implicitly_wait(1)
    product_page = ProductObject(driver, logger)
    driver.implicitly_wait(1)
    product_page.add_to_cart_clipboard()
    driver.implicitly_wait(1)

#################################9##################################
@allure.feature("Ninth test")
@allure.title("htc")
def test_add_htc(driver,logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    driver.implicitly_wait(1)
    main_page.open_category("Телефоны")
    driver.implicitly_wait(1)
    product_page = ProductObject(driver, logger)
    driver.implicitly_wait(1)
    product_page.add_to_cart_htc()
    driver.implicitly_wait(2)

#################################10##################################
@allure.feature("Tenth test")
@allure.title("review")
def test_submit_review(driver,logger):
    main_page = MainObject(driver, logger)
    driver.implicitly_wait(2)
    main_page.go()
    driver.implicitly_wait(2)
    search_item = driver.find_element(By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child(2) div.product-thumb.transition div.image a:nth-child(1) > img.img-responsive")
    search_item.click()
    product_page = ProductObject(driver, logger)
    driver.implicitly_wait(1.5)
    product_page.open_review_form()
    driver.implicitly_wait(1.5)
    product_page.submit_review("aaaaaaa", "ааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааа")
    driver.implicitly_wait(1.5)