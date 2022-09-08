import random

from python_lectures.lectures.secret_information import list_


# provide the function a list and return back one choice at random from the list
def random_output():
    value = random.choice(list_)
    return print(value)


if __name__ == "__main__":
    random_output()
