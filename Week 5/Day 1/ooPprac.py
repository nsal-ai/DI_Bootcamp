# class Dog():
#     # Initializer / Instance Attributes
#     def __init__(self, name_of_the_dog):
#         print("A new dog has been initialized !")
#         print("His name is", name_of_the_dog)
#         self.name = name_of_the_dog

#     def bark(self):
#         print("{} barks ! WAF".format(self.name))

#     def walk(self, number_of_meters):
#         self.number_of_meters = number_of_meters
#         print("{} walked {} meters".format(self.name, self.number_of_meters))

#     def rename(self, new_name):
#         self.name = new_name

# shelter_dog = Dog("Rex")
# shelter_dog.rename("Paul")
# shelter_dog.bark()
# shelter_dog.walk(10)

# class Computer():

#     def description(self, name):
#         """
#         This is a totally useless function
#         """
#         print("I am a computer, my name is", name)
#         #Analyse the line below
#         print(self)

# mac_computer = Computer()
# mac_computer.brand = "Apple"
# print(mac_computer.brand)

# dell_computer = Computer()

# Computer.description(dell_computer, "Mark")
# # IS THE SAME AS:
# dell_computer.description("Mark")


# l = [{'a': 0}, {'b': 1}, {'c': 2}, {'d': 3}, {'e': 4, 'a': 4}]


# # Method 1: Dictionary Comprehension
# d = {k:v for x in l for k,v in x.items()}
# print(d)
# # {'a': 4, 'b': 1, 'c': 2, 'd': 3, 'e': 4}


# # Method 2: Simple Nested Loop
# d = {}
# for dictionary in l:
#     for k, v in dictionary.items():
#         d[k] = v

# print(d)
# {'a': 4, 'b': 1, 'c': 2, 'd': 3, 'e': 4}


# # Method 3: Update Function
# d = {}
# for dictionary in l:
#     d.update(dictionary)

# print(d)
# # {'a': 4, 'b': 1, 'c': 2, 'd': 3, 'e': 4}


# # Method 4: Dictionary Unpacking
# d = {**l[0], **l[1], **l[2], **l[3], **l[4]}
# print(d)
# # {'a': 4, 'b': 1, 'c': 2, 'd': 3, 'e': 4}


class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)

my_account = BankAccount('12435252', 1000)
my_account.view_balance()


class Animal():
    def __init__(self,name):
        self.name = name
class Dog(Animal):
    has_legs = True
    def bark(self):
        print('{} barked, WAF !'.format(self.name))

a1 = Animal('sparky')
d1 = Dog('X')
print(isinstance(d1, Animal))
print(d1.has_legs)

