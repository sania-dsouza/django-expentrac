# Custom validators for password
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_number(pswd):
    if re.search('[0-9]', pswd) is None:
        raise ValidationError(
            _('Must have at least one number.'),
        )


def validate_specialchar(pswd):
    if re.search('[$&+,:;=?@#|<>.^*()%!]', pswd) is None:
        raise ValidationError(
            _('Must have at least one special character.')
        )

