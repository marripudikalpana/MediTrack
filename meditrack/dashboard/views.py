from rest_framework.views import APIView
from rest_framework.response import Response

from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment

class DashboardAPIView(APIView):

    def get(self, request):

        data = {

            "total_patients":
            Patient.objects.count(),

            "total_doctors":
            Doctor.objects.count(),

            "total_appointments":
            Appointment.objects.count(),
        }

        return Response(data)
