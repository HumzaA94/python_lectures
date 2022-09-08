import numpy as np
import pandas as pd

# Global Variables
bool_variable = True
int_variable = 1
string_variable = "word"
float_variable = 1.0


def ask(name, age=""):
    print(f"Name is {name} and I am {age} years old.")


def calculation(a, b):
    # if a and b are actually ints
    # clue for checking if number, use 'isinstance' function
    # https://www.w3schools.com/python/ref_func_isinstance.asp

    plus = a + b
    minus = a - b
    multiplication = a * b
    division = a / b
    formula_for_living_forever = (plus - minus) / multiplication * division

    return plus, minus, multiplication, division, formula_for_living_forever


if __name__ == "__main__":
    ask("Humza", age=29)
    plus, _, _, _, formula_for_living_forever = calculation(30, 10)
    _, minus, _, _, formula_for_living_forever = calculation(40, 2)
