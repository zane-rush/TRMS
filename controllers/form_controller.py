from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.form import Form
from repos.form_repo_impl import FormRepoImpl
from services.form_service import FormService

fr = FormRepoImpl()
fs = FormService(fr)


def route(app):
    @app.route("/employees/<employee_id>/forms", methods=["POST"])
    def post_form(employee_id):
        body = request.json

        form = Form(form_id=body["form_id"], date=body["date"], time=body["time"], location=body["location"],
                    description=body["description"], cost=body["cost"], gradeformat=body["gradeformat"],
                    eventtype=body["eventtype"], justify=body["justify"], attachment=body["attachment"],
                    employee_id=employee_id)

        form = fs.create_form(form)

        return form.json()

    @app.route("/employees/<employee_id>/forms", methods=['GET'])
    def get_employee_forms(employee_id):
        return jsonify([form.json() for form in fs.get_employee_forms(employee_id)])

    @app.route("/forms/<form_id>", methods=["GET"])
    def get_form_by_id(form_id):
        try:
            return fs.get_form(form_id).json(), 200
        except ValueError as e:
            return "Not a Valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employees/<employee_id>/forms/<form_id>", methods=["PUT"])
    def put_form(form_id, employee_id):
        try:
            body = request.json

            form = Form(form_id=form_id, date=body["date"], time=body["time"], location=body["location"],
                        description=body["description"], cost=body["cost"], gradeformat=body["gradeformat"],
                        eventtype=body["eventtype"], justify=body["justify"], attachment=body["attachment"],
                        employee_id=employee_id)

            form = fs.update_form(form)

            return form.json()
        except AttributeError as e:
            return "Not a Valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/forms/<form_id>", methods=["DELETE"])
    def delete_form(form_id):
        try:
            fs.delete_form(form_id)
            return '', 204
        except ValueError as e:
            return "Not a Valid ID", 400
        except ResourceNotFound as r:
            return "Not a Valid ID", 404
