# 这是一个简易的计算器

### 作者介绍：
* author：PeiLingWu
* nickname: Amy
* My Blog:[http://www.cnblogs.com/peiling-wu/tag/Python/]

### 功能介绍
* 用户可以进行加减乘除运算
* 按照括号，乘除，加减的优先级来计算

### 环境依赖：
* Python3.0+

### 目录结构：

    calculator
    ├── __init__.py
    ├── README.md
    ├── bin #入口程序目录
    │   ├── __init__.py
    │   └── calculator.py #入口程序
    ├── conf #配置文件目录
    │   ├── __init__.py
    ├── src #程序核心目录
    │   ├── __init__.py
    │   ├── main.py #调用程序的主函数
    │   ├── priority.py #根据优先级运算
    ├── db #保存数据文件目录
    │   ├── __init__.py
    └── log #日志目录
        └── __init__.py

### 运行说明：
* 该程序只能保留6位小数
* 小数多余6位会进行四舍五入
