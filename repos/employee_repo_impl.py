import psycopg2.errors

from exceptions.resource_not_found import ResourceNotFound
from models.employee import Employee
from repos.employee_repo import EmployeeRepo
from util.db_connection import connection


def _build_employee(record):
    if record:
        return Employee(email=record[2], employeerole=record[1], employee_id=record[0], availreimburse=record[3])
    else:
        return None


class EmployeeRepoImpl(EmployeeRepo):

    def create_employee(self, employee):
        sql = "INSERT INTO employees VALUES (%s, %s, %s, %s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [employee.employee_id, employee.employeerole, employee.email, employee.availreimburse])

        connection.commit()
        record = cursor.fetchone()

        return _build_employee(record)

    def get_employee(self, employee_id):
        sql = "SELECT * FROM employees WHERE e_id = %s"
        cursor = connection.cursor()

        cursor.execute(sql, [employee_id])

        record = cursor.fetchone()

        if record:
            return _build_employee(record)
        else:
            raise ResourceNotFound(f"Employee with id: {employee_id} - Not Found")

    def get_all_employees(self):
        sql = "SELECT * FROM employees"
        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        employee_list = [_build_employee(record) for record in records]

        return employee_list

    def update_employee(self, update):
        sql = "UPDATE employees SET email=%s, employeerole=%s, availreimburse=%s WHERE e_id = %s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [update.email, update.employeerole, update.availreimburse, update.employee_id])

        connection.commit()
        record = cursor.fetchone()

        return _build_employee(record)

    def delete_employee(self, employee_id):
        sql = "DELETE FROM employees WHERE e_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])

        connection.commit()

    def calculate_reimburse(self, availreimburse, employee_id):
        sql = "UPDATE employees SET availreimburse = %s WHERE e_id = %s RETURNING *"

        cursor = connection.cursor()

        cursor.execute(sql, [availreimburse, employee_id])
        connection.commit()

        record = cursor.fetchone()

        return _build_employee(record)
