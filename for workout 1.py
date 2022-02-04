"""
Сегодня я решил тренироваться используя метод "лесенка". Для примера: 1 подтягивание - 2 подтягивания - 3 подтягивания - 2 - 1.
Задача: подсчитать общее колличество повторения за всю лесенку.
///
Today I decided to train using the "ladder" method. For example: 1 pull-up - 2 pull-ups - 3 pull-ups - 2 - 1.
Task: Count the total number of repetitions for the entire "ladder".
"""


n = 1
total = 0
for i in range(n, n*5+1, n):
    total += i
for j in range(n*4,n-1, -n):
    total += j
print(total)