# 判断
# a = int(input('请输入第一位数字:'))
# b = int(input('请输入第二位数字:'))
# if a > b:
#     print('前者大于后者:')
# elif a == b:
#     print('前者等于后者')
# else:
#     print('后者大于前者')

'''
if-if  与  if-elif 的区别:只要都满足就会遍历所有if，而elif只要满足之前的if就不会再继续执行语句
'''

# exit()会直接结束
# a = input('请输入1-9的数字:')
# if a == '':
#     print('不能为空')
#     exit()
# if a in '0123456789':
#     a = int(a)
# else:
#     print('请输入正确数字')
#     exit()
# if a > 5:
#     print('大')
# else:
#     print('小')

# a = input('请输入0-9的数字:')
# if a == '':
#     print('不能为空')
# if a in '0123456789':
#     a = int(a)
# else:
#     print('请输入数字')
# if a > 5:
#     print('比5大')
# else:
#     print('小于等于5')


# a = 1
# if type(a) is int:
#     print('数据类型为数字')
# else:
#     print('数据类型不是数字')

# a = 0
# while a < 2:
#     print('哈哈')
#     a = a + 1

# highchengji = {} # 合格数组
# lowchengji = {} # 不合格数组
# studentlist = ['张三','李四','王五'] # 学生列表
# a = 0 # 定义一个下标
# while a < len(studentlist): # 利用下标和长度的关系做循环输入
#     chengji = int(input('请输入'+studentlist[a]+'的成绩:')) # 输入学生成绩
#     if chengji >= 60:
#         highchengji[studentlist[a]] = chengji # 大于等于60的存入合格数组
#     else:
#         lowchengji[studentlist[a]] = chengji # 小于60的存入不合格数组
#     a = a + 1
# print('合格的人：',highchengji)
# print('不合格的人:',lowchengji)


    
# h = {}
# l = {}
# s = ['张三','李四','王五']
# for i in s:
#     c = int(input('请输入'+i+'的成绩为:'))
#     if c < 60:
#         l[i] = c
#     else:
#         h[i] = c
#     print('合格学生名单:',h)
#     print('不合格学生名单:',l)

# 遍历
# a = ['张三','李四','王五']
# for i in a:
#     print(i)

# b = list(range(0,100,30)) # 自动生成一个数列，步进/步长
# print(b)



# for循环练习
# highchengji = {}
# lowchengji = {}
# a = ['张三','李四','王五']
# for i in a:
#     b = int(input('请输入'+i+'的成绩:'))
#     if b < 60:
#         lowchengji[i] = b
#     else:
#         highchengji[i] = b
# print('合格的人：',highchengji)
# print('不合格的人:',lowchengji)




# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'*',i,' =',j*i,end='  ')
#     print()



# 红绿灯练习
# light = {'红灯':35,'绿灯':30,'黄灯':5}
# while True:
#     for i in light:
#         for j in range(light[i]):
#             print('距离',i,'结束','还有',light[i]-j,'秒')


# 注册练习
# u = input('请输入账号:')
# p = input('请输入密码:')
# if 5 <= len(u) <= 8:
#     if u[0] in 'a':
#         if 6 <= len(p) <= 10:
#             print('注册成功',{u:p})
#         else:
#             print('密码长度为6-10位')
#     else:
#         print('首字母必须为a')
# else:
#     print('账号为5-8位')





# for i in range(10):
#     if i == 4:
#         continue # 跳过循环
#     print(i)

# for i in range(10):
#     if i == 4:
#         break # 跳出循环
#     print(i)


# 方法的定义
# def ceshiu(u):
#     if 5 <= len(u) <= 8:
#         if u[0] in 'a':
#             print('ok')
#         else:
#             print('账号必须以a开头')
#     else:
#         print('账号长度为5-8位')
# ceshiu('a256')

# def jiafa(a,b):
#     if type(a) is int and type(b) is int:
#         return a+b
#     else:
#         return '输入的数据类型必须为数字'
# print(jiafa(12,20))


# 返回,以及自己写方法
# def ceshi(u):
#     if 5 <= len(u) <= 8:
#         if u[0] in 'a':
#             return True
#         else:
#             return '首字母必须为a'
#     else:
#         return '账号长度为5-8位'


# u = input('请输入账号:')
# if ceshi(u) == True:
#     print('注册成功')
# else:
#     print(ceshi(u))



# 捕获异常
# try:
#     print('1'+2)
# except Exception as e:
#     print('上面的代码写错了!',e)