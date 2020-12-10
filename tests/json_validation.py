import unittest
from MetadataTesting.json_validation import ValidateNetkanJson


class TestNetkanValidation(unittest.TestCase):

    def test_validate_netkan(self):
        self.assertTrue(ValidateNetkanJson().validate_schema())
