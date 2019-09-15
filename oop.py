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


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


# This implicitly calls __init__()
dev_1 = Developer('Kim', 'Smith', 50000, 'Python')
dev_2 = Developer('John', 'Smyth', 20000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(issubclass(Developer, Manager))
