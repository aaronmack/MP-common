#!/bin/bash
# -*- coding: utf-8 -*-

import os
import sys
import platform


WIN_PLATFORM = True if platform.system() == "Windows" else False
LINUX_PLATFORM = True if platform.system() == "Linux" else False
OS_PLATFORM = True if platform.system() == "Darwin" else False
PYTHON_VERSION_3 = True if sys.version_info[0] == 3 else False
PYTHON_VERSION_2 = True if sys.version_info[0] == 2 else False
