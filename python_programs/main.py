# lst_1 = [1, 2, 3]
# lst_2 = [5, 6, 7]
#
#
# def lst_com(lst1, lst2):
#     lst_3 = [(lst1[i], lst2[j]) for i in range(0, len(lst1)) for j in range(0, len(lst2))]
#     return lst_3
#
#
# for i in lst_com(lst_1, lst_2):
#     print(i, end=' ')

from itertools import product
# a = map(int, input().split())
# b = map(int, input().split())

a = [1,2]
b = [3,4]
# print(type(a))
print(*product(a, b))



print('Ronak')