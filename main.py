import os
from logger import logger

path = os.path.join(os.getcwd(), 'logs.txt')


# Тест работы генератора на простой функции:
# @logger(path)
# def summa(a, b):
#     return a + b


# summa(3, 5)


# Генератор из предыдущего ДЗ:
@logger(path)
def flat_generator(list_of_lists):
    for element in list_of_lists:
        for item_e in element:
            yield item_e


nested_list_g = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None]
]
for item in flat_generator(nested_list_g):
    print(item)
print('_________')


# Итератор из предыдущего ДЗ:
class FlatIterator:
    @logger(path)
    def __init__(self, list_of_lists):
        self.list = list_of_lists

    def __iter__(self):
        self.cursor_1 = 0
        self.cursor_2 = -1
        return self

    @logger(path)
    def __next__(self):
        self.cursor_2 += 1
        if len(self.list[self.cursor_1]) == self.cursor_2:
            if self.cursor_1 == len(self.list) - 1:
                raise StopIteration
            self.cursor_1 += 1
            self.cursor_2 = 0
        return self.list[self.cursor_1][self.cursor_2]


nested_list_i = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]
for item in FlatIterator(nested_list_i):
    print(item)
