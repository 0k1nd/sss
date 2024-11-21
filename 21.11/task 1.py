'''Учитывая n пар круглых скобок, напишите функцию, которая генерирует все комбинации правильных круглых скобок.

Пример 1:

Вход: n = 3
Выход: ["((()))","(()())","(())()","()(())","()()()"]

Пример 2:

Вход: n = 1
Выход: ["()"]


Ограничения:

    1 <= п <= 8
'''



from itertools import permutations
from itertools import groupby
from collections import Counter

n = int(input())
list_skob = []
i = 0

while i < n:
    i += 1
    list_skob.append('(')
    list_skob.append(')')
    
    
all_variable = list(permutations(list_skob))
def remove_duplicates(list_of_tuples):
    unique_items = set(list_of_tuples)
    return list(unique_items)

result = remove_duplicates(all_variable)
list_of_variable = []
answer = []
   
for combination in result:
    counter = 0
    list_of_variable.append(combination)
    for item in combination:
        if item == ')':
            counter -= 1
        elif counter < 0:
            list_of_variable.remove(combination)
            break
        elif item == '(':
            counter += 1  
    
for nums in list_of_variable:
    str_num = (''.join(nums))
    answer.append(str_num) 

print(answer)
