from django.contrib import admin
from .models import *


@admin.register(Pielegniarka)
class PielegniarkaAdmin(admin.ModelAdmin):
    model=Pielegniarka
    list_filter = ['uprawnienia']

@admin.register(Sekretarka)
class SekretarkaAdmin(admin.ModelAdmin):
    list_display = [
       # 'user__first_name',
        'sekretarka',
        'telefon'
    ]
    def sekretarka(self, obj):
        return obj

@admin.register(Lekarz)
class LekarzAdmin(admin.ModelAdmin):
    list_display = [
        'lekarz',
        'telefon',
        'spec'
    ]
  #search_fields = [
  #    'lekarz__specjalizacja',
  #]

  #list_filter = ['telefon']
    def spec(self, obj):
        return obj.specjalizacja.nazwa

    def lekarz(self, obj):
        return obj

@admin.register(Pacjet)
class PacjetAdmin(admin.ModelAdmin):
    list_display = [
        'imie',
        'nazwisko',
        'pesel',
        'telefon'
    ]
    search_fields = [
        'imie',
        'nazwisko',
    ]


@admin.register(StatusWizyty)
class StatusWizytyAdmin(admin.ModelAdmin):
    pass

@admin.register(Specjalizacje)
class SpecjalizacjeAdmin(admin.ModelAdmin):
    pass

@admin.register(Lek)
class LekAdmin(admin.ModelAdmin):
    pass



class NotatkaWizytyInLine(admin.TabularInline):
    model = NotatkaWizyty

class ReceptaInLine(admin.StackedInline):
    model = Recepta

@admin.register(Wizyta)
class WizytaAdmin(admin.ModelAdmin):
    list_display = [
        'pacjent',
        'lekarz',
        'pielegniarka',
        'status'
    ]
    inlines = [
        NotatkaWizytyInLine,
        ReceptaInLine]
    search_fields = [
        'pacjent__last_name',
        'lekarz__last_name',
        'pielegniarka__last_name',
    ]
    list_filter=[
        'status__nazwa',
        'lekarz__specjalizacja'
    ]



admin.site.register(NotatkaWizyty)
admin.site.register(Recepta)
