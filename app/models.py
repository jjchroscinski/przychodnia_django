from datetime import datetime
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
import uuid

def spr_data(value):
    if value.date() > datetime.date(datetime.today()):
        return value
    else:
        raise ValidationError("Data wizyty nie moze byc starsza od daty utworzenia")

class Sekretarka(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE)
    telefon=models.CharField(
        max_length=14,
        validators=[MinLengthValidator(9)],
        null=False)
    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'

    class Meta:
        verbose_name_plural = "Sekretarki"


class Specjalizacje(models.Model):
    nazwa=models.CharField(
        max_length=100,
        null=False)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name_plural = "Specjalizacje"

class Lekarz(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE)
    specjalizacja=models.ForeignKey(
        Specjalizacje,
        on_delete=models.DO_NOTHING)
    telefon = models.CharField(
        max_length=14,
        validators=[MinLengthValidator(9)],
        null=False)
    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'

    class Meta:
        verbose_name_plural = "Lekarze"

class Pielegniarka(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE)
    UPRAWNIENIA=[
        ('I Stopien', 'I Stopien'),
        ('II Stopien', 'II Stopien')
    ]
    uprawnienia=models.CharField(
        choices=UPRAWNIENIA,
        default='I',
        max_length=15)
    telefon = models.CharField(
        max_length=14,
        validators=[MinLengthValidator(9)],
        null=False)
    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'

    class Meta:
        verbose_name_plural = "Pielegniarki"

class StatusWizyty(models.Model):
    nazwa = models.CharField(
        max_length=100,
        null=False)
    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name_plural = "Statusy wizyt"

class Pacjet(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    pesel = models.CharField(
        unique=True,
        max_length=11,
        null=False)
    imie =  models.CharField(
        max_length=30,
        null=False)
    nazwisko = models.CharField(
        max_length=50,
        null=False)
    telefon = models.CharField(
        max_length=14,
        validators=[MinLengthValidator(9)],
        null=False)
    email = models.CharField(
        null=True,
        max_length=30)
    def __str__(self):
        return f'{self.nazwisko} {self.imie}'

    class Meta:
        verbose_name_plural = "Pacjeci"

class Wizyta(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    pacjent=models.ForeignKey(
        Pacjet,
        on_delete=models.CASCADE,
        null=False)
    cel_wizyty = models.TextField(
        help_text="Opisz w jakim celu pacjent chce przyjsc")
    lekarz=models.ForeignKey(
        Lekarz,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING)
    pielegniarka = models.ForeignKey(
        Pielegniarka,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING)
    data=models.DateTimeField(
        null=False,
        validators=[spr_data])
    status=models.ForeignKey(
        StatusWizyty,
        on_delete=models.DO_NOTHING,
        null=False)
    def __str__(self):
        return f'Wizyta {self.pacjent}'

    class Meta:
        verbose_name_plural = "Wizyty"

class NotatkaWizyty(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    wizyta=models.ForeignKey(
        Wizyta,
        related_name='opis_wizyty',
        on_delete=models.CASCADE,
        null=False)
    opis=models.TextField(
        null=False,
        help_text="Opis wizyty, ustalenia, dalsze kroki")

    def __str__(self):
        return f'Notatka do wizyty pacjenta {self.wizyta.pacjent} z {self.wizyta.data.date()} '

    class Meta:
        verbose_name_plural = "Notatki do wizyt"

class Lek(models.Model):
    nazwa = models.CharField(
        max_length=100,
        null=False)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name_plural = "Leki"
class Recepta(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    wizyta = models.ForeignKey(
        Wizyta,
        related_name='recepta',
        on_delete=models.DO_NOTHING,
        null=False)
    leki=models.ManyToManyField(
        Lek)

    def __str__(self):
        return f'Recepta pacjenta {self.wizyta.pacjent} z {self.wizyta.data.date()}'

    class Meta:
        verbose_name_plural = "Recepty"

