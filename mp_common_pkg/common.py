#!/bin/bash

import os
import sys
import hashlib
from traceback import format_exc
from inspect import getframeinfo, stack

from mp_common_pkg import global_const


if global_const.WIN_PLATFORM:
    import colorama
    colorama.init()


def compute_md5(filename, chunk_4k=False):
    """
    Python function to find MD5 hash value of a file
    Args:
        chunk_4k(bool): using 4k chunk for read file
    """
    if chunk_4k:
        md5_hash = hashlib.md5()
        with open(filename,"rb") as f:
            # Read and update hash in chunks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                md5_hash.update(byte_block)

        return md5_hash.hexdigest()

    else:
        readable_hash = None
        with open(filename,"rb") as f:
            bytes = f.read() # read file as bytes
            readable_hash = hashlib.md5(bytes).hexdigest()
        return readable_hash


def exception_capture_single_line(fun):
    def _cap(*args, **kwargs):
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            print('Error execute: \x1b[6;30;35m' + ' %s \x1b[0m\n' % fun.__name__)

            print('Error info: %s' % e)
            print("%s:%s" % (getframeinfo(stack()[1][0]).filename, getframeinfo(stack()[1][0]).lineno))
    return _cap


def exception_capture_tracking_stack(fun):
    def _cap(*args, **kwargs):
        try:
            return fun(*args, **kwargs)
        except Exception:
            print('Error execute: \x1b[6;30;35m' + ' %s \x1b[0m\n' % fun.__name__)
            print('Error info: %s' % format_exc())
    return _cap


def two_number_sum(num_a, num_b):
    return num_a + num_b
