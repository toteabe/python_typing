#Prueba este código teniendo la extensión Mypy Type 
# 5xcChecker instalada  y habilitada
# revisando la pestaña de PROBLEMS los mensajes mypy

# Variable annotations
age: int = 25
name: str = "Bob"
surname: str = 1234
height: float = 5.6
is_student: bool = True

# Function annotations
def greet(name: str) -> str:
    return f"Hello, {name} {surname+1}!"

# Using the function
message = greet("Bob")
print(message)  # Output: Hello, Bob!