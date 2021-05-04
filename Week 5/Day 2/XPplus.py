class Family():
    def __init__(self, name, age, gender, is_child = True):
        self.members = []
        self.last_name = ''
        self.name = name
        self.age = age
        self.gender = gender
        self.is_child = is_child

    def born(self, **kwargs):
        #super().__(name, age, gender)
        #for value in person_dict.values():
            if self.is_child:
                self.members.append(person)
                print(f'congatulations to the family')


members = [
     {'name':'Michael','age':35,'gender':'Male','is_child':False},
     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]

person_dict = {
    'name': 'Jorge',
    'age': 2,
    'gender': 'Male',
    'is_child': True 
    }

person = Family('oscar', 2, 'Male')
person.born()






