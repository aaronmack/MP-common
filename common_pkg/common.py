#!/bin/bash

import os
import sys
import hashlib

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