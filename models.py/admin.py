class Admin:
    def __init__(self,AdminName,age):
        self.AdminName = AdminName
        self.age = age
    def display(self):
        print(f'the emp name is {self.AdminName}')