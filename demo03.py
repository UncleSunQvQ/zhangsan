# 引用自带时间包
# import time
# for i in range(10):
#     time.sleep(1)
#     print(i)

# 引用自带随机数包
# import random
# a = random.randint(1,10)
# print(a)

'''
class 声明类的名字
然后类名首字母必须大写
面向对象编程
类里面所有的方法都必须传一个参数，叫self
'''

# 如果想要更灵活  1.需将def __init__(self):改为def __init__(self，sex,age,high)，然后self.sex = sex 类推  2.实例化时，zhangsan = gf()改为zhangsan = gf('女'，'18','170cm')
# class gf():
#     def __init__(self):
#         self.sex = '女'
#         self.age = '18'
#         self.high = '170cm'
    
#     def gexing(self,num):
#         print('你的女朋友性别为'+self.sex+'年龄为'+self.age+'身高为'+self.high)
#         if num == 1:
#             print('静若处子')
#         else:
#             print('动若脱兔')

#     def pinxing(self):

#         print('善良')

#     def work(self):
#         print('社畜')
    

# 类的实例化
# zhangsan = gf()
# zhangsan.work()
# zhangsan.gexing(1)
# print(zhangsan.age)

