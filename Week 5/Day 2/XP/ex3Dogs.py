from inheritXP import Dog



# import sys
# sys.path.append('c:/Users/Nigel/desktop/DI_Bootcamp/Week 5/Day 2/inheritXP.py')


class PetDog(Dog):
    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        

    def train(self):
        print(self.bark())
        #return trained == True
    def play(self, *args):
        for args in dog_names:
            print(args, end=' '),
            print('all play together')
            
    def do_a_trick(self, dog_names):
        
        trick_list = [
            '{dog_name} does a barrel roll',
            '{dog_name} stands on his back legs',
            '{dog_name} shakes your hand',
            '{dog_name} plays dead'
        ]
        for dog_name in dog_names:
            print(random.choice(trick_list))


dog_names = ['rex', 'felix', 'Bamba']

Doggi = PetDog('Rufio', 3, 20)
Doggi.train()
Doggi.play()
Doggi.do_a_trick(dog_names)





