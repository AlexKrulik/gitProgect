

class restaurant:
    def __init__(self, rest_name, rest_type):
        self.name = rest_name
        self.type = rest_type

    def open_rest(self):
        print(f'{self.name.title()} is open now')

    def descr_rest(self):
        print(f'Restaurant is {self.type.title()} cousin')

restaurant1 = restaurant('1001 Day', 'Uzbek')

restaurant1.open_rest()
restaurant1.descr_rest()
print(restaurant1.name)
restaurant1.name = '1001 Night'
restaurant1.open_rest()

