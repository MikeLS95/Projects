# x = int(input('What is X? '))
# y = int(input('what is Y? '))

# if x < y:
#     print('x is less than y')
# elif x > y: #else if
#     print('x is greater than y')
# else:
#     print('x is equal to y')

# print('Done')


# score = int(input("Score (0-100): "))

# if score >= 90:
#     print('HD')
# elif score >= 80:
#     print('D')
# elif score >= 70:
#     print('CR')
# elif score >= 50:
#     print('P')
# else:
#     print('F')

name = input('What is your name? ')

# if name == 'Harry':
#     print('Gryffindor')
# elif name == 'Ron':
#     print('Gryffindor')
# elif name == 'Hermione':
#     print('Gryffindor')
# elif name == 'Draco':
#     print('Slytherin')
# else:
#     print('Probably a muggle')

match name:
    case 'Harry' | 'Ron' | 'Hermione':
        print('Gryffindor')
    case 'Draco':
        print('Slytherin')
    case _:
        print('Muggle!')