# Exercise 1:

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
# def oldest_cat(cat_list):
#     oldest_current_cat = cat_list[0]
#     for cat in cat_list:
#         if cat.age > oldest_current_cat.age:
#             oldest_current_cat = cat
#     return cat



# c1 = Cat('sparky', 23)
# c2 = Cat('bob', 23)
# c3 = Cat('tom', 25)

# all_cats = [c1, c2, c3]
# oldest = oldest_cat(all_cats)
# print(f'the oldest cat is {oldest.name} and is {oldest.age}')


# Exercise 2:

# class Dog:
#     def __init__(self, name, height):
#         self.name = name 
#         self.height = height
#     def bark(self):
#         print(f'{self.name} goes woof')
#     def jump(self):
#         print(f'{self.name} jumps {self.height*2}cm high!')

#     def biggest_dog(dog_list):
#         biggest_current_dog = all_dogs[0]
#         for dog in dog_list:
#             if dog.height > biggest_current_dog.height:
#                 biggest_current_dog = dog
#         return dog
    


# davids_dog = Dog('Rex', 50)
# sarahs_dog = Dog('Teacup', 20)


# print(f'the dog is called {davids_dog.name} and he is {davids_dog.height} cm')
# davids_dog.bark()
# davids_dog.jump()
# print(f'the dog is called {sarahs_dog.name} and he is {sarahs_dog.height} cm')
# sarahs_dog.bark()
# sarahs_dog.jump()

# all_dogs = [davids_dog, sarahs_dog]
# biggest = biggest_dog(all_dogs)

# print(f'{biggest.dog} is the biggest')


#Exercise 3

# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)


# stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()



# Exercise 4

# class Zoo:
#     def __init__(self, zoo_name):
#         self.zoo_name = zoo_name
#         self.animals = []
#     def add_animal(self, new_animal):
        
#         animals = ['Ape', 'Baboon', 'Cat','cougar', 'Emu']
#         for animal in animals:
            
#             if animals != self.new_animal:
#                 animals.append(new_animal)
#                 print(animals)
#     def get_animals(self, animals):
#         print(f'{self.animals}')
#     def sell_animal(self, animal_sold):
#         for animal in animals:
#             if animal == animal_sold:
#                 animals.remove(animal)
#     def sort_animals(self):
#         my_dict = {}
#         self.sort_animals = sorted(animals)
       
    
        
        

# new_animal = ('Eel')
# animals = Zoo(['Ape', 'Baboon', 'Cat','cougar', 'Emu'])







    