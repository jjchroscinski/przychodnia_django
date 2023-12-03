from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, User
from .models import Sekretarka, Lekarz, Pielegniarka

@receiver(post_save, sender=Sekretarka)
def dodanie_do_sekretarek(sender, instance, created, **kwargs):
    p = Sekretarka.objects.last()
    user=User.objects.get(id=p.user_id)
    group = Group.objects.get(name='Sekretarki')
    group.user_set.add(user)

@receiver(post_save, sender=Lekarz)
def dodanie_do_lekarzy(sender, instance, created, **kwargs):
    p = Lekarz.objects.last()
    user=User.objects.get(id=p.user_id)
    group = Group.objects.get(name='Lekarze')
    group.user_set.add(user)

@receiver(post_save, sender=Pielegniarka)
def dodanie_do_pielegniarek(sender, instance, created, **kwargs):
    p = Pielegniarka.objects.last()
    user=User.objects.get(id=p.user_id)
    group = Group.objects.get(name='Pielegniarkai')
    group.user_set.add(user)

@receiver(post_migrate)
def dodawanie_grup(sender, **kwargs):

    if sender.name == 'app':
        nazwy_grup = ['Sekretarki', 'Lekarze', 'Pielegniarkai']

        for nazwa in nazwy_grup:
            group, created = Group.objects.get_or_create(name=nazwa)

