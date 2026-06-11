from rest_framework import viewsets
from .models import MedicalReport
from .serializers import MedicalReportSerializer

class MedicalReportViewSet(viewsets.ModelViewSet):

    queryset = MedicalReport.objects.all()
    serializer_class = MedicalReportSerializer
