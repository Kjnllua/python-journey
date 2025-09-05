# List and Dictionary Comprehension Practice

# %% 
# Question 1: Create a list of all the odd numbers between 1 and 30 using a list comprehension.
numbers = range(1, 31)
odd_numbers = [number for number in numbers if number % 2 != 0]

# %%
# Question 2:
"""
You have a list of numbers:
numbers = range(1, 11)
Create a dictionary where the key is the number and the value is its square.
"""
numbers = range(1, 11)
square_numbers = {number: number**2 for number in numbers}

# %%
# Question 3:
"""
From the list below:
fruits = ["apple", "banana", "cherry", "date", "kiwi", "mango"]
Create a list of all fruits that have more than 5 letters in their name.
"""
fruits = ["apple", "banana", "cherry", "date", "kiwi", "mango"]
five_letters = [fruit for fruit in fruits if len(fruit) > 5]

# %%
# Question 4 (Dictionary Comprehension with Filtering
"""
you have two lists:
animals = ["cat", "dog", "elephant", "giraffe", "ant"]
sizes   = ["small", "medium", "large", "large", "small"]
create a dictionary (using comprehension) that only includes the animals whose size is "large".
"""

animals = ["cat", "dog", "elephant", "giraffe", "ant"]
sizes = ["small", "medium", "large", "large", "small"]

filtered_animals = {
    animal: size for animal, size in zip(animals, sizes) if size == "large"
}

#  %%
# Question 5 (List Comprehension with Transformation)
"""
You have a list of words:
words = ["python", "comprehension", "practice", "fun"]
Create a new list where each word is transformed into uppercase using a list comprehension.
"""
words = ["python", "comprehension", "practice", "fun"]
trans = [word.upper() for word in words]

# %%
# Question 6 (Dictionary Comprehension with Numbers)
"""
You have a range of numbers:
numbers = range(1, 16)
Build a dictionary where each number is the key and the value is "even" if the number is even, or "odd" if the number is odd.
"""
numbers = range(1, 16)
num = {number: ("even" if number % 2 == 0 else "odd") for number in numbers}

# %%
# Question 7 (Nested List Comprehension):
# Make a 3×3 multiplication table (a list of lists) using a list comprehension.
table = [[row * col for col in range(1, 4)] for row in range(1, 4)]

# Question 8 (Nested List Comprehension with Condition):
# Build a 5×5 grid (list of lists) of numbers from 1 to 25, but only include even numbers inside each row.
grid = [
    [(row - 1) * 5 + col for col in range(1, 6) if ((row - 1) * 5 + col) % 2 == 0]
    for row in range(1, 6)
]
