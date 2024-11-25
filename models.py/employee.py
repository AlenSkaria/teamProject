class Employee:
    def __init__(self,employeeName,age):
        self.employeeName = employeeName
        self.age = age
    def display(self):
        print(f'the emp name is {self.employeeName}')