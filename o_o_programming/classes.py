# chapter 9
def sample():
    pass
class Dog:
    # state
    breed = ''
    age = ''
    name = ''
    color = ''

    # behavior
    # self key word is used to show that functions and variables are belong to class
    def bark(self):
        print('Dog is barking')

    def run(self):
        print(f'{self.name} is running fast....')

# creating the object from the Class(model)
# creating the instances from the class - INSTANTIATIONS
dog1 = Dog()
dog1.name = 'Max'

dog2 = Dog()
dog2.name = 'Jack'

dog3 = Dog()
dog3.name = 'Sam'

print('************ Behavior of dog: dogs are running ************')
dog1.run()
dog2.run()
dog3.run()

