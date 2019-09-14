# Python Object-Oriented Programming


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


print(Employee.num_of_emps)
emp_1 = Employee('Kim', 'Smith', 50000)
emp_2 = Employee('John', 'Smyth', 20000)
print(Employee.num_of_emps)

print(Employee.__dict__)
print(emp_1.__dict__)
emp_1.raise_amount = 1.05
# raise_amount has been added to emp_1 as an attribute, but only for this instance of Employee
print(emp_1.__dict__)
