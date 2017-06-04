# 这是一个简易的ATM程序

### 作者介绍：
* author：PeiLingWu
* nickname: Amy
* My Blog:[http://www.cnblogs.com/peiling-wu/tag/Python/]

### 功能介绍
* 该程序分两种角色： 管理员和普通用户
* 管理员必须在登录后进行其他操作
* 管理员可新增用户并定义用户的额度为15000
* 管理员可查看用户信息
* 管理员可冻结账户
* 用户必须在登录后进行其他操作
* 用户可查询账户的基本信息
* 用户可提现，手续费5%
* 用户可账户间转账
* 用户可自行还款
* 用户可查询账单
* ATM记录操作日志

### 环境依赖：
* Python3.0+

### 目录结构：

    ShoppingSystem
    ├── __init__.py
    ├── README.md
    ├── bin #入口程序目录
    │   ├── __init__.py
    │   └── atm.py #入口程序
    ├── config #配置文件目录
    │   ├── __init__.py
    │   └── setting.py #配置文件
    ├── src #程序核心目录
    │   ├── __init__.py
    │   ├── account.py #调用用户处理
    │   ├── auth.py #用户
    │   ├── db_handler.py #数据处理
    │   ├── logger.py #日志
    │   ├── main.py #主要程序
    │   ├── transaction.py #算法
    ├── db #保存数据文件目录
    │   ├── accounts
    │   └── account_sample.py
    └── log #日志目录
    │   ├── __init__.py
    │   ├── access.log
    │   └── transactions.log

### 运行说明：
* 进行其他操作时必须先通过用户验证
