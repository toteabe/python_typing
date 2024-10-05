from typing import TypeVar, Generic

K = TypeVar('K')
V = TypeVar('V')

class Pair(Generic[K, V]):
    first: K
    second: V

    def __init__(self, first: K, second: V) -> None:
        self.first = first
        self.second = second

# Example usage
pair1 = Pair[int, str](1, "one")
pair2 = Pair[str, float]("pi", 3.14)

print(pair1.first, pair1.second)  # Output: 1 one
print(pair2.first, pair2.second)  # Output: pi 3.14
