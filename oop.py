# Python Object-Oriented Programming


class Employee:

    # Class variables
    raise_amt = 1.04

    def __init__(self, first, last):
        # These are class attributes
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None


""" 
# This implicitly calls __init__()
emp_1 = Employee('Kim', 'Smith')

emp_1.fullname = 'Dylan Sutton'

print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
 """
