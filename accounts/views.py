from django.shortcuts import render

# Create your views here.


from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .serializers import RegisterSerializer
from fpoapp.models import User
from fpoapp.models import FPO, ServiceProvider, Assistant


class FarmerRegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(role="FARMER")
        
        
        
class FPORegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(role="FPO")

        FPO.objects.create(
            user=user,
            name=self.request.data.get("name")
        )

        

class CreateProviderView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != "FPO":
            raise PermissionDenied("Only FPO can create provider.")

        user = serializer.save(role="PROVIDER")

        fpo_profile = FPO.objects.get(user=self.request.user)

        ServiceProvider.objects.create(
            user=user,
            fpo=fpo_profile
        )

class CreateAssistantView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != "PROVIDER":
            raise PermissionDenied("Only Provider can create assistant.")

        user = serializer.save(role="ASSISTANT")

        provider_profile = ServiceProvider.objects.get(user=self.request.user)

        Assistant.objects.create(
            user=user,
            provider=provider_profile
        )


from rest_framework.response import Response
from rest_framework.views import APIView


class ListProvidersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != "FPO":
            raise PermissionDenied("Only FPO can view providers.")

        fpo_profile = request.user.fpo

        providers = ServiceProvider.objects.filter(fpo=fpo_profile)

        data = [
            {
                "id": provider.user.id,
                "username": provider.user.username,
                "name": provider.name
            }
            for provider in providers
        ]

        return Response(data)
    
    
    

class ListAssistantsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != "PROVIDER":
            raise PermissionDenied("Only Provider can view assistants.")

        provider_profile = request.user.serviceprovider

        assistants = Assistant.objects.filter(provider=provider_profile)

        data = [
            {
                "id": assistant.user.id,
                "username": assistant.user.username,
                "name": assistant.name
            }
            for assistant in assistants
        ]

        return Response(data)
    
    

