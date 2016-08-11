# -*- coding: utf-8 -*-
'''
Created on 2016.4.15

@author: leo
'''

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox()
driver.get("http://test2.admin.haibian.com")
driver.find_element_by_id("uname").clear()
driver.find_element_by_id("uname").send_keys("mujiangliu@163.com")
driver.find_element_by_id("pwd").clear()
driver.find_element_by_id("pwd").send_keys("111111")
driver.find_element_by_name("login_sub").click()
def titleCheck(title):
    if title.decode("utf_8") == '海边管理中心':
        return True
    else:
        return False

print titleCheck(driver.title)
time.sleep(2)
driver.close()