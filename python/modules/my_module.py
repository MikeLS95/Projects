_greeting = 'Hello World'
nums = [10, 20, 30]
person = {'name': 'John', 'age': 21}

def foo(person):
    print(f'{person.get("name", "Someone")} is {person.get("age", "unknown")} years old.')

def greet():
    print(_greeting)