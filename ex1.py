# -*- coding:utf-8 -*-

#=====================================================================
'''
# 函数
# 组织好的，可重复使用的，提高模块性
def hello():
    print("Hello world!")
hello()                                      # 函数调用
# 带参数的函数
def print_str(str):
    print(str)
    return
print_str("调用带参数的函数")
# 带有返回值的函数
def get_temp():
    return 20
temp = get_temp()
print("当前温度是：",temp)
# 函数有多个return时
def test():
    a = 11
    b = 22
    c = 33
    # return [a,b,c]                         # 封装成列表
    return a,b,c                             # 封装成元组
num = test()    
print(num)
# 函数的嵌套使用
def test1():
    print("----------1----------")
def test2():
    print("----------2----------")
def test3():
    test1()
    print("嵌套调用函数")
    test2()
test3()
'''
# 全局变量与局部变量
wendu = 0
def get_wendu():
    global wendu
    wendu = 33
def print_wendu(wendu):
    print("温度是%d度"%wendu)
get_wendu()
print_wendu(wendu)
#=====================================================================
'''
# 元组——与列表相同，不同之处在于元组的元素不能修改，元组使用()，列表使用[]
tuple = (1,2,3,"a","b","c","hello")
# 访问元组
print("tuple[1]:",tuple[1])
# 删除元组——元组中的元素值不允许删除，但是可以用del删除整个元组
'''
#=====================================================================
'''
# 遍历列表
list = [1,22,33,14,25,36]
for i in list:
    print(i)
else:
    print("for语句执行完成")
'''
#=====================================================================
'''
# 字典——另一种可变容器模型，且可以存储任意类型对象
dictionary = {"Name": "Li", "Age": 23, "Weight": 67}     # 定义字典
print("你的名字是%s,今年%d岁，体重%dkg。" %
      (dictionary['Name'], dictionary['Age'], dictionary['Weight']))
#----------------------------字典操作:增删改查---------------------------
# 增加元素
dictionary["add"] = "河北"
print(dictionary)
# 删除元素
del dictionary["Name"]                        # 删除的单独元素
#dictionary.clear()                            # 清空字典
print(dictionary)
# 修改元素
# dictionary["add"] = "南京"
# print(dictionary)
# 查询元素
print(dictionary.get("Age"))
'''
#=====================================================================
'''
# 列表——存储数据，可以是不同数据类型
list = ['hello','world',1,3.14,"li"]    # 定义列表
#----------------------------列表操作:增删改查---------------------------
# 插入
list.insert(1,"why")                    # 在固定位置插入
list.append("dong")                     # 在最后添加
# 删除
list.pop()                              # 从后往前删除
list.remove(3.14)                       # 根据内容删除
del list[0]                             # 删除元素list[0]
# 改变元素
list[0] = "name"                        # 指定位置修改
# 查询
if 1 in list:
    print("1在列表中")
if "this" not in list:
    print("这个元素不在列表中")
print(list)
'''
