from rest_framework import viewsets
from .models import Exam
from .serializers import ExamSerializer


# Create your views here.
class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
