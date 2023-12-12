from rest_framework import viewsets, filters
from .serializers import *
from .permissions import IsInGroupS, IsInGroupPL
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['last_name']
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    search_fields = ['last_name']
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class SekretarkaViewSet(viewsets.ModelViewSet):
    queryset = Sekretarka.objects.all()
    serializer_class = SekretarkaSerializer
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
class LekarzViewSet(viewsets.ModelViewSet):
    queryset = Lekarz.objects.all()
    serializer_class = LekarzSerializer
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class PielegniarkaViewSet(viewsets.ModelViewSet):
    queryset = Pielegniarka.objects.all()
    serializer_class = PielegniarkaSerializer
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class SpecjalizacjeViewSet(viewsets.ModelViewSet):
    queryset = Specjalizacje.objects.all()
    serializer_class = SpecjalizacjeSerializer
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class StatusWizytyViewSet(viewsets.ModelViewSet):
    queryset = StatusWizyty.objects.all()
    serializer_class = StatusWizytySerializer
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsInGroupS | IsAdminUser]
        return [permission() for permission in permission_classes]

class PacjetViewSet(viewsets.ModelViewSet):
    queryset = Pacjet.objects.all()
    serializer_class = PacjetSerializer
    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'update ', 'partial_update']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsInGroupS | IsAdminUser]
        return [permission() for permission in permission_classes]

class WizytaViewSet(viewsets.ModelViewSet):
    queryset = Wizyta.objects.all()
    serializer_class = WizytaSerializer
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsInGroupS | IsAdminUser]
        return [permission() for permission in permission_classes]

class NotatkaWizytyViewSet(viewsets.ModelViewSet):
    queryset = NotatkaWizyty.objects.all()
    serializer_class = NotatkaWizytySerializer
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsInGroupPL | IsAdminUser]
        return [permission() for permission in permission_classes]


class LekViewSet(viewsets.ModelViewSet):
    queryset = Lek.objects.all()
    serializer_class = LekSerializer
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class ReceptaViewSet(viewsets.ModelViewSet):
    queryset = Recepta.objects.all()
    serializer_class = ReceptaSerializer
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsInGroupPL | IsAdminUser]
        return [permission() for permission in permission_classes]
