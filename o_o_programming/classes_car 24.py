class car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__odometer_reading = 0 #default value # hidden attribute from object, private

    def get_descriprion(self):
        print(f"Details of the car\n\t\t\tMake/model/year: {self.__make.title()}/{self.__model.upper()}/{self.__year}")


    def get_odometer(self):
        return f'Current milage: {self.__odometer_reading}'

    def set_odometer(self, milage):
        print('Updating odometer reading >>>')
        if milage > self.__odometer_reading:
            self.__odometer_reading = milage
        else:
            print(f'Invalid milage was entered for the odometer! Value entered: {milage}')


    def increment_odometer(self, miles:int):
        print(f'Adding {miles} miles to your odometer reading >>>')
        if miles > 0:
            self.__odometer_reading += miles
        else:
            print(f'Miles can not be negative number. Value entered: {miles} miles.')




car1 = car('BMW', 'X5', '2024')
car1.get_descriprion()
print('_______________________________________________________')

print(car1.get_odometer())
car1.set_odometer(9999)
print(car1.get_odometer())

print('_______________________________________________________')

car1.increment_odometer(-50)
print(car1.get_odometer())

print('_______________________________________________________')

car1.increment_odometer(50)
print(car1.get_odometer())





