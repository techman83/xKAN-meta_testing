

class ValidateJson:
    """
    Common json validation for CKAN/NetKAN
    """

    def validate_schema(self):
        return True


class ValidateCkanJson(ValidateJson):
    pass


class ValidateNetkanJson(ValidateJson):
    pass
