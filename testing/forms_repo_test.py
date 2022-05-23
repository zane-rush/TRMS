import unittest

from models.form import Form
from repos.form_repo_impl import FormRepoImpl

fr = FormRepoImpl()


class TestFormRepo(unittest.TestCase):

    added_form = Form()

    def test_create_form(self):
        TestFormRepo.added_form = fr.create_form(Form(form_id=0, date="1111-11-11", time=0, location="",
                                                 description="", cost=0, gradeformat="",
                                                 eventtype="", justify="", attachment="",
                                                 employee_id=0))

        self.assertEqual(self.added_form, Form(form_id=0, date="1111-11-11", time=0, location="",
                                                       description="", cost=0, gradeformat="",
                                                       eventtype="", justify="", attachment="",
                                                       employee_id=0))

        self.assertIsNotNone(fr.get_form(self.added_form.form_id))
        print(self.added_form)

    def test_get_form(self):
        form = fr.get_form(0)
        self.assertEqual(form, Form(form_id=0, date="1111-11-11", time=0, location="",
                                                 description="", cost=0, gradeformat="",
                                                 eventtype="", justify="", attachment="",
                                                 employee_id=0))

    def test_update_form(self):
        form = Form(form_id=0, date="2022-04-22", time=6, location="Denver",
                                    description="Extra Training", cost=300, gradeformat="Presentation",
                                    eventtype="Seminar", justify="Left Blank", attachment="File.doc",
                                    employee_id=0)
        form = fr.update_form(form)

        self.assertEqual(form, Form(form_id=0, date="2022-04-22", time=6, location="Denver",
                                    description="Extra Training", cost=300, gradeformat="Presentation",
                                    eventtype="Seminar", justify="Left Blank", attachment="File.doc",
                                    employee_id=0))
        print(self.added_form)

    def test_delete_form(self):
        TestFormRepo.added_form = fr.create_form(Form(form_id=3, date="2022-04-22", time=3, location="Denver",
                                                      description="Extra Training", cost=300, gradeformat="Presentation",
                                                      eventtype="Seminar", justify="Left Blank", attachment="File.doc",
                                                      employee_id=0))

        form = fr.delete_form(TestFormRepo.added_form.form_id)

        self.assertIsNone(form)

    @classmethod
    def tearDownClass(cls):
        if cls.added_form.form_id:
            fr.delete_form(cls.added_form.form_id)


if __name__ == '__main__':
    unittest.main()