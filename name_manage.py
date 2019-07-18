# -*- coding:utf-8 -*-
# 名字管理系统
# 打印功能提示
print("="*50)
print("                   名字管理系统")
print("1:添加一个名字") 
print("2:删除一个名字") 
print("3:修改一个名字") 
print("4:查询一个名字") 
print("5:退出系统") 
print("="*50)
names = []                                   # 定义一个空的名字列表
while True:
    # 获取用户命令
    num = int(input("请输入您的选择："))
    # 根据用户选择，执行相应操作
    if num==1:
        new_name = input("请输入一个名字：")
        names.append(new_name)
        print(names)
    elif num==2:
        del_name = input("请输入要删除的文字：")
        names.remove(del_name)
        print(names)
    elif num==3:
        pass
    elif num==4:
        find_name = input("请输入要查询的名字：")
        if find_name in names:
            print("要查找的名字在列表中")
        else:
            print("要查找的名字不在列表中")
    elif num==5:
        break
    else:
        print("输入有误，请重新输入")