import json
import unittest
from common.configHttp import RunMain
import common.common
import paramunittest
import geturlParams
import urllib.parse

urlparams = geturlParams.geturlParams()
url = urlparams.get_Url()
login_xls = common.common.get_xls('userCase.xlsx', 'login')

@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        print(self.case_name+"测试开始前准备")

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):
        """
        check test result
        :return:
        """
        data = self.query
        url1 = "http://www.xxx.com/login?"
        new_url = url1 + data
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
        info = RunMain().run_main(self.method, urlparams.get_Url(), data1)
        ss = json.loads(info)
        if self.case_name == 'login':
            self.assertEqual(ss['code'], 200)
        if self.case_name == 'login_error':
            self.assertEqual(ss['code'], -1)
        if self.case_name == 'login_null':
            self.assertEqual(ss['code'], 10001)


