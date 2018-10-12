# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("https://vk.com/login?act=mobile&hash=c164c2928c4c23e70dbf96d01962")
    wd.find_element_by_id("quick_email").click()
    wd.find_element_by_id("quick_email").send_keys("\\undefined")
    wd.find_element_by_id("quick_pass").click()
    wd.find_element_by_id("quick_pass").send_keys("\\undefined")
    wd.find_element_by_id("quick_login_button").click()
    wd.find_element_by_css_selector("span.left_label.inl_bl").click()
    wd.find_element_by_xpath("//li[@id='l_nwsf']//span[.='Новости']").click()
    wd.find_element_by_xpath("//li[@id='l_msg']//span[.='Сообщения']").click()
    wd.find_element_by_css_selector("span.left_label.inl_bl").click()
    wd.find_element_by_link_text("Настройки страницы Алексей").click()
    wd.find_element_by_id("top_logout_link").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
