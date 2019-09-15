# Python Object-Oriented Programming


class Employee:

    # Class variables
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        # These are class attributes
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay


# This implicitly calls __init__()
emp_1 = Employee('Kim', 'Smith', 50000)
emp_2 = Employee('John', 'Smyth', 20000)

print(emp_1 + emp_2)
