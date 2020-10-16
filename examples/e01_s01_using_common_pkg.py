#!/bin/bash

import mp_common_pkg


@mp_common_pkg.common.exception_capture_tracking_stack
def function_raise_error():
    raise AttributeError("I'm an error, please deal with me!")


if __name__ == "__main__":
    function_raise_error()