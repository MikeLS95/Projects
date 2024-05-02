# with open('shopping-list.txt') as f:
#     for index, line in enumerate(f):
#         print(f'{index + 1}. {line.strip()}')
#     print([line.strip() for line in f])

# shows = [
#     'Mr. Robot',
#     'Fallout',
#     'The Walking Dead: Daryl Dixon',
#     'Game of Thrones'
# ]

# with open('tv-shows.txt', 'w') as f:
#     f.writelines([show+'\n' for show in shows])
    # f.write('Mr. Robot\n')
    # f.write('Fallout\n')
    # f.write('The Walking Dead: Daryl Dixon\n')
    # print(f.write(input("Enter a new show to our list! ")))

# import csv

# with open('people.csv') as f:
#     reader = csv.DictReader(f)
#     # reader.__next__()
#     for row in reader:
#         print(row)
#         # print(f'{row[0]} is {row[1]} years old')

menu = [
    {'item': 'Cappuccino', 'size': 'medium', 'price': 5.00},
    {'item': 'Latte', 'size': 'large',  'price': 7.00},
    {'item': 'Eggs Benedict', 'size': 'single', 'price': 17.50}
]

# with open('cafe-menu.csv', 'w') as f:
#     writer = csv.DictWriter(f, menu[0].keys())
#     writer.writeheader()
#     writer.writerows(menu)

import json, random

# with open('movies.json') as f:
#     movies = json.load(f)
#     m = movies[2]
#     print(f"{m['title']} was directed by {m['director']} and stars {random.choice (m['stars'])}")

# with open('menu.json', 'w') as f:
#     json.dump(menu, f, indent=4)


result = json.dumps(menu, indent=4)

new_menu = json.loads(result)

print(new_menu[0])