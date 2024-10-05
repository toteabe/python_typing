from typing import TypeVar, Generic, List

# Define a type variable
T = TypeVar('T')

# Generic Stack class
class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

# Using Stack with integers
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
print(int_stack.pop())  # Output: 2

# Using Stack with strings
str_stack = Stack[str]()
str_stack.push("apple")
str_stack.push("banana")
print(str_stack.pop())  # Output: banana