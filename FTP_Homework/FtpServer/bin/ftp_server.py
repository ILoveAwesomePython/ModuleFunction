#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu

import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import main

if __name__ == '__main__':
    main.ArvgHandler()
