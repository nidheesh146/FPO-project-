from django.urls import path
from .views import FarmerRegisterView,CreateProviderView,CreateAssistantView,FPORegisterView,ListProvidersView,ListAssistantsView

urlpatterns = [
    path('register/', FarmerRegisterView.as_view()),
    path('create-provider/', CreateProviderView.as_view()),
    path('create-assistant/', CreateAssistantView.as_view()),
    path('providers/', ListProvidersView.as_view()),
    path('assistants/', ListAssistantsView.as_view()),
    path('register-fpo/', FPORegisterView.as_view()),
    
]
