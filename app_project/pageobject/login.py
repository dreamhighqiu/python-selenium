#-*-coding:utf-8-*-
from appium import webdriver
from util.base_page import public_method
from driver import Open_Driver

import unittest
class Login(object):
    def __init__(self):
        open_driver = Open_Driver()
        self.driver = open_driver.launchapp()
        self.pub_met = public_method()





    def login(self,username,password):
        self.driver.find_element_by_id("com.yaochufa.app:id/btn_my_login").click()
        self.driver.find_element_by_id("com.yaochufa.app:id/et_phone").clear()
        self.driver.find_element_by_id("com.yaochufa.app:id/et_phone").send_keys(username)
        self.driver.find_element_by_id("com.yaochufa.app:id/et_pwd").send_keys(password)
        self.driver.find_element_by_id("com.yaochufa.app:id/btn_login").click()

    def logout(self):
        self.driver.find_element_by_id("com.yaochufa.app:id/iv_my_setting").click()
        self.driver.find_element_by_name("退出登录").click()
        self.driver.find_element_by_id("com.yaochufa.app:id/btn_bottom_sure").click()

    def click_product(self):
        #进入首页
        self.driver.find_element_by_id("com.yaochufa.app:id/item_index").click()

        self.pub_met.swipeUp(100,3)
        self.driver.find_element_by_name(u"5201乐纯提供移动端标题!!!!-移动端长标题移动端长标题移动端长标题移动端长标题移动端长标!").click()


    def product_detail(self):

        self.pub_met.swipeUp(100,2)

    def test_click(self):
        login = Login()
        login.click_product()
        login.product_detail()





















