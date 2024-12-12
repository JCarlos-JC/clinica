# nurses/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NurseViewSet

router = DefaultRouter()
router.register(r'', NurseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
