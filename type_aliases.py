from typing import List, Tuple

# Type alias for a list of tuples (name, age)
People = List[Tuple[str, int]]

def process_people(people: People) -> None:
    for name, age in people:
        print(f"{name} is {age} years old.")

# Using the function
group: People = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
process_people(group)
