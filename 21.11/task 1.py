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

def find_duplicates(list_of_tuples):
    counter = Counter(list_of_tuples)
    duplicates = [item for item, count in counter.items() if count > 1]
    return duplicates

result = find_duplicates(all_variable)
list_of_variable = []
for nums in result:
    str_num = (''.join(nums))
    vatiant = '({})'
    rkekgne = vatiant.format(str_num)
    list_of_variable.append(rkekgne)
    
print(list_of_variable)
