# chapter 9
def sample():
    pass


class Dog:
    def __init__(self, breed, age, name, color):
        # state
        self.breed = breed
        self.age = age
        self.name = name
        self.color = color

    # behavior
    # self key word is used to show that functions and variables are belong to class
    def bark(self):
        print('Dog is barking')

    def run(self):
        print(f'dog named {self.name} is running fast and he is {self.age} years old and he is {self.color} color....')


# creating the object from the Class(model)
# creating the instances from the class - INSTANTIATIONS


dog3 = Dog('Gray', 10, 'Sam', 'Gray')

print('************ Behavior of a dog ************')

dog3.run()


