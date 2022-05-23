import psycopg2.errors

from exceptions.resource_not_found import ResourceNotFound
from models.form import Form
from repos.form_repo import FormRepo
from util.db_connection import connection


def _build_form(record):
    if record:
        return Form(form_id=record[0], date=record[1], time=record[2], location=record[3], description=record[4],
                    cost=record[5], gradeformat=record[6], eventtype=record[7], justify=record[8], attachment=record[9],
                    employee_id=record[10])
    else:
        return None


class FormRepoImpl(FormRepo):

    def create_form(self, form):
        sql = "INSERT INTO forms VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [form.form_id, form.date, form.time, form.location, form.description, form.cost,
                             form.gradeformat, form.eventtype, form.justify, form.attachment, form.employee_id])

        connection.commit()
        record = cursor.fetchone()

        return _build_form(record)

    def get_form(self, form_id):
        sql = "SELECT * FROM forms WHERE f_id = %s"
        cursor = connection.cursor()

        cursor.execute(sql, [form_id])

        record = cursor.fetchone()

        if record:
            return _build_form(record)
        else:
            raise ResourceNotFound(f"Form with id: {form_id} - Not Found")

    def get_employee_forms(self, employee_id):
        sql = "SELECT * FROM forms WHERE employee_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])

        records = cursor.fetchall()

        if records:
            return [_build_form(record) for record in records]
        else:
            raise ResourceNotFound(f"Resource not found")

    def update_form(self, update):
        sql = "UPDATE forms SET f_date=%s, f_time=%s, location=%s, description=%s, cost=%s, gradeformat=%s, " \
              "eventtype=%s, justify=%s, attachment=%s, employee_id=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [update.date, update.time, update.location, update.description, update.cost,
                       update.gradeformat, update.eventtype, update.justify, update.attachment, update.employee_id])

        connection.commit()
        record = cursor.fetchone()

        return _build_form(record)

    def delete_form(self, form_id):
        sql = "DELETE FROM forms WHERE f_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [form_id])
        connection.commit()
