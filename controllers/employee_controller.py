from flask import request, jsonify


from exceptions.resource_not_found import ResourceNotFound
from models.employee import Employee
from repos.employee_repo_impl import EmployeeRepoImpl
from services.employee_service import EmployeeService

er = EmployeeRepoImpl()
es = EmployeeService(er)


def route(app):
    @app.route("/employees", methods=["POST"])
    def post_employee():
        body = request.json

        employee = Employee(email=body["email"], employeerole=body['employeerole'], employee_id=body["employee_id"],
                            availreimburse=body["availreimburse"])

        employee = es.create_employee(employee)

        return employee.json()

    @app.route("/employees", methods=["GET"])
    def get_all_employees():
        return jsonify([employee.json() for employee in es.get_all_employees()])

    @app.route("/employees/<employee_id>", methods=["GET"])
    def get_employee_by_id(employee_id):
        try:
            return es.get_employee(int(employee_id)).json(), 200
        except ValueError as e:
            return "Not a Valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employees/<employee_id>", methods=["PUT"])
    def put_employee(employee_id):
        body = request.json

        employee = Employee(email=body["email"], employeerole=body['employeerole'], employee_id=employee_id,
                            availreimburse=body["availreimburse"])

        employee = es.update_employee(employee)

        try:
            return employee.json()
        except AttributeError as e:
            return "Not a Valid ID", 404
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employees/<employee_id>", methods=["DELETE"])
    def del_employee(employee_id):
        try:
            es.get_employee(employee_id)
            es.delete_employee(employee_id)
            return '', 204
        except ValueError as e:
            return "Not a Valid ID", 404
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employees/<employee_id>", methods=["GET", "PATCH"])
    def calculate_reimbursement(employee_id):
        body = request.json

        try:
            employee = es.get_employee(employee_id)
            employee.availreimburse = es.calculate_reimburse(availreimburse=body["availreimburse"],
                                                             pending=body["pending_reimburse"],
                                                             awarded=body["awarded_reimburse"],
                                                             employee_id=employee_id)
            employee = es.get_employee(employee_id)

            return employee.json()
        except ResourceNotFound as r:
            return r.message, 404


