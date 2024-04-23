nums = [10, 14, 21, 50, 5, -6]
spam = ['cat', 'dog', 'bird', 'horse']

employees = [
    {'name': 'John', 'age': 36},
    {'name': 'Mary', 'age': 27},
    {'name': 'Bob', 'age': 40},
    {'name': 'Daniel', 'age': 40}
]


def square(x):
    return x ** 2

def cube(x):
    return x ** 3

# Create a list of the squares of nums
# squared_nums = []
# for num in nums:
#     squared_nums.append(square(num))

# squared_nums = list(map(square, nums))
squared_nums = [square(num) for num in nums]

even_numbers = list(filter(lambda x: x % 2 == 0, nums))
cubed_nums = list(map(lambda x: x ** 3, even_numbers))

# print(nums)
# print(squared_nums)
# print(cubed_nums)
# print(even_numbers)
# print(sorted(nums, reverse=True))

employees_over_30 = [x['name'] for x in employees if x['age'] >= 30]

print(employees_over_30)
# print(sorted(employees, key=lambda emp: emp['name']))
# print(max(employees, key=lambda emp: emp['age']))
# print(max(map(lambda emp: emp['age'], employees)))