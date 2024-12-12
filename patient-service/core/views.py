from django.shortcuts import render
from .models import Patient
from .serializers import PatientSerializer
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
     queryset = Patient.objects.all()
     serializer_class = PatientSerializer

@api_view(['GET'])
def get_patient(request, nid):
    try:
        # Buscar paciente com base no 'nid'
        patient = Patient.objects.get(nid=nid)
        return Response({
            'nid': patient.nid,
            'nome': patient.nome
        })
    except Patient.DoesNotExist:
        return Response({'error': 'Paciente não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    try:
        patient = Patient.objects.get(nid=nid)
        return JsonResponse({
            'nid': patient.nid,
            'nome': patient.nome,
        })
    except Patient.DoesNotExist:
        return JsonResponse({'error': 'Paciente não encontrado'}, status=404)