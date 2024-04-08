import math
import random
from datetime import datetime, timedelta
from typing import Optional


# Simple Functions
def simple_function_a(x: int) -> int:
    """Adds 10 to the input."""
    return x + 10


def simple_function_b(s: str) -> str:
    """Reverses a string."""
    return s[::-1]


# Intermediate Functions
def intermediate_function_a(lst: list) -> int:
    """Calculates the sum of a list of numbers."""
    return sum(lst)


def intermediate_function_b(lst: list) -> list:
    """Sorts a list of numbers."""
    return sorted(lst)


# Advanced Functions
def advanced_function_a(date_str: str) -> str:
    """Converts a date string to a different format."""
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%d/%m/%Y')


def advanced_function_b(radius: float) -> float:
    """Calculates the volume of a sphere given its radius."""
    return (4 / 3) * math.pi * (radius ** 3)


# Super Advanced Functions
def super_advanced_function_a(n: int) -> int:
    """Generates a random number between 1 and 100."""
    return random.randint(1, 100)


def super_advanced_function_b(n: int) -> str:
    """Generates a random password."""
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    password = ''.join(random.choice(characters) for _ in range(n))
    return password


# Simple Functions
def simple_function_c(x: int) -> int:
    """Multiplies the input by 2."""
    return x * 2


def simple_function_d(x: int, y: int) -> int:
    """Calculates the sum of two numbers."""
    return x + y


# Intermediate Functions
def intermediate_function_c(lst: list) -> float:
    """Calculates the average of a list of numbers."""
    return sum(lst) / len(lst)


def intermediate_function_d(lst: list) -> list:
    """Filters a list of numbers to only include even numbers."""
    return [num for num in lst if num % 2 == 0]


# Advanced Functions
def advanced_function_c(text: str) -> str:
    """Capitalizes the first letter of each word in a sentence."""
    return ' '.join(word.capitalize() for word in text.split())


def advanced_function_d(n: int) -> bool:
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# Super Advanced Functions
def super_advanced_function_c(n: int) -> str:
    """Converts a number to its binary representation."""
    return bin(n)[2:]


def super_advanced_function_d(lst: list) -> Optional[int]:
    """Finds the maximum product of two integers in a list."""
    if len(lst) < 2:
        return None
    lst.sort()
    return max(lst[-1] * lst[-2], lst[0] * lst[1])


# Sample usage
print(simple_function_a(5))  # Output: 15
print(intermediate_function_a([1, 2, 3, 4, 5]))  # Output: 15
print(advanced_function_a("2024-04-10"))  # Output: "10/04/2024"
print(super_advanced_function_a(1))  # Output: Random number between 1 and 100
