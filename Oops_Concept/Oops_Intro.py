#Explain OOP concepts using one example program

class Employee:
    company_name = "ABC Technologies"   # Class variable

    def __init__(self, name, salary):
        self.name = name               # Instance variable
        self._salary = salary          # Encapsulation (protected)

    def get_salary(self):
        return self._salary

    def calculate_bonus(self):
        return self._salary * 0.10     # Base bonus

    def display(self):
        print(f"Name: {self.name}")
        print(f"Company: {Employee.company_name}")
        print(f"Salary: {self._salary}")


# ---------------- INHERITANCE & METHOD OVERRIDING ----------------
class Manager(Employee):

    def calculate_bonus(self):
        return self._salary * 0.20     # Overridden method


# ---------------- POLYMORPHISM ----------------
def show_bonus(emp):
    print(f"Bonus: {emp.calculate_bonus()}")


# ---------------- OBJECT CREATION ----------------
emp1 = Employee("Ravi", 50000)
mgr1 = Manager("Anita", 80000)

emp1.display()
show_bonus(emp1)

print("-" * 30)

mgr1.display()
show_bonus(mgr1)
