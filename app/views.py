from rest_framework import viewsets, filters
from .serializers import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated , AllowAny


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['last_name']
    permission_classes = [IsAdminUser]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    search_fields = ['last_name']
    permission_classes = [IsAdminUser]

class SekretarkaViewSet(viewsets.ModelViewSet):
    queryset = Sekretarka.objects.all()
    serializer_class = SekretarkaSerializer
    permission_classes = [IsAuthenticated]



class LekarzViewSet(viewsets.ModelViewSet):
    queryset = Lekarz.objects.all()
    serializer_class = LekarzSerializer
    permission_classes = [IsAuthenticated]

class PielegniarkaViewSet(viewsets.ModelViewSet):
    queryset = Pielegniarka.objects.all()
    serializer_class = PielegniarkaSerializer
    permission_classes = [IsAuthenticated]

class SpecjalizacjeViewSet(viewsets.ModelViewSet):
    queryset = Specjalizacje.objects.all()
    serializer_class = SpecjalizacjeSerializer
    permission_classes = [AllowAny]

class StatusWizytyViewSet(viewsets.ModelViewSet):
    queryset = StatusWizyty.objects.all()
    serializer_class = StatusWizytySerializer
    permission_classes = [IsAuthenticated]

class PacjetViewSet(viewsets.ModelViewSet):
    queryset = Pacjet.objects.all()
    serializer_class = PacjetSerializer
    permission_classes = [IsAuthenticated]

class WizytaViewSet(viewsets.ModelViewSet):
    queryset = Wizyta.objects.all()
    serializer_class = WizytaSerializer
    permission_classes = [IsAuthenticated]

class NotatkaWizytyViewSet(viewsets.ModelViewSet):
    queryset = NotatkaWizyty.objects.all()
    serializer_class = NotatkaWizytySerializer
    permission_classes = [IsAuthenticated]


class LekViewSet(viewsets.ModelViewSet):
    queryset = Lek.objects.all()
    serializer_class = LekSerializer
    permission_classes = [AllowAny]


class ReceptaViewSet(viewsets.ModelViewSet):
    queryset = Recepta.objects.all()
    serializer_class = ReceptaSerializer
    permission_classes = [IsAuthenticated]
