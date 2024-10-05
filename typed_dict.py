from typing import TypedDict

class Movie(TypedDict):
    title: str
    year: int
    rating: float

# Creating a movie dictionary
movie: Movie = {
    "title": "Inception",
    "year": 2010,
    "rating": 8.8
}

print(movie)
