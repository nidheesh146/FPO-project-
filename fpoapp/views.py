from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer
from rest_framework.response import Response
from rest_framework import status



class ServiceRequestViewSet(viewsets.ModelViewSet):

    queryset = ServiceRequest.objects.select_related(
        'farmer',
        'provider',
        'assistant'
    )

    serializer_class = ServiceRequestSerializer
    permission_classes = [IsAuthenticated]
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if 'provider' in request.data:
            instance.provider_id = request.data.get('provider')

        if 'status' in request.data:
            if request.data.get('status') == 'COMPLETED':
                instance.status = 'COMPLETED'

        if 'assistant' in request.data:
            instance.assistant_id = request.data.get('assistant')

        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
