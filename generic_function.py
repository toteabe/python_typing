from typing import TypeVar, List

T = TypeVar('T')

def first_element(lst: List[T]) -> T:
    return lst[0]

# Examples
print(first_element([1, 2, 3]))          # Output: 1
print(first_element(["a", "b", "c"]))    # Output: a
