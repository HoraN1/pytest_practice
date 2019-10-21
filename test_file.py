# -*- coding: utf-8 -*-

"""
Author: zhanxin
Email: horacesunhe@gmail.com
date: 2019/10/21 12:19
"""


class TestClass:
    @classmethod
    def setup_class(cls):
        print("\nSetup TestClass!")

    @classmethod
    def teardown_class(cls):
        print("\nTeardown TestClass!")

    def setup_method(self, method):
        if method == self.test1:
            print("\nSetting up test1!")
        elif method == self.test2:
            print("\nSetting up test2!")
        else:
            print("\nSetting up unknown test!")

    def teardown_method(self, method):
        if method == self.test1:
            print("Tearing down test1!")
        elif method == self.test2:
            print("Tearing down test2!")
        else:
            print("\nTearing down unknown test!")

    def test1(self):
        print("Executing test1!")
        assert True

    def test2(self):
        print("Executing test2!")
        assert True
