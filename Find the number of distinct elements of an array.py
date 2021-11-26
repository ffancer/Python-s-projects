# Найти количество различных элементов массива. Пример: для 1 4 5 1 1 3 ответ 4.
# Find the number of distinct elements in the array. Example: for 1 4 5 1 1 3 the answer is 4.


def number_of_distinct(lst):
    return f"number of distinct elements in the {lst} - {len(set(lst))}"


print(number_of_distinct([1, 4, 5, 1, 1, 3]))

