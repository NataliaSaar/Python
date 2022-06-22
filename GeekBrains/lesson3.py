# 1. Python script making division
def division(a, b):
    if b != 0:
        result = a / b
        print(result)
    else:
        print('Impossible zero division!')

input_string = input('Please type dividend and divisor: ')
div = input_string.split()
dividend = int(div.__getitem__(0))
divisor = int(div.__getitem__(1))
division(dividend, divisor)

# 2. Python script collecting data about user
def userdata(name, surname, birthday, location, email, phone_number):
     print(f"name - {name} {surname} from {location} has birthday at {birthday}, contacts - {email}, {phone_number}")

name = input('Please type your name:\n')
surname = input('Please type your surname:\n')
birthday = input('Please type your birthday:\n')
location = input('Please type your city:\n')
email = input('Please type your email:\n')
phone_number = input('Please type your phone number:\n')

userdata(name = name, surname = surname, location = location, birthday = birthday, email = email, phone_number = phone_number)
# 3. Python script making sum of biggest numbers

def sumofb(num1, num2, num3):

    nums = (num1, num2, num3)
    maxnum = sorted(nums)
    sumnum = maxnum[2] + maxnum[1]
    print(sumnum)

numinput = input('Please type 3 nunbers separated by space:\n')
div = numinput.split()
num1 = int(div.__getitem__(0))
num2 = int(div.__getitem__(1))
num3 = int(div.__getitem__(2))
sumofb(num1, num2, num3)

# 4. Python script elevating x in y:

def elevating(x, y):
    while y != 0:
        x = x * x
        y = y + 1

    x = 1/x
    print(x)

numinput = input('Please type positive number x and negative number y to elevate x to y:\n')
div = numinput.split()
x = int(div.__getitem__(0))
y = int(div.__getitem__(1))

elevating(x, y)

# 6. Python script which capitilize all words from input
def capit(*args):
    capwords = list()
    for word in words:
        word = word.capitalize()
        capwords.append(word)
    print(capwords)

word_input = input('Please type few words:\n')
words = word_input.split()
capit(words)

# 5. Python script making sum of numbers until N
def sumnum(*args):
    idx = 0
    global val
    for n in nums:
        try:
            numx = int(nums.__getitem__(idx))
            val = val + numx
            idx += 1

        except ValueError:
            print('final sum is %d' % val)
            print('exiting')
            quit()

    print('sum is %d' % val)


val = 0
while True:
    numinput = input('Please type numbers to sum or type N for exit:\n')
    nums = numinput.split()
    sumnum(nums)

