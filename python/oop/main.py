import dog

# Ted = dog.create('Ted', 16, 'Border Collie')
# Loki = dog.create('Loki', 4, 'Border Collie')

# dog.walk(Ted)
# dog.walk(Loki)
# dog.walk(Ted)

# print(Ted)
# print(Loki)

dog1 = dog.Dog('Ted') # creates a new instance of Dog
dog2 = dog.Dog('Loki')

# dog1.name = 'Ted' # Create attribute 'name' on dog1 and assign 'Ted' to it.
# dog2.name = 'Loki'

# dog1.greet()
# dog2.greet()

print(dog1.__dict__)
print(dog2.__dict__)