# -*-coding:utf-8 -*-
"""
通过{}和 ：来代替传统的 % 方式
"""

# ----------------------------------
"""
1、使用位置参数
要点：从以下例子可以看出位置参数不受顺序约束，且可以为{},只要format里有相对应的参数值即可,参数索引从0开，传入位置参数列表可用*列表
"""
l = ['Mike', 18]
print('my name is {}, age {}'.format('Mike', 18))
print('my name is {1}, age {0}'.format(18, 'Mike'))
print('my name is {}, age {}'.format(*l))

# ------------------------------------------
"""
2、使用关键字参数
要点：关键字参数值要对得上，可用字典当关键字参数传入值，字典前加**即可
"""
hash = {'name': 'John', 'age': 18}
print('my name is {name}, age {age}'.format(name='John', age=18))
print('my name is {name}, age {age}'.format(**hash))

# ------------------------------------------------------
"""
3、填充与格式化
[填充字符][对齐方式 <^>][宽度]
"""
print('{0:*>10}'.format(10))        # 右对齐
print('{0:*<10}'.format(10))        # 左对齐
print('{0:*^10}'.format(10))        # 居中对齐

# -------------------------------
"""4、精度与进制"""
print('{0:.2f}'.format(1/3))
print('{0:b}'.format(10))   # 二进制
print('{0:o}'.format(10))   # 八进制
print('{0:x}'.format(10))   # 十六进制
print('{:,}'.format(12369132698))   # #千分位格式化

# ----------------------------------
"""5、使用索引"""
a = ['hoho', 18]
print('name is {0[0]} age is {0[1]}'.format(a))

