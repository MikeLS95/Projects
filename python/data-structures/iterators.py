nums = [10, 14, 21, 50, 5, -6]

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

# Create a list of the squares of nums
# squared_nums = []
# for num in nums:
#     squared_nums.append(square(num))

squared_nums = list(map(square, nums))
cubed_nums = list(map(lambda x: x ** 3, nums))
even_numbers = list(filter(lambda x: x % 2 == 0, nums))

print(nums)
print(squared_nums)
print(cubed_nums)
print(even_numbers)