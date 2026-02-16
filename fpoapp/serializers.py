from rest_framework import serializers
from .models import ServiceRequest


class ServiceRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceRequest
        fields = '__all__'
        read_only_fields = ['farmer','status', 'created_at']
        
    def validate_status(self, value):
        if value not in ['PENDING', 'COMPLETED']:
            raise serializers.ValidationError("Invalid status.")
        return value

