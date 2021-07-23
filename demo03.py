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
默认属性方法_init_
使用_init_来接受参数
每个类里面的方法，第一个参数必须是self
面向对象编程
类里面所有的方法都必须传一个参数，叫self
'''


# class Gf():
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
# zhangsan = Gf() # 类的实例化
# zhangsan.work()
# zhangsan.gexing(1)
# print(zhangsan.age)


# 更灵活的写法，要改动def __init__默认属性方法及实例化，要注意添加'关键print'
class Wuti():
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

dongxi = Wuti('1','2','3')
dongxi.qiwei()
dongxi.yanse(1)
print(dongxi.gao)


# 类的继承   Wuti:父类   Newwuti:子类
# class Newwuti(Wuti):
#     pass

# dongxi = Newwuti('1','2','2')
# dongxi.yanse(1)
# print(dongxi.gao)


# 类的重写/多态
class Newwuti(Wuti):
    def qiwei(self):
        print('氨味')

dongxi = Newwuti('3','3','3')
dongxi.qiwei()