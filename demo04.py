# f = float(input('请输入华氏温度: '))

# c = (f - 32) / 1.8

# print('%.1f华氏度 = %.1f摄氏度' % (f, c))

# print(f'{f:.1f} 华氏度 = {c:.1f} 摄氏度')




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



# from random import randint

# a = randint(1,6)

# b = 0

# while True:

#     b += 1

#     c = int(input('请输入猜测的数字:'))

#     if c < a:

#         print('小了')

#     elif c > a:

#         print('大了')

#     else:

#         print('猜中了')

#         break

# print(f'一共猜了{b}次')


# 乘法表1
# for i in range(1,10):

#     for j in range(1,i+1):

#         print(j,'x',i,'=',j*i,end='\t')
#     print()

# 乘法表2
# i = 1
# print('-' * 50)
# while i < 11:
#     n = 1
#     while n < 11:
#         print('{:4d}'.format(i * n),end=' ')  # print(f'{i * n:4d}',end=' ')
#         n += 1
#     print()
#     i += 1
# print('-' * 50)


# 有 21 根棍子，首先用户选 1 到 4 根棍子，然后电脑选 1 到 4 根棍子。谁选到最后一根棍子谁就输。(用户和电脑一次选的棍子总数只能是 5)
# sticks = 21

# print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
# print("Whoever will take the last stick will lose")

# while True:
#     print("Sticks left: " , sticks)
#     if sticks == 1:
#         print("You took the last stick, you lose")
#         break
#     sticks_taken = int(input("Take sticks(1-4):"))
#     if sticks_taken >= 5 or sticks_taken <= 0:
#         print("Wrong choice")
#         continue
#     print("Computer took: " , (5 - sticks_taken) , "\n")
#     sticks -= 5






# 输出斐波那契数列前20个数

# a, b = 0, 1

# for _ in range(20):

#     a, b = b, a + b
#     print(a, end='  ')




# a = int(input('请输入正整数:'))

# is_prime = True

# for i in range(2,a):

#     if a % i == 0:

#         is_prime = False

#         break

# if a != 0 and is_prime == 1:

#     print(f'{a}是素数')

# else:

#     print(f'{a}不是素数')




# # 寻找水仙花数

# for a in range(1,10):

#     for b in range(0,10):

#         for c in range(0,10):

#             if a**3 + b**3 + c**3 == a*100 + b*10 + c:

#                 print(a*100+b*10+c)




# Craps赌博游戏
# from random import randint

# money = 1000

# while money > 0:

#     du = int(input('请下注:'))

#     if du > money:

#         print(f'余额不足,当前余额为{money}')

#         continue

#     else:

#         need_go_on = False

#         play = randint(1,6) + randint(1,6)

#         if play == 7 or play == 11:

#             money += du

#             print(f'玩家摇出了{play}点，玩家胜!余额为{money}')

#         elif play == 2 or play == 3 or play == 12:

#             money -= du

#             print(f'玩家摇出了{play}点，庄家胜!余额为{money}')

#         else:

#             need_go_on = True

#             print(f'玩家摇出了{play}点，游戏继续!')

#         while need_go_on:

#             play_2 = randint(1,6) + randint(1,6)

#             if play_2 == 7:

#                 money -= du

#                 need_go_on = False

#                 print(f'玩家摇出了{play_2}点，庄家胜!余额为{money}')

#             elif play_2 == play:

#                 money += du

#                 need_go_on = False

#                 print(f'玩家摇出了{play_2}点，玩家胜!余额为{money}')

#             else:

#                 print(f'玩家摇出了{play_2}点')

#                 continue

# print('玩家破产!')






# for x in range(0,21):

#     for y in range(0,34):

#         z = 100 - x - y

#         if 5*x + 3*y + z//3 == 100 and z % 3 == 0:

#             print(f'公鸡:{x} 母鸡:{y} 小鸡:{z}')






# a = float(input('请输入a:'))

# b = float(input('请输入b:'))

# c = float(input('请输入c:'))

# if a + b > c and a + c > b and c + b > a:

#     z = a + b + c

#     print(f'三角形的周长为:{z:.1f}')

#     print('三角形的周长为:%.1f' %z)

# else:

#     print('无法构成三角形')


# from random import randint

# a = randint(1, 10)

# c = 0

# while True:

#     b = int(input('请输入猜测的数字:'))

#     c += 1

#     if b > a:

#         print('大了')

#     elif b < a:

#         print('小了')

#     else:

#         print('猜对了')

#         break

# print(f'共猜了{c}次')





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








'''

设计一个生成指定长度验证码的函数。

说明：验证码由四位数字和英文大小写字母构成。
'''

# from random import randrange

# s = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# def yanzheng(scode=4):
#     code = ''

#     for _ in range(scode):

#         index = randrange(0,len(s))

#         code += s[index]

#     return code

# for _ in range(10):

#     print(yanzheng())


# 简便方法
# import random

# import string

# def yanzheng(scode=4):

#     s = string.digits + string.ascii_letters

#     return ''.join(random.choices(s,k=scode))

# for _ in range(10):

#     print(yanzheng())



# 设计一个函数返回给定文件名的后缀名

# def geshi(filename):

#     pos = filename.rfind('.')

#     return filename[pos+1:] if pos > 0 else ''

# print(geshi('a.txt'))

# print(geshi('a'))


# 简便方法

# from os.path import splitext


# def get_suffix(filename):

#     return splitext(filename)[1][1:]


# print(get_suffix('a.txt'))

# print(get_suffix('a'))



# import os
# import time


# content = '北 京 欢 迎 你 为 你 开 天 辟 地     '

# while True:

#     # Windows清除屏幕上的输出

#     os.system('cls')  
#     print(content)

#     time.sleep(0.5)

#     content = content[1:] + content[0]



# 将一颗色子掷6000次，统计每个点数出现的次数。
# import random

# tongji = [0] * 6

# for _ in range(6000):

#     dian = random.randint(1,6)

#     tongji[dian-1] += 1

# for dian in range(1,7):

#     print(f'{dian}点共出现{tongji[dian-1]}次')


# 练习
# from random import randint

# s = [0] * 6

# for _ in range(6000):

#     dianshu = randint(1,6)

#     s[dianshu-1] += 1

# for i,j in enumerate(s):

#     print(f'{i+1}点出现了{j}次')


# enumerate函数

# items = ['Python', 'Java', 'Go', 'Swift']


# for index in range(len(items)):

#     print(f'{index}: {items[index]}')


# for index, item in enumerate(items):

#     print(f'{index}: {item}')




# 录入5个学生3门课程的考试成绩，计算每个学生的平均分和每门课的平均分。

# names = ['关羽', '张飞', '赵云', '马超', '黄忠']

# courses = ['语文', '数学', '英语']

# # 用生成式创建嵌套的列表保存5个学生3门课程的成绩

# scores = [[0] * len(courses) for _ in range(len(names))]

# # 录入数据

# for i, name in enumerate(names):

#     print(f'请输入{name}的成绩 ===>')

#     for j, course in enumerate(courses):

#         scores[i][j] = float(input(f'{course}: '))
# print()

# print('-' * 5, '学生平均成绩', '-' * 5)

# # 计算每个人的平均成绩

# for index, name in enumerate(names):

#     avg_score = sum(scores[index]) / len(courses)

#     print(f'{name}的平均成绩为: {avg_score:.1f}分')
# print()

# print('-' * 5, '课程平均成绩', '-' * 5)

# # 计算每门课的平均成绩

# for index, course in enumerate(courses):

#     # 用生成式从scores中取出指定的列创建新列表

#     curr_course_scores = [score[index] for score in scores]

#     avg_score = sum(curr_course_scores) / len(names)

#     print(f'{course}的平均成绩为：{avg_score:.1f}分')


# 练习

# names = ['张三','李四']

# courses = ['语文','数学']

# scores = [[0] * len(courses) for _ in range(len(names))]

# for i,name in enumerate(names):

#     print(f'请输入{name}的成绩:')

#     for j,course in enumerate(courses):

#         scores[i][j] = float(input(f'{course}:'))

# print('学生平均成绩为:')

# for index,name in enumerate(names):

#     avg_score = sum(scores[index]) / len(courses)

#     print(f'{name}:{avg_score:.1f}')

# print('学科平均成绩为')

# for index,course in enumerate(courses):

#     s = [score[index] for score in scores]

#     avg_score = sum(s) / len(names)

#     print(f'{course}:{avg_score:.1f}')




# 设计一个函数返回指定日期是这一年的第几天

# def is_leap_year(year):

#     """判断指定的年份是不是闰年，平年返回False，闰年返回True"""

#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# def which_day(year, month, date):

#     """计算传入的日期是这一年的第几天

#     :param year: 年

#     :param month: 月

#     :param date: 日

#     """

#     # 用嵌套的列表保存平年和闰年每个月的天数

    # days_of_month = [

        # [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],

        # [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # ]

#     # 布尔值False和True可以转换成整数0和1，因此

#     # 平年会选中嵌套列表中的第一个列表(2月是28天)

#     # 闰年会选中嵌套列表中的第二个列表(2月是29天)

#     days = days_of_month[is_leap_year(year)]

#     total = 0

#     for index in range(month - 1):

#         total += days[index]

#     return total + date


# print(which_day(1980, 11, 28))    # 333

# print(which_day(1981, 12, 31))    # 365

# print(which_day(2018, 1, 1))      # 1

# print(which_day(2016, 3, 1))      # 61



