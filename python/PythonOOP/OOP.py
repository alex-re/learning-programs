class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first + '.' + self.last + '@co.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return "%s %s" % (self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)  # employees doesent have raise_amount BUT the inherent from their parrent class

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod  # NOT self AND cls
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # as same as each other
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # if employees is None:
            # self.employees = []
        # else:
            # self.employees = employees
        self.employees = [] if employees is None else employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


emp_1 = Employee('ali', 'ALI', 1000)
emp_2 = Employee('gholi', 'GHOLI', 2000)
# print(Employee.num_of_emps)
# print(emp_1.email)
# print(emp_1.__dict__)
# print(emp_2.fullname())  # auto pass emp_2 arg to fullname method.
# Employee.fullname(emp_2)  # we must manually pass emp_2 arg to fullname method
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# Employee.set_raise_amount(1.05)
# emp_str = Employee.from_string('test-user-3000')
# import datetime
# my_date = datetime.date(2016, 7, 11)
# print(Employee.is_workday(my_date))
# dev_1 = Developer('dev', 'lop', 6000, 'Python')
mgr_1 = Manager('man', 'Smith', 6000, [emp_1])
# mgr_1.print_emps()
# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, Manager))
print(issubclass(Developer, Employee))



