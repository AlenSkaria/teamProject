class Employee:
    def __init__(self,name,age,doj,createdOn,isActive):
        self.name = name
        self.age = age
        self.doj = doj
        self.__createdOn=createdOn
        self.isActive=isActive


    def getCO(self):
        return self.__createdOn

    def setCO(self,createdOn):
        self.__createdOn = createdOn

    def display(self):
        print(f'the emp name is {self.employeeName}, {self.age},{self.doj},{self.getCO()},')