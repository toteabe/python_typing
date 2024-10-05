from typing import Protocol

#Drawable es como una interfaz de java, sólo tiene firma de métodos
class Drawable(Protocol):
    def draw(self) -> None:
        ...

class Circle:
    def draw(self) -> None:
        print("Drawing a circle")

class Square:
    def draw(self) -> None:
        print("Drawing a square")

def render(shape: Drawable) -> None:
    shape.draw()

# Using render with different shapes
circle = Circle()
square = Square()

render(circle)  # Output: Drawing a circle
render(square)  # Output: Drawing a square
