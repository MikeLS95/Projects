# def create(name, age, breed):
#     new_dog = {
#         'Name': name,
#         'Breed': breed,
#         'Age': age,
#         'walks': 0
#     }

#     return new_dog

# def walk(dog):
#     dog['walks'] += 1

class Dog:
    # Constructor method (whole thing)
    def __init__(self, name):
        # Creates a new attribute 'name' on self and copies the value of 'name' parameter into it.
        self.name = name
        self.action = 'sleeping'

    def greet(self, message='Hello'):
        print(f'{message} {self.name}!')

        