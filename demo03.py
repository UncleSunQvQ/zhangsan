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


# 更灵活的写法，要改动def __init__代码块及实例化，要注意添加'关键print'
class wuti():
    def __init__(self,chang,kuan,gao):
        self.chang = chang
        self.kuan = kuan
        self.gao = gao

    def yanse(self,num):
        print('物体的长为'+self.chang+'宽为'+self.kuan+'高为'+self.gao) #关键print
        if num == 1:
            print('蓝色')
        else:
            print('绿色')

    def qiwei(self):
        print('无')

dongxi = wuti('1','2','3')
dongxi.qiwei()
dongxi.yanse(1)
# print(dongxi.chang)

