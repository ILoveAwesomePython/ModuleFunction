# 这是一个简易的员工管理程序

### 作者介绍：
* author：PeiLingWu
* nickname: Amy
* My Blog:[http://www.cnblogs.com/peiling-wu/tag/Python/]

### 功能介绍
* 根据员工所在部门进行查询
* 根据入职日期进行模糊查询
* 根据输入的员工年龄范围进行查询
* 查到的信息，打印后，最后面要显示查到的条数
* 创建新员工，以phone做唯一键，staff_id自增（主键）
* 通过输入员工id删除员工
* 批量修改员工所在部门

### 环境依赖：
* Python3.0+

### 目录结构：

    StaffManagement
    ├── __init__.py
    ├── README.md
    ├── bin #入口程序目录
    │   ├── __init__.py
    │   └── ManageStaff.py #入口程序
    ├── conf #配置文件目录
    │   ├── __init__.py
    ├── modules #程序核心目录
    │   ├── __init__.py
    │   ├── SearchStaff.py #查询员工
    │   ├── AddNewStaff.py #添加新员工
    │   ├── DeleteStaff.py #删除员工
    │   ├── UpdateStaffInf.py #更新员工信息
    ├── db #保存数据文件目录
    │   ├── __init__.py
    │   ├── StaffInf.json
    │   └── DeptInf.json
    └── log #日志目录
        └── __init__.py

### 运行说明：

