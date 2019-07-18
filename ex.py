# -*- coding:utf-8 -*-
# 字符串操作
'''
name = "abcdefABCDE"
print(name[-1])                  # 最后一个字幕
print(name[2:5])                 # cde：不包括name[5]
print(name[2:-2])                # cdefABC：不包括neme[-2]
print(name[2:-1])                # cdefABCD：不包括neme[-1]    
print(name[2:])                  # cdefABCD
print(name[2:-1:2])              # ceac:[开始：结束：步长]        
print(name[-1:])                 # E:默认步长为1
print(name[-1::-1])              # EDCBAfedcba:倒序
print(name[::-1])                # EDCBAfedcba:倒序
'''
# 字符串常见操作
my_str = "hello world I am li"
print(my_str.find("world"))      # 6:返回w的下标