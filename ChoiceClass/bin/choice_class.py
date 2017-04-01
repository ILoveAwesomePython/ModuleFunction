#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import admin_run

if __name__ == '__main__':
    admin_run.admin_role()