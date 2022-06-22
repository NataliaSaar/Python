# 1. Python script prints type of items in the list
my_list = [1, 'one', 23, 5.5]
for item in my_list:
    print(type(item))

# 2. Python script changing list items order
input_string = input('Please input a list of 5 element separated by space: ')
my_list = input_string.split()
print(my_list)
my_order = [1, 0, 3, 2, 4]
my_list = [my_list[i] for i in my_order]
print(my_list)

# 3. Python script shows season by month number
month = int(input("Input the month number (e.g. January - 1, February - 2 etc.): "))

if month in (12, 1, 2):
    season = 'winter'
elif month in (3, 4, 5):
    season = 'spring'
elif month in (6, 7, 8):
    season = 'summer'
else:
    season = 'autumn'

print(season)

# 4. Python script separating words to new lines
input_string = input('Please input a list element separated by space: ')
string = input_string.split()
print(string)
for word in string:
    print(word[0:10])

# 5. Python script sorting numbers together with input
my_list = [7, 5, 3, 3, 2]
number = int(input('Please input any number: '))
my_list.append(number)
my_list.sort()
my_list.reverse()
print(my_list)

# 6. Python script collecting and analyzing data about some goods
structure = []
keys = 'name', 'price', 'amount', 'type'
n = int(input('how many goods you want to register? '))
for i in range(n):
    input_string = input('type name, price, amount and type of goods you want to register with space separator: ')
    values = input_string.split()
    my_dict = dict(zip(keys, values))
    goods = i+1, my_dict
    structure.append(tuple(goods))

print(structure)

anadict = {}
for key in keys:
    key_name = '{}'.format(key)
    values = []
    for i in range(n):
        t1 = structure.__getitem__(i)
        d1 = t1.__getitem__(1)
        values.append(d1.get(key_name))
    anadict.update({key_name: values})

print(anadict)
