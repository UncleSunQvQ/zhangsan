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


# 二维元组
# a = (1,1.1,'ceshi',1)
# b = (a,'haha','xixi')
# print(b[0][1])


# 切片
# a = (1,1.1,'ceshi',1)
# print(a[0:2]) #左闭右开
# print(a[2:])


# 数组 在数组中添加数据的两种方式 （PS：元组完成以后不可以修改，数组可以修改）
# 方式一
# a = [1,1.1,'ceshi',False,True] # 数组
# a.append('append1') # 往数组中增加数据，在尾部添加
# a.append('append2')
# print(a)

# 方式二
# a = [1,1.1,'ceshi',False,True] # 数组
# a.insert(0,1) # 往数组中增加数据，在下标处添加
# print(a)


# 数组的剪切
# a = [1,1.1,'ceshi',False,True] # 数组
# b = a.pop(0) # 剪切
# c = a.pop(0) # 剪切
# print(b+c)
# print(b)

# 数组的清除
# a = [1,1.1,'ceshi',False,True] # 数组
# a.clear() # 清除数组
# print(a)

# 清除数组中的固定数据
# a = [1,1.1,'ceshi',False,True] # 数组
# a.remove('ceshi')
# print(a)


# 数组的合并
# a = [1,1.1,'ceshi',False,True] # 数组
# xx = ['nihao','buaho']
# a.extend(xx) #合并数组
# print(a) #合并方式一
# print(a+xx) #合并方式二

# 数组中数据的统计（False是0，True是1）
# a = [1,1.1,'ceshi',False,True]
# b = a.count(1)
# print(b)

'''
字典的特点
1.字典中的值没有顺序
2.字典的结构必须是 键值对的结构  key:value
'''

# 取值-方式一
# a = {'name':'张三','age':18}
# print(a['name']) 

# 取值-方式二
# a = {'name':'张三','age':18}
# b = a.get('name') 
# print(b)

# 取值-方式三
# a = {'name':'张三','age':18}
# b = a.pop('name')
# print(b)

# 三种取值的区别
# a = {'name':'张三','age':18}
# print(a.get('name1')) # 若值不存在，不报错
# print(a.pop('name1')) # 若值不存在，报错
# print(a['name1']) # 若值不存在，报错

# 新增
# a = {'name':'张三','age':18}
# a['high'] = '183cm' 
# print(a)

# 修改
# a = {'name':'张三','age':18}
# a['name'] = '李四'
# print(a)

# a = {'name':'张三','age':18}
# a.update(phone = 222,name = '赵六') # 有就更新，没有就新增
# print(a)

# 删除
# a = {'name':'张三','age':18}
# del a['name']
# print(a)

# 练习
# name = input('请输入名字:')
# age = input('请输入年龄:')
# sex = input('请输入性别:')
# userinfo = {}
# userinfo.update(name = name,age = age,sex = sex)
# print(userinfo)

