#!/bin/bash

from mp_common_pkg import common
from mp_common_pkg import global_const


@common.exception_capture_tracking_stack
def function_raise_error():
    raise AttributeError("I'm an error, please deal with me!")


@common.exception_capture_single_line
def function_raise_error_too():
    raise AttributeError("I'm an error, please deal with me!")


def print_current_environment_info():
    print("if windows platform: {}".format(global_const.WIN_PLATFORM))
    print("if python version 3: {}".format(global_const.PYTHON_VERSION_3))


if __name__ == "__main__":
    function_raise_error()
    function_raise_error_too()