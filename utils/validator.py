import re


class Validator():

    @staticmethod
    def empty_field_validation(field, label):
        if not len(field.strip()):
            label['text'] = 'No puede estar vacío'
        return bool(len(field.strip()))

    @staticmethod
    def has_numbers_validation(field, label):
        if not bool(re.match(re.compile("^[a-zA-Z]+$"), field)):
            label['text'] = 'No puede ingresar números'
        return bool(re.match(re.compile("^[a-zA-Z]+$"), field))
