# 1.

import sys
hours, rate, bonus = (int(x) for x in sys.argv[1:])

salary = (hours * rate) + bonus
print(salary)

# 2.

import random

randomlist = random.sample(range(10, 1000), 7)
print(randomlist)

new_list = []
for i in range(1, len(randomlist)):
    if randomlist.__getitem__(i) > randomlist.__getitem__(i - 1):
        new_list.append(randomlist.__getitem__(i))

print(new_list)

# 3.

list_gen = [i for i in range(20,240) if i % 20 == 0 or i % 21 == 0]
print(list_gen)

# 4.

from collections import Counter
#randomlist = random.sample(range(10, 100), 7)
randomlist = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(randomlist)
uni_list = [k for k,v in Counter(randomlist).items() if v==1]
print(uni_list)

# 5.

import random
from functools import reduce
def my_func(prev_el, el):
    return prev_el + el

print(reduce(my_func, [i for i in range(100, 1001) if i % 2 == 0]))

# 6.

from itertools import cycle, count

с = 0
for el in cycle(el for el in count(int(input('from which number to start?:\n'))) if el < 100):
    if с > 10:
        break
    print(el, el)
    с += 1

# 7.

def fact(n):
    count = 1
    fact = 1
    while count <= n:
        yield fact
        count += 1
        fact = fact * count

for el in fact(int(input('from where we start?\n'))):
    print(el)
