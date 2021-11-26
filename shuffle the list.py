# Given an array. Shuffle its elements randomly so that each element is in a different place.
# Дан массив. Перемешать его элементы случайным образом так, чтобы каждый элемент оказался на новом месте.

from random import randint


def shuffle_list(lst):
    new_list = lst[:]
    list_len = len(new_list)

    for i in range(list_len):
        rdm_index = randint(0, list_len - 1)
        temp = new_list[i]
        new_list[i] = new_list[rdm_index]
        new_list[rdm_index] = temp

    return new_list


print(shuffle_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(shuffle_list(['a', 'b', 'c', 'd']))
print(shuffle_list([11, '1111', [1, 2], 'b']))
