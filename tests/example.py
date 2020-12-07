import unittest

from CkanMetaTester.project import ProjectExample


class TestExample(unittest.TestCase):

    def test_true(self):
        project_example = ProjectExample()
        self.assertTrue(project_example.example_return())
