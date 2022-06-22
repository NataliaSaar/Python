# 1.
with open("text.txt", "a") as y:
    while True:
        x = input("Enter blah, or leave string empty to finish:\n")
        if x != '':
            y.writelines(x + '\n')

        else:
            print('bye!')
            break

# 2.
with open("text.txt", "r") as file:

    number_of_lines = 0
    number_of_words = 0
    number_of_characters = 0
    for line in file:
        line = line.strip("\n")
        words = line.split()
        number_of_lines += 1
        number_of_words += len(words)
        number_of_characters += len(line)

print("lines:", number_of_lines, "words:", number_of_words, "characters:", number_of_characters)

# 3.

import statistics
with open("salary.txt", "r") as file:
    salaries = []
    for line in file:
        line = line.strip("\n")
        values = line.split()
        salary = float(values.__getitem__(1))
        worker = values.__getitem__(0)
        salaries.append(salary)
        if salary < 20000:
            print(worker, salary)
    print('Median of all salaries is: ', statistics.mean(salaries))

# 4.
import io
with io.open('numbers.txt', 'r', encoding='utf-8') as source:
    with io.open('numbers_new.txt', 'a', encoding='utf-8') as dest:
        for line in source:
            line = line.strip("\n")
            values = line.split()
            number_str = values.__getitem__(0)
            if number_str == 'One':
                string = 'Один', values.__getitem__(1), values.__getitem__(2), '\n'
                dest.writelines(string)
            elif number_str == 'Two':
                string = 'Два', values.__getitem__(1), values.__getitem__(2), '\n'
                dest.writelines(string)
            elif number_str == 'Three':
                string = 'Три', values.__getitem__(1), values.__getitem__(2), '\n'
                dest.writelines(string)
            elif number_str == 'Four':
                string = 'Четыре', values.__getitem__(1), values.__getitem__(2), '\n'
                dest.writelines(string)
            else:
                print('bye!')
                break

# 5.

import random
with open('numforsum.txt', 'a') as file:
    for i in range(9):
        file.write(' ')
        file.write(' '.join(str(random.randint(2, 10))))
with open('numforsum.txt', 'r') as file:
    for line in file:
        numbers = line.split(' ')
        numbers.pop(0)
        print(numbers)
        print(sum(map(int,numbers)))

#6.

import io
with open('lessons.txt', 'r', encoding='utf-8') as file:
    disciplines = {}
    for line in file:
        line = line.strip("\n")
        values = line.split()
        discipline = values.__getitem__(0)
        lessons = [int(s) for s in values if s.isdigit()]
        lesnum = sum(lessons)
        disciplines.__setitem__(discipline, lesnum)
    print(disciplines)

#7.

import statistics
import json
with open('firms.txt', 'r') as file:
    firms = {}
    numbers_for_median = []
    median_profit = {}
    for line in file:
        line = line.strip("\n")
        values = line.split()
        firm = values.__getitem__(0)
        numbers = [int(s) for s in values if s.isdigit()]
        proceeds = numbers.__getitem__(0)
        expenses = numbers.__getitem__(1)
        profit = proceeds - expenses
        firms.__setitem__(firm, profit)
        if profit >= 0:
            numbers_for_median.append(profit)
    median_profit.__setitem__('average_profit:', statistics.mean(numbers_for_median))
    with open('firms_data.json', 'a') as json_f:
        json.dump(firms, json_f)
        json.dump(median_profit, json_f)
