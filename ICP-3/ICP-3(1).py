class Employee:
    num_employees = 0  # Class variable to count employees

    def __init__(self, name, family, salary, department):
        """Initializes an employee's attributes."""
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.num_employees += 1  # Increment employee count

    def average_salary(self, other_employees):
        total_salaries = self.salary
        for employee in other_employees:
            total_salaries += employee.salary
        return total_salaries / (len(other_employees) + 1)

class FulltimeEmployee(Employee): # Represents a full-time employee.

    def __init__(self, name, family, salary, department, benefits):
        """Initializes a full-time employee's attributes."""
        super().__init__(name, family, salary, department)
        self.benefits = benefits


# Create instances of Employee and FulltimeEmployee
employee1 = Employee("Manasa", "Dhompa", 50000, "Engineering")

employee2 = FulltimeEmployee("Ravi","Akula", 60000, "Sales", ["Health insurance", "Paid leave"])

print("Employee name: {}|Employee Family: {}|Employee Salary: {}|Employee department: {}".format(employee1.name,employee1.family,employee1.salary, employee1.department))  # Output: Alice Engineering
print("Employee name: {}|Employee Family: {}|Employee Salary: {}|Employee department: {}|Employee Benefits: {}".format(employee2.name,employee2.family,employee2.salary, employee2.department, employee2.benefits))  # Output: Alice Engineering

average_salary = employee1.average_salary([employee2])
print("Average salary:", average_salary) 
print("number of Employees:",employee1.num_employees)