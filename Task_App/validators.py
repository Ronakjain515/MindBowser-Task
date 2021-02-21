import re
from django.core.exceptions import ValidationError

# this contain letters without space
def Namevalidator(value):
    
    if not value.isalpha():
        raise ValidationError("This field can only contain letters without space")

    return value


def PasswordValidator(value):

    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pat = re.compile(reg)

    if re.search(pat, value):
        return value
    else:
        raise ValidationError("Should have at least one number. Should have at least one uppercase and one lowercase character. Should have at least one special symbol. Should be between 6 to 20 characters long.")


def MobileNoValidator(value):

    if value.isdigit() and len(value) == 10:
        return value
    raise ValidationError("This field can contain only 10 digits")