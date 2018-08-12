class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first +'.'+last+'.@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Jhon', 'Smith')
emp1.first = '_jim_'

print(emp1.frist)
print(emp1.email)
print(emp1.fullname())
