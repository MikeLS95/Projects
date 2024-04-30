def my_decorator(func: 'function'):
    def wrapper():
        print('--------------------')
        func()
        print('--------------------')

    return wrapper


# @my_decorator
# def my_function():
#     print('This is my function')

# # x = my_decorator(my_function)

# # x()
# my_function()

def get_name(func):
    def wrapper():
        value = input('Enter your name: ')
        func(value)

    return wrapper

@get_name
def greet(name):
    print(f'Hello, {name}!')


greet()

@get_name 
def cya(name):
    print(f'Goodbye, {name}!')

cya()