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
    wd.get("https://vk.com/")
    wd.find_element_by_id("index_email").click()
    wd.find_element_by_id("index_email").clear()
    wd.find_element_by_id("index_email").send_keys("mamaev_alexey@list.ru")
    wd.find_element_by_id("index_pass").click()
    wd.find_element_by_id("index_pass").clear()
    wd.find_element_by_id("index_pass").send_keys("Kuperman")
    wd.find_element_by_id("index_login_button").click()
    wd.find_element_by_xpath("//li[@id='l_nwsf']//span[.='Новости']").click()
    wd.find_element_by_xpath("//li[@id='l_fr']//span[.='Друзья']").click()
    wd.find_element_by_xpath("//li[@id='l_fr']//span[.='Друзья']").click()
    wd.find_element_by_css_selector("span.left_label.inl_bl").click()
    wd.find_element_by_xpath("//li[@id='l_fr']//span[.='Друзья']").click()
    wd.find_element_by_xpath("//li[@id='l_aud']//span[.='Музыка']").click()
    wd.find_element_by_css_selector("span.left_label.inl_bl").click()
    wd.find_element_by_id("top_profile_link").click()
    wd.find_element_by_id("top_logout_link").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
