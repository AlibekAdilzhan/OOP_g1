from typing import List

def my_mul(a: float, b: float) -> float:
    c: float = a * b
    return c

def my_mul_list(mylist: List[float]) -> float:
    return mylist

print(my_mul_list(["111", "234", "sdfk"]))