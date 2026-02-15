from django.db import models


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
        ('COMPLETED', 'Completed'),
    ]

    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    provider = models.ForeignKey(ServiceProvider, on_delete=models.SET_NULL, null=True, blank=True)
    assistant = models.ForeignKey(Assistant, on_delete=models.SET_NULL, null=True, blank=True)

    service_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    created_at = models.DateTimeField(auto_now_add=True,null=True)
