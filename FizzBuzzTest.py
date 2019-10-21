# -*- coding: utf-8 -*-

"""
Author: zhanxin
Email: horacesunhe@gmail.com
date: 2019/10/21 11:26
"""
import pytest

def setup_function(function):
    if function == test_returnWith1PassedIn:
        print("\nSetting up test with 1 pass in!")
    elif function == test_returnWith2PassedIn:
        print("\nSetting up test with 2 pass in!")
    elif function == test_returnFizzWizzWith3PassedIn:
        print("\nSetting up test with 3 pass in!")
    elif function == test_returnFizzWizzWith5PassedIn:
        print("\nSetting up test with 5 pass in!")
    elif function == test_returnFizzWizzWith6PassedIn:
        print("\nSetting up test with 6 pass in!")
    elif function == test_returnFizzWizzWith10PassedIn:
        print("\nSetting up test with 10 pass in!")
    elif function == test_returnFizzWizzWith15PassedIn:
        print("\nSetting up test with 15 pass in!")
    else:
        print("Setting up unknown test!")


def teardown_function(function):
    if function == test_returnWith1PassedIn:
        print("\nTearing down test with 1 pass in!")
    elif function == test_returnWith2PassedIn:
        print("\nTearing down test with 2 pass in!")
    elif function == test_returnFizzWizzWith3PassedIn:
        print("\nTearing down test with 3 pass in!")
    elif function == test_returnFizzWizzWith5PassedIn:
        print("\nTearing down test with 5 pass in!")
    elif function == test_returnFizzWizzWith6PassedIn:
        print("\nTearing down test with 6 pass in!")
    elif function == test_returnFizzWizzWith10PassedIn:
        print("\nTearing down test with 10 pass in!")
    elif function == test_returnFizzWizzWith15PassedIn:
        print("\nTearing down test with 15 pass in!")
    else:
        print("Tearing down unknown test!")

def fizzBuzz(value):
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    if isMultiple(value, 5):
        return "Buzz"
    return str(value)


def checkFizzBuzz(value, expectedRetVal):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal


def isMultiple(value, mod):
    return (value % mod) == 0


def test_returnWith1PassedIn():
    checkFizzBuzz(1, "1")


def test_returnWith2PassedIn():
    checkFizzBuzz(2, "2")


def test_returnFizzWizzWith3PassedIn():
    checkFizzBuzz(3, "Fizz")


def test_returnFizzWizzWith5PassedIn():
    checkFizzBuzz(5, "Buzz")


def test_returnFizzWizzWith6PassedIn():
    checkFizzBuzz(6, "Fizz")


def test_returnFizzWizzWith10PassedIn():
    checkFizzBuzz(10, "Buzz")


def test_returnFizzWizzWith15PassedIn():
    checkFizzBuzz(15, "FizzBuzz")
