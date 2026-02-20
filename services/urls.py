from django.urls import path
from .views import *

urlpatterns = [
    path('requests/', ServiceRequestListCreateView.as_view()),
    path('requests/<int:pk>/assign-provider/', AssignProviderView.as_view()),
    path('requests/<int:pk>/respond/', RespondRequestView.as_view()),
    path('requests/<int:pk>/assign-assistant/', AssignAssistantView.as_view()),
    path('requests/<int:pk>/start/', StartWorkView.as_view()),
    path('requests/<int:pk>/complete/', CompleteWorkView.as_view()),
]
