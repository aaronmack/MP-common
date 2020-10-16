#!/bin/bash

import unittest
from common_pkg import common


class TestCommon(unittest.TestCase):
    def test_two_number_sum(self):
        assert common.two_number_sum(1, 1) == 2


if __name__ == '__main__':
    unittest.main()
