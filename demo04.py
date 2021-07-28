# u = input('请输入用户名:')
# p = input('请输入密码:')
# if u == 'admin' and p == '123456':
#     print('验证成功')
# else:
#     print('验证失败')

# x = int(input('请输入x:'))
# if x > 1:
#     y = 3 * x - 5
#     # print(y)
# elif x < -1:
#     y = 5 * x + 3
#     # print(y)
# else:
#     y = x + 2
# print(y)
# print(f'{x},{y}')
# print('%d,%d' %(x,y))


# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))
# print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')

# r = float(input('请输入圆的半径:'))
# c = 2 * 3.14 * r
# s = 3.14 * r * r
# print(f'周长:{c:.1f},面积:{s:.1f}')
# print('周长:%.1f,面积:%.1f' %(c,s))


# a = float(input('请输入a:'))
# b = float(input('请输入b:'))
# c = float(input('请输入c:'))
# if a + b > c and a + c > b and c + b > a:
#     z = a + b + c
#     print(f'三角形的周长为:{z:.1f}')
#     print('三角形的周长为:%.1f' %z)
# else:
#     print('无法构成三角形')


# s = 0
# for i in range(0,101,2):
#     s += i
# print(s)

# import random
# a = random.randint(0,10)
# c = 0
# while a > 0:
#     c += 1
#     b = int(input('请输入:'))
#     if b > a:
#         print('大了')
#     elif b < a:
#         print('小了')
#     else:
#         print('猜对了')
#         break
# print('总共猜了',c,'次')

# def add(*jihe):
#     sum = 0
#     for i in jihe:
#         sum += i
#     return sum

# print(add(1,2,3))


# import demo03
# import demo02
# demo03.test()
# demo02.test()


# import demo03 as d3
# import demo02 as d2
# d3.test()
# d2.test()


# from demo03 import test
# test()

# from demo02 import test
# test()

# from demo03 import test as d3
# from demo02 import test as d2
# d3()
# d2()