from django.db import models

class Customers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
