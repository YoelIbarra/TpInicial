import re


class Validator():

    @staticmethod
    def empty_field_validation(field):
        return not len(field.strip())

    @staticmethod
    def has_numbers_validation(field):
        return bool(re.match(re.compile("^[a-zA-Z]+$"), field))
