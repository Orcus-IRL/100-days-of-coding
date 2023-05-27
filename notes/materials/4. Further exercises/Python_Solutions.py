Practice!

# Question 1

import sys

py_version = sys.version
print('You are using version',py_version)

# Question 2

names = input('Please enter names separated by commas: ')
name_list = names.split(',')
print(name_list)

# Question 3

def(number):
    if (abs(100 - number)) <= 10 or (abs(200 - number)) <= 10:
        return True
    else:
        return False

# Question 4

def print_nums(number_list):

    for item in number_list:
        while item > 0:
            value = str(item) * item
            print(value)

# Question 5

import multiprocessing
print(multiprocessing.cpu_count())

# Question 6

def digit_sum(number):
    sum = 0
    while number > 0:
        sum = sum + number % 10
        number = number // 10
    return sum

# Question 7

def pig_latin(word):
    vowels = ['a','e','i','o','u']
    front = None
    for index, char in enumerate(word):
        if char in vowels:
            front = word[index:]
            back = word[:index]
            break
    if not front:
        return 'No vowels!'
    translation = front + back + 'ay'
    return translation

# Question 8

def double(string):
    str_len = len(string)
    for i in range(str_len - 1):
        if string[i] == string[i+1]:
            return True

    return False

# Question 9
def palindrome(string):
    if string == string[::-1]:
        return True
    return False

# Question 10

def add_commas(number):

    str_number = str(number)

    str_number = str_number[::-1]
    comma = ','
    new_str = ''
    for i, num in enumerate(str_number):
        if i != 0 and (i % 3) == 0:
            new_str = new_str + comma
        new_str = new_str + num

    return new_str[::-1]

# Question 11

def to_binary(number):
    print(f'{number} in binary is {number:08b})

# Question 12

def check_sums(number):
    sum_1 = 0
    for i,v in enumerate(range(number+1)):
        sum_1 = sum_1 + v
    sum_2 = (number * (number + 1))/2

    return sum_1, sum_2

# Question 15
def convert_h_m(num):
  hours = num // 60
  mins = num % 60
  return str(hours) + 'h' + ':' + str(mins)  + ' mins'

# Question 16
def unique_items(my_list):
    if len(my_list) == len(set(my_list)):
        return True
    else:
        return False

# Question 17
def no_plus_sum(a,b):

    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a
# Explanation: https://stackoverflow.com/questions/17342042/why-this-code-for-additionusing-bitwise-operation-works-in-java

 # Question 18
def num_divisors(num):
    divisors = [i for i in range(1,num + 1) if num%i ==0]
    return (divisors, len(divisors))
# Question 19
def odd_even(num):
    if (num & 1):
        print('Odd')
    print('Even')

 # Question 20
def primes(start,end):
    primes = []
    for i in range(start,end+1):
        if i>1:
            for j in range(2,i):
                if i%j == 0:
                    break

            else:
                primes.append(i)
      return primes
      #(Note the use of the for/else clause here - it can be extremely useful - https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops)   
