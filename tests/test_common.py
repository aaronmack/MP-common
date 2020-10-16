#!/bin/bash

import unittest
from mp_common_pkg import common


def test_meta_info(ori_func):
    def wrapper(*args, **kwargs):
        result = ori_func(*args, **kwargs)
        print("TESTING FUNCTION: {}".format(ori_func.__name__))
    return wrapper


class TestCommon(unittest.TestCase):

    @test_meta_info
    def test_two_number_sum(self):
        assert common.two_number_sum(1, 1) == 2

    @test_meta_info
    def test_two_number_sum(self):
        assert common.two_number_sum(1, 1) == 2


if __name__ == '__main__':
    unittest.main()
