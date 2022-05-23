import unittest

import exceptions
from exceptions.resource_not_found import ResourceNotFound
from models.employee import Employee
from repos.employee_repo_impl import EmployeeRepoImpl

er = EmployeeRepoImpl()


class TestEmployeeRepo(unittest.TestCase):

    added_employee = Employee()

    def test_create_employee_success(self):
        TestEmployeeRepo.added_employee = er.create_employee(self.added_employee)

        self.assertEqual(self.added_employee, Employee(email="", employeerole="",
                                                       employee_id=self.added_employee.employee_id,
                                                       availreimburse=1000))

        self.assertIsNotNone(er.get_employee(self.added_employee.employee_id))
        print(self.added_employee)

    def test_get_employee_success(self):
        employee = er.get_employee(0)
        self.assertEqual(employee, Employee(email="", employeerole="", employee_id=0,
                                            availreimburse=1000))

    def test_update_employee(self):
        employee = Employee(email="", employeerole="", employee_id=0,
                                                   availreimburse=1000)
        employee = er.update_employee(employee)

        self.assertEqual(employee, Employee(email="", employeerole="", employee_id=0, availreimburse=1000))

        self.assertIsNotNone(er.get_employee(employee_id=0))
        print(self.added_employee)

    def test_calculate_reimburse(self):
        employee = er.create_employee(Employee(email="", employeerole="", employee_id=0,
                                                   availreimburse=1000))
        employee = er.calculate_reimburse(availreimburse=900, employee_id=0)

        self.assertEqual(employee, Employee(email="", employeerole="", employee_id=0, availreimburse=900))
        er.delete_employee(employee_id=0)

    def test_delete_employee(self):
        TestEmployeeRepo.added_employee = er.create_employee(Employee(email="email", employeerole="email",
                                                                      employee_id=3, availreimburse=1000))
        employee = er.delete_employee(TestEmployeeRepo.added_employee.employee_id)

        self.assertIsNone(employee)

    @classmethod
    def tearDownClass(cls):
        if cls.added_employee.employee_id:
            er.delete_employee(cls.added_employee.employee_id)


if __name__ == '__main__':
    unittest.main()
