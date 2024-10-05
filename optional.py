from typing import Optional, Union

# Optional type (can be int or None)
optional_age: Optional[int] = None
optional_age = 25

# Union type (can be str or int)
name_or_id: Union[str, int] = "Alice"
name_or_id = 12345

# Function using Union
def process(value: Union[str, int]) -> str:
    if isinstance(value, str):
        return f"Name: {value}"
    else:
        return f"ID: {value}"

print(process("Bob"))   # Output: Name: Bob
print(process(67890))   # Output: ID: 67890
