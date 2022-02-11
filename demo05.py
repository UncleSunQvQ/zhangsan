# 重复卡号
# from collections import Counter
# a = '''aaaaghghjhjhjhbdcba
# sdfdgfh
# sdfdgfh
# dsfdg
# dsfdg'''
# a = a.split()
# common = dict(Counter(a).most_common())
# # 所有
# print('-' * 7, '所有卡号', '-' * 6)
# for i,j in common.items():
#     print('|{}{}|'.format(i.ljust(20),j))
# print('-' * 7, '所有卡号', '-' * 6,'\n','\n')
# # 相同
# print('-' * 7, '重复卡号', '-' * 6)
# for i,j in common.items():
#     if j > 1:
#         print('|{}{}|'.format(i.ljust(20),j))
# print('-' * 7, '重复卡号', '-' * 6,'\n','\n')
# # 相同卡号列表
# print('相同卡号元组: ',tuple([i for i,j in common.items() if j > 1]))
