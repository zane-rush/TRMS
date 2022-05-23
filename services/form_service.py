from repos.form_repo import FormRepo


class FormService:

    def __init__(self, form_repo: FormRepo):
        self.form_repo = form_repo

    def create_form(self, form):
        return self.form_repo.create_form(form)

    def get_form(self, form_id):
        return self.form_repo.get_form(form_id)

    def get_employee_forms(self, employee_id):
        return self.form_repo.get_employee_forms(employee_id)

    def update_form(self, update):
        return self.form_repo.update_form(update)

    def delete_form(self, form_id):
        return self.form_repo.delete_form(form_id)
