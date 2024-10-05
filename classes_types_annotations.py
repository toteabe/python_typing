from typing import List

class Person:
    name: str
    age: int
    #Forward references (strings) are used when a class refers to itself or is not yet defined.
    friends: List['Person']

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.friends = []

    def add_friend(self, friend: 'Person') -> None:
        self.friends.append(friend)

    def get_friends_names(self) -> List[str]:
        return [friend.name for friend in self.friends]

# Creating instances
alice = Person("Alice", 30)
bob = Person("Bob", 25)
alice.add_friend(bob)

print(alice.get_friends_names())  # Output: ['Bob']
