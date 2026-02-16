from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class FPO(models.Model):
    name = models.CharField(max_length=100)


class Farmer(models.Model):
    name = models.CharField(max_length=100)
    fpo = models.ForeignKey(FPO, on_delete=models.CASCADE)


class ServiceProvider(models.Model):
    name = models.CharField(max_length=100)
    fpo = models.ForeignKey(FPO, on_delete=models.CASCADE)


class Assistant(models.Model):
    name = models.CharField(max_length=100)
    provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE,null=True)


class ServiceRequest(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ASSIGNED', 'Assigned'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]

    farmer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='farmer_requests'
    )

    provider = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='provider_requests'
    )

    assistant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='assistant_requests'
    )

    service_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)


class User(AbstractUser):

    ROLE_CHOICES = (
        ('FARMER', 'Farmer'),
        ('FPO', 'FPO'),
        ('PROVIDER', 'Provider'),
        ('ASSISTANT', 'Assistant'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
