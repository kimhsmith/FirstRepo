from oop import Employee


def main():
    # TODO: add stuff here
    emp_1 = Employee('Kim', 'Smith')

    emp_1.fullname = 'Dylan Sutton'

    print(emp_1.email)
    print(emp_1.fullname)

    del emp_1.fullname


if __name__ == '__main__':
    main()
