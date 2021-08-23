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



# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
# u = input('请输入用户名:')
# p = input('请输入密码:')
# if u == 'admin' and p == '123456':
#     print('验证成功')
# else:
#     print('验证失败')


# x = int(input('请输入x:'))
# if x > 1:
#     print(f'f(x) = 3 * {x} - 5','=',3*x-5)
# elif -1 <= x <= 1:
#     print(f'f(x) = {x} + 2','=',x+2)
# else:
#     print(f'f(x) = 5 * {x} + 3','=',5*x+3)

# import random
# a = random.randint(1,3)
# b = 0
# while True:
#     b += 1
#     c = int(input('请输入:'))
#     if c > a:
#         print('大于目标数字')
#     elif c < a:
#         print('小于目标数字')
#     else:
#         print('猜对了')
#         break
# print(f'共猜了{b}次')

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'x',i,'=',j*i,end='\t')
#     print()







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


# import random
# counters = [0] * 6
# for _ in range(6000):
#     face = random.randint(1, 6)
#     counters[face - 1] += 1
# for face in range(1, 7):
#     print(f'{face}点出现了{counters[face - 1]}次')

# items3 = []
# for x in 'ABC':
#     for y in '12':
#         items3.append(x + y)
# print(items3)


