from repos.employee_repo import EmployeeRepo
from exceptions.resource_not_found import ResourceNotFound


class EmployeeService:

    def __init__(self, employee_repo: EmployeeRepo):
        self.employee_repo = employee_repo

    def create_employee(self, employee):
        return self.employee_repo.create_employee(employee)

    def get_employee(self, employee_id):
        return self.employee_repo.get_employee(employee_id)

    def get_all_employees(self):
        return self.employee_repo.get_all_employees()

    def update_employee(self, update):
        return self.employee_repo.update_employee(update)

    def delete_employee(self, employee_id):
        return self.employee_repo.delete_employee(employee_id)

    def calculate_reimburse(self, availreimburse, pending, awarded, employee_id):
        availreimburse = (availreimburse - pending - awarded)
        if availreimburse >= 0:
            return self.employee_repo.calculate_reimburse(availreimburse, employee_id)
        else:
            raise ResourceNotFound

