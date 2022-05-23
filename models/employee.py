class Employee:

    def __init__(self, email="", employeerole="", employee_id=0, availreimburse=1000):
        self.email = email
        self.employeerole = employeerole
        self.employee_id = employee_id
        self.availreimburse = availreimburse

    def __repr__(self):
        return str({
            'email': self.email,
            'employee_id': self.employee_id,
            'employeerole': self.employeerole,
            'availreimburse': self.availreimburse
        })

    def json(self):
        return {
            'email': self.email,
            'employee_id': self.employee_id,
            'employeerole': self.employeerole,
            'availreimburse': self.availreimburse
        }

    def __eq__(self, other):
        if not other:
            return False

        if not isinstance(other, Employee):
            return False

        return self.__dict__ == other.__dict__
