from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer


class ServiceRequestViewSet(viewsets.ModelViewSet):

    queryset = ServiceRequest.objects.select_related(
        'farmer',
        'provider',
        'assistant'
    )

    serializer_class = ServiceRequestSerializer
    permission_classes = [IsAuthenticated]
