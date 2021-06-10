import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class NumberValidator(object):
    def __init__(self, min_digits=0):
        self.min_digits = min_digits

    def validate(self, password, user=None):
        if not len(re.findall('\d', password)) >= self.min_digits:
            raise ValidationError(
                _('The password must contain at least'
                    f'{self.min_digits} digit(s), 0-9.'),
                code='password_no_number',
                params={'min_digits': self.min_digits},
            )


class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _('The password must contain at least'
                    '1 uppercase letter, A-Z.'),
                code='password_no_upper',
            )


class LowercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _('The password must contain at least'
                    '1 lowercase letter, a-z.'),
                code='password_no_lower',
            )


class SymbolValidator(object):
    def validate(self, password, user=None):
        if re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _('The password must not contain these characters: ' +
                  '()[]{}|\`~!@#$%^&*_-+=;:\'\",<>./?'),
                code='password_no_symbol',
            )
