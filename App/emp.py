from datetime import datetime

class EmployeeLibrary:
    def __init__(self):
        self.employees = {}

    def create_new_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        doj = input("Enter Date of Joining (YYYY-MM-DD): ")
        self.employees[emp_id] = {
            "Name": name,
            "Age": age,
            "DOJ": doj,
            "CreatedOn": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "IsActive": True
        }

    def list_employees(self):
        return self.employees

    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")
        if emp_id in self.employees:
            print("Current Details:", self.employees[emp_id])
            print("Enter new details (leave blank to keep current value):")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            doj = input("Enter Date of Joining (YYYY-MM-DD): ")
            is_active = input("Is Active (True/False): ")

            if name:
                self.employees[emp_id]["Name"] = name
            if age:
                self.employees[emp_id]["Age"] = int(age)
            if doj:
                self.employees[emp_id]["DOJ"] = doj
            if is_active:
                self.employees[emp_id]["IsActive"] = is_active.lower() == "true"
        else:
            print("Employee ID not found.")

    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")
        if emp_id in self.employees:
            del self.employees[emp_id]
            print("Employee deleted.")
        else:
            print("Employee ID not found.")


# Example usage
library = EmployeeLibrary()

while True:
    print("\nEmployee Management System")
    print("1. Create New Employee")
    print("2. List Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        library.create_new_employee()
    elif choice == "2":
        employees = library.list_employees()
        for emp_id, details in employees.items():
            print(f"ID: {emp_id}, Details: {details}")
    elif choice == "3":
        library.update_employee()
    elif choice == "4":
        library.delete_employee()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
