from itertools import permutations
from itertools import groupby
from collections import Counter

n = int(input())
con = (n - 1)
list_skob = []
i = 0

while i < con:
    i += 1
    list_skob.append('(')
    list_skob.append(')')
    
print(list_skob)
    
all_variable = list(permutations(list_skob))
def remove_duplicates(list_of_tuples):
    unique_items = set(list_of_tuples)
    return list(unique_items)


result = remove_duplicates(all_variable)
list_of_variable = []
for nums in result:
    str_num = (''.join(nums))
    vatiant = '({})'
    rkekgne = vatiant.format(str_num)
    list_of_variable.append(rkekgne)
    
print(list_of_variable)

