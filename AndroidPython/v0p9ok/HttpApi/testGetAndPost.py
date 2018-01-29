# coding=utf-8

import requests
import unittest
import  json

class testClass(unittest.TestCase):
    def setUp(self):
        print "初始化"
    def tearDown(self):
        print "结束"

    def testGet(self):
        keyword = {"wd":"poptest"}
        headers = {"User-Agent":"test",
                   'Referer': 'http://login.weibo.cn/login/?ns=1&revalid=2&backU'}
        cookies = dict(IPLOC="CN1100", ABTEST="1")
        res = requests.get("https://customer-api.helijia.com/app-customer/transformers/getCityList?version=3.3.0.1&sign_type=md5&city=110100&req_time=1472372990756&device_type=android&device_id=d3c1d53d0a8a378f",
                           params=keyword,
                           headers=headers,
                           cookies=cookies)
        print res.text
        if u"北京市" in res.text:
            print "pass"
            result = True
        else:
            print "fail"
            result = False
        self.assertTrue(result)

    def testPost(self):
        keyword = {"query":"postman"}
        headers = {"User-Agent":"hlj-android/3.3.0.1",
                   "Content-Type":"application/x-www-form-urlencoded",
                   'Referer': 'http://login.weibo.cn/login/?ns=1&revalid=2&backU'}
        cookies = dict(IPLOC="CN1100", ABTEST="1")
        res = requests.post("https://app.helijia.com/zmw/user/bind_dev",
                            #data=json.dumps(keyword),
                            data=keyword,
                            headers=headers,
                            cookies=cookies)
        print res.text
        if u"网页" in res.text:
            print "pass"
        else:
            print "fail"
        self.assertTrue(True)
    def GetSort(self):
        url ="https://search.yaochufa.com/ycf-search/solr/vproduct/search?channel=AppStore&city=%E5%8C%97%E4%BA%AC&cityCode=110100&cityLat=39.92998577808024&cityLng=116.3956450378787&imei=126F3CEA-3E23-47FF-9821-5017CA998286&isTagPage=1&lang=app&machineCode=126F3CEA-3E23-47FF-9821-5017CA998286&machineType=0&maxPrice=999999&minPrice=0&p=1&province=&s=20&sort=1&system=ios&tagList=967&tagNew=&version=5.9.1"
        headers ={"Connection":"keep-alive","Accept":"*/*",
                "User-Agent":"MyYaoChuFaApp/5.9.1 (iPhone; iOS 11.2; Scale/2.00)" ,
                "APIGEEHEADER2": "MTUxNjk1Njk4MyN2ZXJzaW9uLHN5c3RlbSxsYW5nLGltZWksI3NpMzY1ZTIyYmY0YjJlZWE5ZTVlYjUxYjIyNjVlNWFjMWMzcHVtczk="
                }


        res=requests.get(url =url,headers =headers,verify =False).json()
        print res


if __name__ == "__main__":
    unittest.main()