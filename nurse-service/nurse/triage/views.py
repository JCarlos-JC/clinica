# triagem/views.py
from rest_framework import viewsets
from .models import Screening
from .serializers import ScreeningSerializer

class ScreeningViewSet(viewsets.ModelViewSet):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer
