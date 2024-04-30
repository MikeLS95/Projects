spam = ['cat', 'dog', 'bird', 'horse']
eggs = [12, 78, 100, 5.4, 42]
# person = ['Mike', 28, 180]
tic_tac_toe = [
    ['', '', ''],
    ['', 'X', ''],
    ['', '', '']
]

for i in range(len(spam)):
    print(spam[i])

for index, animal in enumerate(spam, 1):
    print(f'{index}. {animal}')

print(list(enumerate(spam, 1)))

# x = 'bird'
# if x in spam:
#     print(spam.index(x))

# def display_person(person):
#     # name = person[0] # First name
#     # age = person[1]
#     # height = person[2]
#     name, age, height = person
#     print(f'{name} is {age} years old and {height}cm tall.')

# me = ['Mike', 28, 180]
# display_person(me)
