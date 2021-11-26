# Given an array. Shuffle its elements randomly so that each element is in a different place.
# Дан массив. Перемешать его элементы случайным образом так, чтобы каждый элемент оказался на новом месте.

from random import shuffle


def shuffle_list(lst):
    old_lst = lst[:]
    shuffle(lst)

    while lst != old_lst:
        return lst


print(shuffle_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(shuffle_list(['a', 'b', 'c', 'd']))
print(shuffle_list([11, '1111', [1, 2], 'b']))
