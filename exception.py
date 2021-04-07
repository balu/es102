# Define the error.
class NameNotCapitalizedError(Exception):
    pass

class NameTooLongError(Exception):
    pass

def greeting(name):
    if len(name) > 10:
        raise NameTooLongError
    if name[0].isupper():
        print(f"Hello {name}.")
    else:
        raise NameNotCapitalizedError

# Handle the error.
try:
    name = input("Enter your name: ")
    greeting(name)
except NameNotCapitalizedError:
    print(f"Name {name} is not properly capitalized.")
except NameTooLongError:
    print(f"Name {name} is too long.")