# Question 1
# Write a function print_numbers(n) that prints numbers from 1 to n using a loop.
def print_numbers(n):
    for num in range(1, n + 1):
        print(num)


# Question 2
# Write a function even_numbers(n) that returns a list of all even numbers up to n (including n if it’s even).
def even_numbers(n):
    is_even = []
    for num in range(1, n + 1):
        if num % 2 == 0:
            is_even.append(num)
        else:
            continue
    return is_even


# Question 3
# Write a function count_vowels(word) that counts how many vowels (a, e, i, o, u) are in a string.
def count_vowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    for letter in word.lower():
        if letter in vowels:
            count += 1

    return count


# Question 4
# Write a function multiply_list(numbers) that takes a list of numbers and returns the product of them all.
def multiply_list(numbers):
    product = 1
    for num in list(numbers):
        product *= num

    return product


# Question 5#
# Write a function factorial(n) that returns the factorial of n using a loop.
def factorial(n):
    number = range(1, n + 1)
    product = 1

    for num in number:
        product *= num

    return product


# Question 6
# Write a function reverse_list(lst) that returns the reversed list without using slicing ([::-1]) or the built-in reverse() method.
def reverse_list(lst):
    new_list = []

    for item in lst:
        new_list.insert(0, item)

    return new_list


# Question 7
# Write a function sum_all(*args) that returns the sum of all numbers passed in, no matter how many there are.
def sum_all(*nums):
    return sum(nums)


# Question 8
# Write a function greet(**kwargs) that prints a greeting message depending on the keywords provided.
def greet(**details):
    if "name" in details and "age" in details:
        print(f"Hello {details['name']}, you are {details['age']} years old.")
    elif "name" in details:
        print(f"Hello {details['name']}.")
    elif "age" in details:
        print(f"Hello, you are {details['age']} years old.")

# Question 9
'''
Write a function fizzbuzz(n) that prints numbers from 1 to n, but:
   - For multiples of 3 → print "Fizz"
   - For multiples of 5 → print "Buzz"
   - For multiples of both 3 and 5 → print "FizzBuzz"
   - Otherwise → print the number itself
'''
def fizzbuzz(n):
    numbers = list(range(1, n+1))

    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Question 10
# Write a function find_max(numbers) that finds the largest number in a list without using Python’s built-in max() function.
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Question 11
"""
Write a function word_lengths(words) that takes a list of words and returns a dictionary where:
- Each word is a key
- Its length is the value
"""
def word_lengths(words):
    word_dict = {}
    for word in words:
        word_dict.update({word: len(word)})
    return word_dict

# Question 12
# Write a function prime_numbers(n) that returns a list of all prime numbers up to n.
def prime_numbers(n):
    is_prime = []

    for num in range(2, n+1):
        for divisor in range(2, num):
            if num % divisor == 0:
                break
        else:
            is_prime.append(num)
    return is_prime
