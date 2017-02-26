# ATM 执行程序即启动程序,启动程序里面不写逻辑

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)) ))

from src import main

if __name__ == '__main__':
    main.run()

