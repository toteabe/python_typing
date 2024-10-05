#Desde python 3.10 puedes reemplazar Union por carácter pipe |
def process_new(value: str | int) -> str:
    if isinstance(value, str):
        return f"Name: {value}"
    else:
        return f"ID: {value}"

print(process_new("Charlie"))  # Output: Name: Charlie
print(process_new(54321))      # Output: ID: 54321
