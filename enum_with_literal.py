from enum import Enum
from typing import Literal

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

def paint(color: Literal['red', 'green', 'blue']) -> None:
    print(f"Painting in {color}")

# Using with enum values
paint(Color.RED.value)    # Output: Painting in red
paint("green")            # Output: Painting in green

# paint("yellow")        # Type checker error
