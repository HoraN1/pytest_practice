# -*- coding: utf-8 -*-

"""
Author: zhanxin
Email: horacesunhe@gmail.com
date: 2019/10/21 16:23
"""
import pytest


@pytest.fixture(autouse=True)
def setup():
    print("\nSetup")


def test1():
    print("\nExecuting test1!")
    assert True


# @pytest.mark.usefixtures("setup")
def test2():
    print("\nExecuting test2!")
    assert True
