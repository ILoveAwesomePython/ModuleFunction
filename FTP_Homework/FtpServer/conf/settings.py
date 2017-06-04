#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USER_HOME = "%s/home"%BASE_DIR
LOG_DIR = "%s/log"%BASE_DIR

LOG_LEVEL = "DEBUG"

ACCOUNT_File = "%s/conf/account.cfg"%BASE_DIR

HOST = "0.0.0.0"
PORT = 9999