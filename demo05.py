# 无售有后续查询
# import sys
# names = sys.stdin.read()

# b = []
# names_list = [y for y in (x.strip() for x in names.splitlines()) if y]

# for i in names_list:
#     b.append(i.upper())
# print(tuple([item.zfill(16) for item in b]))



# 重复卡号
# from collections import Counter
# names = '''
# 04e5B5D2F94980
# 04e5B5D2F94980
# 04E5B5D2F94945
# '''
# b = []
# names_list = [y for y in (x.strip() for x in names.splitlines()) if y]
# for i in names_list:
#     b.append(i.upper())
# common = dict(Counter(b).most_common())
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


<<<<<<< HEAD


=======
>>>>>>> baf3d016b2fec204a8d5df1c95fbdea836863675
# 重复卡号
# from collections import Counter
# import sys
# names = sys.stdin.read()
# b = []
# names_list = [y for y in (x.strip() for x in names.splitlines()) if y]
# for i in names_list:
#     b.append(i.upper())
#     b = [item.zfill(16) for item in b]
# common = Counter(b).most_common()
# # 所有
# print('-' * 7, '所有卡号', '-' * 6)
# for i,j in common:
#     print('|{}{}|'.format(i.ljust(20),j))
# print('-' * 7, '所有卡号', '-' * 6,'\n','\n')
# # 相同
# print('-' * 7, '重复卡号', '-' * 6)
# for i,j in common:
#     if j > 1:
#         print('|{}{}|'.format(i.ljust(20),j))
# print('-' * 7, '重复卡号', '-' * 6,'\n','\n')
# # 相同卡号列表
<<<<<<< HEAD
# print('相同卡号元组: ',tuple([i for i,j in dict(common).items() if j > 1]))
=======
# print('相同卡号元组: ',tuple([i for i,j in dict(common).items() if j > 1]))
>>>>>>> baf3d016b2fec204a8d5df1c95fbdea836863675
