import unittest
from unittest.mock import MagicMock

from models.employee import Employee
from repos.employee_repo_impl import EmployeeRepoImpl
from services.employee_service import EmployeeService


class TestEmployeeService(unittest.TestCase):
    er = EmployeeRepoImpl()
    es = EmployeeService(er)

    def test_calculate_reimburse(self):
        self.er.create_employee(Employee(email="", employeerole="", employee_id=0,
                                         availreimburse=1000))
        calc = self.es.calculate_reimburse(1000, 100, 200, 0)

        self.assertEqual(calc, Employee(email="", employeerole="", availreimburse=700, employee_id=0))
        self.er.delete_employee(employee_id=0)


if __name__ == '__main__':
    unittest.main()
