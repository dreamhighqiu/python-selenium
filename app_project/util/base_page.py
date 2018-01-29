#-*-coding:utf-8-*-
from appium import webdriver
import time
from pageobject.driver import Open_Driver
class public_method(object):
    def __init__(self):
        open_driver = Open_Driver()
        self.driver = open_driver.launchapp()
    def wait_activity(self):
        ca = self.driver.current_activity
        self.driver.wait_activity(ca,30)

    def swipeUp(self, t=500, n=1):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()

        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeDown(self, t=500, n=1):
        '''向下滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipLeft(self, t=500, n=1):
        '''向左滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.05
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipRight(self, t=500, n=1):
        '''向右滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.05
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)
    def tap(self,postion,t):
        #driver.tap([(615, 52), (690, 146)], 500)
        self.driver.tap(self.position,self.t)
    def contexts(self):
        cc = self.driver.current_context
        cs = self.driver.contexts
        for i in cs:
            i!=cc
            self.driver.switch_to.context(i)

    # 截图
    def getScreenShot(self):

        time = self.getTime()
        filename = '../jpg/ %s.png' % time
        self.driver.get_screenshot_as_file(filename)

    # 获取时间戳
    def getTime(self):
        tamp = int(time.time())
        return tamp

    # 隐式等待
    def implicit_for_wait(self,t):
        self.driver.implicitly_wait(t)

    # 显示等待
    def wait(self,t):

        self.driver.WebDriverWait(self.driver, 10, 5).until(lambda driver: driver.find_element_by_id("ssss"))














