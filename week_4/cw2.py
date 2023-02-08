from dataclasses import dataclass
from typing import List

# class Library:
#     def __init__(self, name, director, books):
#         self.name = name
#         self.director = director
#         self.books = books

#     def __str__(self):
#         return f"{self.name} {self.director} {self.books}"

#     def __eq__(self, lib2):
#         if self.name == lib2.name and self.director == lib2.director and self.books == lib2.books:
#             return True
#         else:
#             return False

@dataclass
class Library:
    name: str
    director: str
    books: List



lib1 = Library(2134, "AB", [])
lib2 = Library("SL", "BA", [])

print(lib1.name)
