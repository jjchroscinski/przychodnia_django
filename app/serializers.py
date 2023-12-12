from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields =['url','username', 'first_name', 'last_name', 'email']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields =['url', 'name']

class SekretarkaSerializer(serializers.HyperlinkedModelSerializer):
    user=UserSerializer()
    class Meta:
        model = Sekretarka
        fields = '__all__'
        read_only_fields = ['user']

class SpecjalizacjeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Specjalizacje
        fields = '__all__'

class LekarzSerializer(serializers.HyperlinkedModelSerializer):
    imie=serializers.CharField(source='user.first_name')
    nazwisko=serializers.CharField(source='user.last_name')
    email=serializers.CharField(source='user.email')
    specjalizacja=serializers.CharField(source='specjalizacja.nazwa')

    class Meta:
        model = Lekarz
        fields = '__all__'

class PielegniarkaSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Pielegniarka
        fields = '__all__'
        read_only_fields = ['user']


class StatusWizytySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StatusWizyty
        fields = '__all__'

class PacjetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pacjet
        fields = '__all__'


class WizytaSerializer(serializers.HyperlinkedModelSerializer):
    status=serializers.CharField(source='status.nazwa')

    class Meta:
        model = Wizyta
        fields= ['id',
                 'pacjent',
                 'cel_wizyty',
                 'lekarz',
                 'pielegniarka',
                 'data',
                 'status',
                 'opis_wizyty',
                 'recepta'
                 ]

class NotatkaWizytySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NotatkaWizyty
        fields = '__all__'


class LekSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lek
        fields = '__all__'

class ReceptaSerializer(serializers.HyperlinkedModelSerializer):
    leki=serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='nazwa'
    )

    class Meta:
        model = Recepta
        fields = ['id',
                  'wizyta',
                  'leki'
                  ]
