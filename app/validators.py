from datetime import datetime
from django.core.exceptions import ValidationError


def spr_data(value):
    if value.date() > datetime.date(datetime.today()):
        return value
    else:
        raise ValidationError("Data wizyty nie moze byc starsza od daty utworzenia")

def spr_tel(value):
    if value.isdigit():
        return value
    else:
        raise ValidationError("Uzyj samych cyfr")

def spr_mail(value):
    if '@' in value:
        return value
    else:
        raise ValidationError("Zle podany mail")

