import random
from datetime import datetime
import math
import re
import itertools


# Simple Functions

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


print(greet("Alice"))  # Output: Hello, Alice! (Independent)


def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


print(add(3, 5))  # Output: 8 (Independent)


# Intermediate Functions

def get_random_number(start: int, end: int) -> int:
    """Return a random number within a range."""
    return random.randint(start, end)


print(get_random_number(1, 10))  # Output: Random number between 1 and 10 (Independent)


def get_current_time() -> str:
    """Return the current time."""
    return datetime.now().strftime("%H:%M:%S")


print(get_current_time())  # Output: Current time in HH:MM:SS format (Independent)


# Advanced Functions

def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle."""
    return math.pi * radius ** 2


print(calculate_circle_area(5))  # Output: Area of a circle with radius 5 (Independent)


def is_email_valid(email: str) -> bool:
    """Check if an email address is valid."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


print(is_email_valid("example@example.com"))  # Output: True (Independent)


# Super Advanced Functions

def generate_permutations(items: list) -> list:
    """Generate all possible permutations of a list."""
    return list(itertools.permutations(items))


print(generate_permutations([1, 2, 3]))  # Output: All permutations of [1, 2, 3] (Independent)


def calculate_fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)


print(calculate_fibonacci(5))  # Output: 5th Fibonacci number (Dependent on calculate_fibonacci)
