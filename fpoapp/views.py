from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer
from rest_framework.response import Response
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer
from .permissions import IsFarmer, IsFPO, IsProvider,IsAssistant
from rest_framework.decorators import action


class ServiceRequestViewSet(viewsets.ModelViewSet):

    queryset = ServiceRequest.objects.select_related(
        'farmer',
        'provider',
        'assistant'
    )

    serializer_class = ServiceRequestSerializer
    permission_classes = [IsAuthenticated]
    
    
    
    def create(self, request, *args, **kwargs):

        if request.user.role != 'FARMER':
            return Response(
                {"error": "Only farmers can create service requests."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(farmer=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    @action(
        detail=True,
        methods=['patch'],
        permission_classes=[IsAuthenticated, IsFPO]
    )
    def assign_provider(self, request, pk=None):

        service_request = self.get_object()

        if service_request.status != 'PENDING':
            return Response(
                {"error": "Provider can only be assigned to pending requests."},
                status=status.HTTP_400_BAD_REQUEST
            )

        provider_id = request.data.get("provider")

        service_request.provider_id = provider_id
        service_request.status = 'ASSIGNED'
        service_request.save()

        return Response({"message": "Provider assigned successfully."})
    
    @action(
        detail=True,
        methods=['patch'],
        permission_classes=[IsAuthenticated, IsProvider]
    )
    def assign_assistant(self, request, pk=None):

        service_request = self.get_object()

        if service_request.status not in ['ASSIGNED', 'IN_PROGRESS']:
            return Response(
                {"error": "Assistant can only be assigned after provider is assigned."},
                status=400
            )

        assistant_id = request.data.get("assistant")

        service_request.assistant_id = assistant_id
        service_request.save()

        return Response({"message": "Assistant assigned successfully."})



    @action(
        detail=True,
        methods=['patch'],
        permission_classes=[IsAuthenticated, IsProvider]
    )
    def start(self, request, pk=None):

        service_request = self.get_object()

        if service_request.status != 'ASSIGNED':
            return Response(
                {"error": "Only assigned requests can be started."},
                status=status.HTTP_400_BAD_REQUEST
            )

        service_request.status = 'IN_PROGRESS'
        service_request.save()

        return Response({"message": "Work started."})


    @action(
        detail=True,
        methods=['patch'],
        permission_classes=[IsAuthenticated, IsProvider]
    )
    def complete(self, request, pk=None):

        service_request = self.get_object()

        if service_request.status != 'IN_PROGRESS':
            return Response(
                {"error": "Only in-progress requests can be completed."},
                status=status.HTTP_400_BAD_REQUEST
            )

        service_request.status = 'COMPLETED'
        service_request.save()

        return Response({"message": "Service completed successfully."})


