# Functions
def hello(name, age):
    x = 5
    print(f'Hello, {name}! You are {age} years old!')
    
def goodbye():
    global name
    name = 'Barry'
    print(f'Goodbye, {name}!')

# Main   
# goodbye() 
# hello('Mike', 28)
# print(x)

def add_tax(amount, tax_rate=0.1):
    total = amount * (1 + tax_rate)
    return total

subtotal = float(input('Subtotal: $'))
grand_total = add_tax(subtotal)
print(f'Total (inc company tax): $ {grand_total:.2f}')
