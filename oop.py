# Python Object-Oriented Programming


import datetime


class Employee:

    # Class variables
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        # These are class attributes
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # Better to call Employee rather than self since this change shouldn't change for each instance
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # This is basically an alternative constructor.
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# This implicitly calls __init__()
emp_1 = Employee('Kim', 'Smith', 50000)
emp_2 = Employee('John', 'Smyth', 20000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = 'Dylan-Sutton-30000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)

my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))
