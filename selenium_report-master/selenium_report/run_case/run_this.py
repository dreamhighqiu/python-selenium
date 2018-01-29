# coding:utf-8
import os
# python2.7要是报编码问题，就加这三行，python3不用加
import sys
import time
import unittest

import HTMLTestRunner_jpg

reload(sys)
sys.setdefaultencoding('utf8')

cur_path = os.path.dirname(os.getcwd())
# 测试用例的路径
case_path = os.path.join(cur_path, "case")
#print case_path
# 设置报告文件存路径
report_path = os.path.join(cur_path, "test_report/")
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# 设置报告名称格式
HtmlFile = report_path + now + "HtmlReport.html"
fp = file(HtmlFile, "wb")

if __name__ == "__main__":

    discover = unittest.defaultTestLoader.discover(case_path,"test*.py")
    print(discover)
    """run = HTMLTestRunner_jpg.HTMLTestRunner(title="可以装逼的测试报告",
                                                            description="测试用例参考",
                                                            stream=open(report_path+"\\result.html", "wb"),
                                                            retry=1)"""
    #run = selenium_report.HTMLTestRunner_jpg.HTMLTestRunner(title="可以装逼的测试报告",description = "测试用例参考",stream =fp,retry = 1)
    run = HTMLTestRunner_jpg.HTMLTestRunner(title="可以装逼的测试报告", description="测试用例参考", stream=fp)
    #run = HTMLTestRunner.HTMLTestRunner(title="可以装逼的测试报告", description="测试用例参考", stream=fp)

    run.run(discover)



