from datetime import datetime

class EmployeeLibrary:
    def __init__(self):
        self.employees = {}

    def create_new_employee(self, emp_id, name, age, doj):
        self.employees[emp_id] = {
            "Name": name,
            "Age": age,
            "DOJ": doj,
            "CreatedOn": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "IsActive": True
        }

    def list_employees(self):
        return self.employees

    def update_employee(self, emp_id, updated_details):
        if emp_id in self.employees:
            self.employees[emp_id].update(updated_details)

    def delete_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]


hello
    
