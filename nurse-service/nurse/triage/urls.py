# triagem/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScreeningViewSet

router = DefaultRouter()
router.register(r'', ScreeningViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
