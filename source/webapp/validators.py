from django.core.validators import BaseValidator

from django.utils.deconstruct import deconstructible


@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
    code = 'too_short'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)


@deconstructible
class MaxLengthValidator(BaseValidator):
    message = 'Ensure this value has at most %(limit_value)d character (it has %(show_value)d).'
    code = 'max_length'

    def compare(self, a, b):
        return a > b

    def clean(self, x):
        return len(x)