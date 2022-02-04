"""
Сегодня я решил тренироваться используя метод "лесенка". Для примера: 1 подтягивание - 2 подтягивания - 3 подтягивания - 2 - 1.
Задача: подсчитать общее колличество повторения за всю лесенку.
///
Today I decided to train using the "ladder" method. For example: 1 pull-up - 2 pull-ups - 3 pull-ups - 2 - 1.
Task: Count the total number of repetitions for the entire "ladder".
"""


def workout_1(step=1, sets=5):
    total = 0

    for i in range(step, step * sets + 1, step):
        total += i
    for j in range(step * (sets - 1), step - 1, -step):
        total += j

    return total


print(workout_1())
print(workout_1(2))
print(workout_1(3))
