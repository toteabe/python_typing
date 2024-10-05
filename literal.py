from typing import Literal

def set_status(status: Literal['active', 'inactive', 'pending']) -> None:
    print(f"Status set to {status}")

# Valid usages
set_status('active')    # Output: Status set to active
set_status('pending')   # Output: Status set to pending

# Invalid usage (static type checker like mypy will flag this)
# set_status('deleted')  # Error: Argument 'deleted' is not a valid Literal
