# 9-1 , 9-4

class restaurant:
    """Exercises 9-1 nad 9-4"""

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def open_restaurant(self):
        print(f'{self.name.title()} is Open Now!!!')

    def describe_restaurant(self):
        print(f'{self.name.title()} is {self.cuisine_type.title()} restaurant.')

    def increment_number_served(self, served: int):
        print(f'Updating number of served customers by {served}')
        if served > 0:
            self.number_served += served
            print(f'Number served of customers is {restaurant1.number_served}')
        else:
            print(f'No updates so far. {restaurant1.number_served} cutomers have been served.')

    def update_number_served(self, number):
        print(f'Updated number of served customers is {number}')
        self.number_served = number


restaurant1 = restaurant('Silk Road', 'uzbek')
restaurant1.open_restaurant()
restaurant1.describe_restaurant()
print(f'Number served of customers is {restaurant1.number_served}')
restaurant1.number_served = 2
print(f'Number served of customers is {restaurant1.number_served}')
print('________________________________________________________________')

restaurant1.increment_number_served(18)

print('________________________________________________________________')
restaurant1.increment_number_served(0)

print('________________________________________________________________')
restaurant1.increment_number_served(20)

print('________________________________________________________________')
restaurant1.update_number_served(10)

