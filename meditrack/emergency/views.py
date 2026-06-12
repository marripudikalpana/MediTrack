from rest_framework import viewsets

from .models import EmergencyContact
from .serializers import EmergencySerializer

class EmergencyViewSet(viewsets.ModelViewSet):

    queryset = EmergencyContact.objects.all()

    serializer_class = EmergencySerializer