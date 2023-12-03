from rest_framework import routers
from django.urls import path, include
from .views import *


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'sekretarki', SekretarkaViewSet)
router.register(r'lekarze', LekarzViewSet)
router.register(r'pielegniarki', PielegniarkaViewSet)
router.register(r'specjalizacja', SpecjalizacjeViewSet)
router.register(r'status', StatusWizytyViewSet)
router.register(r'pacjent', PacjetViewSet)
router.register(r'wizyta', WizytaViewSet)
router.register(r'notatka', NotatkaWizytyViewSet)
router.register(r'lek', LekViewSet)
router.register(r'recepta', ReceptaViewSet)
router.register(r'group', GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
]