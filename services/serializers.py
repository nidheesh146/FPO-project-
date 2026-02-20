from rest_framework import serializers
from fpoapp.models import ServiceRequest


class ServiceRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceRequest
        fields = '__all__'
        read_only_fields = ['farmer', 'status', 'created_at']
