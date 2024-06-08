from django.db import models

class PhoneNumberInfo(models.Model):
    phone_number = models.CharField(max_length=20, unique=True)
    country = models.CharField(max_length=100)
    service_provider = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number

