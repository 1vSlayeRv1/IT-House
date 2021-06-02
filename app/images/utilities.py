from datetime import datetime
from os.path import splitext
from django.core.exceptions import ValidationError


def get_timestamp_path(instance, filename):
    ext = splitext(filename)[-1]
    if ext in ('.png', '.jpg'):
        return f'{datetime.now().timestamp()}{ext}'
    else:
        raise ValidationError('Image is not .png or .jpg')
