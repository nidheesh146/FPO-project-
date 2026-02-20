from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from fpoapp.models import ServiceRequest
from fpoapp.models import User
from .serializers import ServiceRequestSerializer



class ServiceRequestListCreateView(generics.ListCreateAPIView):
    serializer_class = ServiceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "FARMER":
            return ServiceRequest.objects.filter(farmer=user)

        if user.role == "FPO":
            return ServiceRequest.objects.all()

        if user.role == "PROVIDER":
            return ServiceRequest.objects.filter(provider=user)

        if user.role == "ASSISTANT":
            return ServiceRequest.objects.filter(assistant=user)

        return ServiceRequest.objects.none()

    def perform_create(self, serializer):
        if self.request.user.role != "FARMER":
            raise PermissionDenied("Only farmers can create requests.")
        serializer.save(farmer=self.request.user)



class AssignProviderView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        if request.user.role != "FPO":
            raise PermissionDenied("Only FPO can assign provider.")

        service_request = get_object_or_404(ServiceRequest, pk=pk)

        provider_id = request.data.get("provider_id")
        provider = get_object_or_404(User, id=provider_id, role="PROVIDER")

        service_request.provider = provider
        service_request.status = "ASSIGNED"
        service_request.save()

        return Response({"message": "Provider assigned"})


class RespondRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        if request.user.role != "PROVIDER":
            raise PermissionDenied("Only provider can respond.")

        service_request = get_object_or_404(ServiceRequest, pk=pk)

        if service_request.provider != request.user:
            raise PermissionDenied("Not your request.")

        action = request.data.get("action")

        if action == "accept":
            service_request.status = "IN_PROGRESS"
        elif action == "reject":
            service_request.status = "REJECTED"
        else:
            return Response({"error": "Invalid action"}, status=400)

        service_request.save()
        return Response({"message": f"Request {action}ed successfully"})


class AssignAssistantView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        if request.user.role != "PROVIDER":
            raise PermissionDenied("Only provider can assign assistant.")

        service_request = get_object_or_404(ServiceRequest, pk=pk)

        if service_request.provider != request.user:
            raise PermissionDenied("Not your request.")

        assistant_id = request.data.get("assistant_id")
        assistant = get_object_or_404(User, id=assistant_id, role="ASSISTANT")

        service_request.assistant = assistant
        service_request.save()

        return Response({"message": "Assistant assigned"})



class StartWorkView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        if request.user.role != "ASSISTANT":
            raise PermissionDenied("Only assistant can start work.")

        service_request = get_object_or_404(ServiceRequest, pk=pk)

        if service_request.assistant != request.user:
            raise PermissionDenied("Not your request.")

        service_request.status = "IN_PROGRESS"
        service_request.save()

        return Response({"message": "Work started"})



class CompleteWorkView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        if request.user.role != "ASSISTANT":
            raise PermissionDenied("Only assistant can complete work.")

        service_request = get_object_or_404(ServiceRequest, pk=pk)

        if service_request.assistant != request.user:
            raise PermissionDenied("Not your request.")

        service_request.status = "COMPLETED"
        service_request.save()

        return Response({"message": "Work completed"})
