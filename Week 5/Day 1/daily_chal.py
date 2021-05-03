class Farm:
    def __init__(self, name, animals):
        print('a new farm has been initialized!')
        print(f'the name of the farm is, {name} farm')
        self.name = name
        self.animals = {}
        
        
    def add_animal(self, animal, amount):
        self.amount = amount
        animals = {'cow':1, 'sheep':1, 'goat':1}
        
        if animal in animals:
            animals[animal] += self.amount
            self.animals.update(animals, amount)
        print(animals)
        #else:
            #animals.update(animal)
        #print(animals)
        
        for key, value in animals.items():
            print(key, ' : ', value)
    def get_info(self):        





macdonald = Farm('McDonald')
macdonald.add_animal('cow', 6)
macdonald.add_animal('sheep', 5)
macdonald.add_animal('goat', 12)


print(macdonald.get_info())



    
    
    


