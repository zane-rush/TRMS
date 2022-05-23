
class Form:

    def __init__(self, form_id=0, date="0001-01-01", time=0, location="", description="", cost=0, gradeformat="",
                 eventtype="", justify="", attachment="", employee_id=0):
        self.form_id = form_id
        self.date = date
        self.time = time
        self.location = location
        self.description = description
        self.cost = cost
        self.gradeformat = gradeformat
        self.eventtype = eventtype
        self.justify = justify
        self.attachment = attachment
        self.employee_id = employee_id

    def __repr__(self):
        return str({
            'form_id': self.form_id,
            'date': self.date,
            'time': self.time,
            'location': self.location,
            'description': self.description,
            'cost': self.cost,
            'gradeformat': self.gradeformat,
            'eventtype': self.eventtype,
            'justify': self.justify,
            'attachment': self.attachment,
            'employee_id': self.employee_id,
        })

    def json(self):
        return {
            'form_id': self.form_id,
            'date': self.date,
            'time': self.time,
            'location': self.location,
            'description': self.description,
            'cost': self.cost,
            'gradeformat': self.gradeformat,
            'eventtype': self.eventtype,
            'justify': self.justify,
            'attachment': self.attachment,
            'employee_id': self.employee_id,
        }

    def __eq__(self, other):
        if not other:
            return False
        if not isinstance(other, Form):
            return False

        return self.__dict__ == other.__dict__
