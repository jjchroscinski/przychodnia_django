from rest_framework.permissions import BasePermission

class IsInGroupS(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Sekretarki').exists()

class IsInGroupPL(BasePermission):
    def has_permission(self, request, view):
        grupy = ['Lekarze', 'Pielegniarkai']

        return any(request.user.groups.filter(name=g).exists() for g in grupy)