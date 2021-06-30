'''
print ('hello world!') #字符串
print (2) #整数
print (2.2) #小数
print (2<3) #布尔值
print ('拼'+'接') #字符串拼接
print (23333,55555) #打印多条
print (9-8+1*(1+1))
'''
'''
所有的方法都是小括号，比如print()  input()
元组，数组，字典的取值，都是用[]，比如a[8]
'''

# a = input('请输入:')
# b = input('请输入:')
# print('长度和为:',len(a)+len(b))

# print(type('ha'))
# print(type(1))
# print(type(1.1))
# print(type(()))
# print(type([]))
# print(type({}))

# 元组
# a = (1,1.1,'ceshi',1) # 元组

# 下标
# print(a[2]) 
# print(a.index('ceshi'))
# print(a.count(1))

# b = (a,'haha','xixi')
# print(b[0][0])

# 切片
# print(a[0:2]) #左闭右开
# print(a[2:])

# 数组 PS：元组完成以后不可以修改，数组可以修改
# a = [1,1.1,'ceshi',False,True] # 数组
# a.append('append1') # 往数组中增加数据，在尾部添加
# a.append('append2')
# a.insert(0,1) # 往数组中增加数据，在下标处添加
# b = a.pop(0) # 剪切
# c = a.pop(0) # 剪切
# print(b+c)
# print(b)
# a.clear() # 清除
# xx = ['nihao','buaho']
# a.extend(xx) #合并数组
# print(a)
# print(a+xx)
# b = a.count(1)
# print(b)

'''
字典的特点
1.字典中的值没有顺序
2.字典的结构必须是 键值对的结构  key:value
'''

# a = {'name':'张三','age':18}
# a['high'] = '183cm'
# a['name'] = '李四'
# a.pop('name')
# print(a)

# b = a.get('name')
# print(b)

# a.update(phone = 222,name = '赵六') # 有就更新，没有就新增
# print(a)

# print(a.get('name1')) # 若值不存在，不报错
# print(a['name1']) # 若值不存在，报错
# del a['name']
# print(a)


# name = input('请输入名字:')
# age = input('请输入年龄:')
# sex = input('请输入性别:')
# userinfo = {}
# userinfo.update(name = name,age = age,sex = sex)
# print(userinfo)

