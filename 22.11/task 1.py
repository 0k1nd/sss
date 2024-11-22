'''Задача: Максимальная длина подмассива с одинаковыми числами после ограниченного изменения

Дан массив целых чисел nums и целое число k. Вы можете изменить не более k элементов массива на любое значение. 
Найдите максимальную длину подмассива, состоящего из одинаковых чисел, после выполнения изменений.
Пример 1

_


Ввод:
nums = [1, 1, 2, 2, 2, 1, 1]
k = 2
Вывод:
5
Объяснение:

    Можно изменить два элемента [1, 1, 2, 2, 2, 1, 1] → [2, 2, 2, 2, 2, 1, 1].
    Максимальный подмассив одинаковых чисел имеет длину 5.
____


Пример 2
Ввод:
nums = [1, 3, 3, 3, 4]
k = 1
Вывод:
4
Объяснение:

    Можно изменить один элемент [1, 3, 3, 3, 4] → [3, 3, 3, 3, 4].
    Максимальный подмассив одинаковых чисел имеет длину 4'''


from collections import Counter
from itertools import groupby


nums = [1, 1, 2, 2, 2, 1, 1]
k = int(input())

def iterlen(it):
    return sum(1 for _ in it)
 
def max_seq(s):
    result = {}
    for letter, group in groupby(s):
        l = iterlen(group)
        if result.get(letter, 0) < l:
            result[letter] = l
    return result

def get_result(list):
    max_key = max(max_seq(list), key=max_seq(list).get)
    result = max_seq(list)[max_key] + k
    if result <= len(list):
        print(result)
    else:
        print(len(list))

get_result(nums)