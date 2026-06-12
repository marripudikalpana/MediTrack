from rest_framework import serializers
from .models import DietPlan

class DietSerializer(serializers.ModelSerializer):

    class Meta:
        model = DietPlan
        fields = '__all__'