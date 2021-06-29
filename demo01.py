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

# a = (1,1.1,'ceshi',1)
# print(a[2])

# print(a.index('ceshi'))
# print(a.count(1))

# b = (a,'haha','xixi')
# print(a[0:2]) #左闭右开
# print(a[2:])

a = [1,1.1,'ceshi',False,True]
# a.append('append1')
# a.append('append2')
# a.insert(0,1)
# b = a.pop(0) # 剪切
# c = a.pop(0) # 剪切
# print(b+c)
# print(b)
# a.clear() # 清除
# xx = ['nihao','buaho']
# a.extend(xx) #合并数组
# print(a+xx)
b = a.count(1)
print(b)