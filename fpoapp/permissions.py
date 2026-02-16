from rest_framework.permissions import BasePermission

class IsFarmer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'FARMER'

class IsFPO(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'FPO'

class IsProvider(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'PROVIDER'

class IsAssistant(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'ASSISTANT'
