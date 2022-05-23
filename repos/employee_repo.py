from abc import ABC, abstractmethod


class EmployeeRepo(ABC):

    @abstractmethod
    def create_employee(self, employee):
        pass

    @abstractmethod
    def get_employee(self, employee_id):
        pass

    @abstractmethod
    def get_all_employees(self):
        pass

    @abstractmethod
    def update_employee(self, update):
        pass

    @abstractmethod
    def delete_employee(self, employee_id):
        pass

    @abstractmethod
    def calculate_reimburse(self, availreimburse, employee_id):
        pass

