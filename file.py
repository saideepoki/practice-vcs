import pandas as pd

class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id}\t{self.name}\t{self.age}\t{self.salary}"

class Sorter:
    def __init__(self, employees):
        self.employees = employees

    def sort_by_age(self):
        self.employees.sort(key=lambda x: x.age)

    def sort_by_name(self):
        self.employees.sort(key=lambda x: x.name)

    def sort_by_salary(self):
        self.employees.sort(key=lambda x: x.salary)

    def display(self):
        for emp in self.employees:
            print(emp)

if __name__ == "__main__":
    employees_data = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000)
    ]

    employee_sorter = Sorter(employees_data)

    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        employee_sorter.sort_by_age()
    elif choice == 2:
        employee_sorter.sort_by_name()
    elif choice == 3:
        employee_sorter.sort_by_salary()
    else:
        print("Invalid choice. Sorting by default (Employee ID).")

    print("\nSorted Data:")
    print("-" * 40)
    employee_sorter.display()
