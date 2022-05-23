from abc import ABC, abstractmethod


class FormRepo(ABC):

    @abstractmethod
    def create_form(self, form):
        pass

    @abstractmethod
    def get_form(self, form_id):
        pass

    @abstractmethod
    def get_employee_forms(self, employee_id):
        pass

    @abstractmethod
    def update_form(self, update):
        pass

    @abstractmethod
    def delete_form(self, form_id):
        pass
