# Given an array. Shuffle its elements randomly so that each element is in a different place.
# Дан массив. Перемешать его элементы случайным образом так, чтобы каждый элемент оказался на новом месте.

from random import shuffle
from copy import copy


# def shuffle_list(lst):
#     old_lst = copy(lst)
#     shuffle(lst)
#     new_lst = lst
#
#     if old_lst != new_lst:
#         return lst
#     shuffle(new_lst)
#     # return new_lst

def shuffle_list(lst):
    return lst[-1:]+lst[:-1]


print(shuffle_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(shuffle_list(['a', 'b', 'c', 'd']))
print(shuffle_list(['one', '777', 12, 54, [1, 2]]))

# print([1,2,3] == [1,2])
