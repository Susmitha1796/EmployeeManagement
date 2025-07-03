# Employee class definition
class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def calculate_yearly_salary(self):
        return self.salary * 12

    def display_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Monthly Salary: ₹{self.salary}")
        print(f"Yearly Salary: ₹{self.calculate_yearly_salary()}")
        print("-" * 30)

# Manager subclass definition
class Manager(Employee):
    def __init__(self, emp_id, name, department, salary, team_size):
        super().__init__(emp_id, name, department, salary)
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print(f"Team Size: {self.team_size}")
        print("=" * 30)

# Testing / Demo block
if __name__ == "__main__":
    # Create an Employee
    emp1 = Employee("E101", "Susmitha", "HR", 50000)
    emp1.display_details()

    # Create a Manager
    mgr1 = Manager("M201", "Anjali", "Engineering", 80000, 10)
    mgr1.display_details()
