# Session one


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@co.com'

    def fullname(self):
        return "%s %s" % (self.first, self.last)


emp_1 = Employee('ali', 'ALI', 1000)
emp_2 = Employee('gholi', 'GHOLI', 2000)


# print(emp_1.email)

print(emp_2.fullname())  # auto pass emp_2 arg to fullname method.
Employee.fullname(emp_2)  # we must manually pass emp_2 arg to fullname method
