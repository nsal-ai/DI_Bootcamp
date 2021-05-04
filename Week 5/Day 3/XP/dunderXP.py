# abs() returns the absolute value of a number by calling number parameter in parentheses


# class Functions:
#     def __init__(self, number):
#         self.number = number
#         self.abs = abs

#     def __abs__(self):
#         return f'this function prints out {self.number} as an absolute'

#     def __int__(self):
#         return f'this built-in function returns {self.number} as an integer'

#     def __input__(self):
#         return f'this function allows {self.number} as an input'

# result = Functions(3)
# print(abs(result.number))
# print(result.__abs__())
# print(result.__int__())
# print(result.__input__())
# print(__doc__)


# Ex 2 CURRENCIES ==================

class Currency:

    def __init__(self, type_, amount):
        self.type_ = type_
        self.amount = amount

    def __str__(self):
        return f'{self.amount} {self.type_}'

    def __int__(self, other):
        
        new_amount = self.amount + other.amount

        if self.type_ != other.type_:
            print('TypeError:Cannot add between Currency type <dollar> and <shekel>')
        else:
            return f'{new_amount}'
            
        
    def __repr__(self):
        return f'{self.amount} {self.type_}'



c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c4 = Currency('shekel', 1)
c3 = Currency('shekel', 10)
other = Currency('dollar', 0)


print(str(c1))
print(c1.__int__(other))
print(c1.__repr__())
print(c1.amount+5)
print(c1.__int__(c2))
print(c1.__repr__())
c1.amount = int(c1.amount+5)
print(c1.__repr__())

c1.amount += c2.amount
print(c1.__str__())

print(c1.__int__(c3))








