from controllers import employee_controller, form_controller
# Controls other controllers


def route(app):
    employee_controller.route(app)
    form_controller.route(app)
