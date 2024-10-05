from typing import Callable

# Function that takes a function as an argument
def apply_operation(x: int, y: int, op: Callable[[int, int], int]) -> int:
    return op(x, y)

# Define some operations
def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

# Use apply_operation
result1 = apply_operation(3, 4, add)       # 7
result2 = apply_operation(3, 4, multiply)  # 12

print(result1, result2)
