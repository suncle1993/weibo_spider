#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 4/8/18 10:41 AM
@author: Chen Liang
@function: selenium模拟登录
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
import time
import re


# def singleton(cls):
#     instances = {}
#
#     def wrap(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#
#     return wrap
#
#
# @singleton
class WeiboSeleniumLogin(object):

    def __init__(self, driver_path):
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        self.__driver = webdriver.Chrome(driver_path, chrome_options=chrome_options)
        self.__driver.maximize_window()
        self.__driver.set_page_load_timeout(30)
        self.__driver.set_window_size(1124, 850)
        self.__cookies = None
        self._source = None

    def login(self, username, password, login_url):
        self.__driver.get(login_url)
        name_field = self.__driver.find_element_by_id('loginname')
        name_field.clear()
        name_field.send_keys(username)
        password_field = self.__driver.find_element_by_class_name('password').find_element_by_name('password')
        password_field.clear()
        password_field.send_keys(password)
        submit = self.__driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a/span')
        ActionChains(self.__driver).double_click(submit).perform()
        time.sleep(5)
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'WB_miniblog')))

        self._source = self.__driver.page_source
        # print(self._source)
        if self.is_login():
            # print('login success')
            self.__cookies = self.__driver.get_cookies()
            self.__driver.quit()
            return True
        self.__driver.quit()
        return False

    def is_login(self):
        rs = re.search("CONFIG\['islogin'\]='(\d)'", self._source)
        if rs:
            return int(rs.group(1)) == 1
        else:
            return False

    @property
    def cookies(self):
        return self.__cookies

    @property
    def user_id(self):
        rs = re.search("CONFIG\['uid'\]='(\d+)'", self._source)
        if rs:
            return int(rs.group(1))
        else:
            return -1


if __name__ == '__main__':
    chrome_driver_path1 = '/root/qk_python/python/data/collect/weibo_spider/priv/chromedriver'
    username1 = input('请输入你的账号\n')
    password1 = input('请输入你的密码\n')
    login_url1 = 'https://weibo.com/login.php'
    sl = WeiboSeleniumLogin(chrome_driver_path1)
    if sl.login(username1, password1, login_url1):
        print('login success')
        print(sl.cookies)
        print(sl.user_id)
    else:
        print('login failed')
