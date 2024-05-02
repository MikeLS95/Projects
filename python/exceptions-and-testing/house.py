class House:
    def __init__(self, price):
        self.__price = price

    # Getter
    @property
    def price(self):
        return self.__price
    
    #setter
    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            print('Price must be greater than zero')

    # def display_price(self):
    #     print(f'The price of this house is ${self.__price}')


my_house = House(800000)
# my_house.__price = -2000
# my_house.display_price()
my_house.price = -900000
print(my_house.price)