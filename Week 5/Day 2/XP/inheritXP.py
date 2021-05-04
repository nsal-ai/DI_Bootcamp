# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Sheeba(Cat):
#     def sing(self,sounds):
#         return f'{sounds}'

# my_cats = []

# my_cats.append(Cat('Bengal', 2))
# my_cats.append(Cat('Chartreux', 3))
# my_cats.append(Cat('Sheeba', 5))

# group_cats = Pets(my_cats)
# group_cats.walk()

# Exercise 2

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age 
        self.weight = weight
    
    def bark(self):
        print(f'{self.name} is barking')

    def run_speed(self):
        return self.weight/(self.age)*10


    def fight(self, other_dog):
        
        #self.other_dog = other_dog
        run_speed = self.run_speed()

        if run_speed * self.weight > other_dog.run_speed()*other_dog.weight:
            print(f'{self.name} is the WINNER!')
        else:
            print(f'{other_dog.name} is the WINNER')

       



Dog1 = Dog('Lassy', 5, 25)
Dog2 = Dog('Kanine', 7, 28)
Dog3 = Dog('Hulk', 6, 35)
Dog1.bark()
print(Dog1.run_speed())
print(Dog1.run_speed()*Dog1.weight)
other_dog = Dog('Rocky', 3, 20)
other_dog.bark()
other_dog.fight(Dog3)














