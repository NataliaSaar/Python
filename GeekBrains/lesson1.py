#1. Python program to print some variables
name = input('type your name: ')
surname = input('type your surname: ')
age = input('type your age: ')
print(name, surname, age)

#2. Python program to convert seconds to timestamp %H:%M:%S
import time
seconds = int(input('type seconds to convert: '))
print(time.strftime('%H:%M:%S', time.gmtime(seconds)))

#3. Python program to add up n nn nnn numbers
n = int(input('type number :'))
nn = int("%s%s" % (n,n))
nnn = int("%s%s%s" % (n,n,n))
print(n + nn + nnn)

# 4. Python program to largest and smallest digit of a number
# Function to the largest and smallest digit of a number
def Digits(n):
    largest = 0
    while (n):
        r = n % 10
        largest = max(r, largest)
        n = n // 10

    print(largest)
n = int(input('type multi-digit number: '))
Digits(n)

#5. Python script counting rentability of company total and for each employee
revenue = float(input('enter revenue: '))
expenses = float(input('enter expenses: '))

if (revenue > expenses):
    amount = revenue - expenses
    print('Total Profit Amount = {0}'.format(amount))
    empnum = int(input('enter the number of employees: '))
    revperemp = amount / empnum
    print('Profit per employee = {0}'.format(revperemp))
elif (expenses > revenue):
    amount = expenses - revenue
    print('Total Loss = {0}'.format(amount))
else :
    print('No Profit No Loss!!!')


#6. Python script counting day when speed of athlete will be not less then b-parameter
print('The athlete is engaged in daily jogging. On the first day, his result was a kilometers. Every day, the athlete increased the result by 10% compared to the previous one. It is required to determine the number of the day for which the athletes result will be at least b kilometers.')
a = int(input('enter speed a: '))
b = int(input('enter speed b: '))
day = int(1)

while (a < b):
    day = day + 1
    a = a * 1.1

print('The athletes speed is not less then b-parameter on the day {0}'.format(day))