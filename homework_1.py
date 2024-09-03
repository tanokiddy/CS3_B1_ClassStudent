from typing import List
from typing import Literal

ROLE_TYPE = Literal["staff", "manager", "director"]

class Staff:
    def __init__(self, staff_id: int, staff_name: str, base_salary: int, role: ROLE_TYPE, salary_rate: int) -> None:
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.base_salary = base_salary
        self.role = role
        self.salary_rate = salary_rate
    def get_gross_salary(self) -> int:
        return self.base_salary * self.salary_rate

class Manager(Staff):
    def __init__(self, staff_id: int, staff_name: str, base_salary: int, role: ROLE_TYPE, salary_rate: int, bonus: int, managed_department: List[str]) -> None:
        super().__init__(staff_id, staff_name, base_salary, role, salary_rate)
        self.bonus = bonus
        self.managed_department = managed_department
    def get_gross_salary(self) -> int:
        return super().get_gross_salary() + self.bonus
    def get_info(self) -> str:
        return f"Managed departments: {', '.join(self.managed_department)}"

class Director(Staff):
    def __init__(self, staff_id: int, staff_name: str, base_salary: int, role: ROLE_TYPE, salary_rate: int, bonus: int, managed_branch: List[str]) -> None:
        super().__init__(staff_id, staff_name, base_salary, role, salary_rate)
        self.bonus = bonus
        self.managed_branch = managed_branch
    def get_gross_salary(self) -> int:
        return super().get_gross_salary() + self.bonus
    def get_info(self) -> str:
        return f"Managed branch: {', '.join(self.managed_branch)}"
    
staff_1 = Staff(1, "Staff 1", 600, "staff", 1)
manager_1 = Manager(1, "Manager 1", 1200, "manager", 1.2, 100, ["human resource", "product"])
director_1 = Director(1, "Director 1", 2000, "director", 2, 500, ["Hanoi", "HCM"])

print(manager_1.get_gross_salary())
print(manager_1.get_info())
print()
print(director_1.get_gross_salary())
print(director_1.get_info())