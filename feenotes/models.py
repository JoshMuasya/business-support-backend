from django.db import models
from customer.models import Customers

class Feenotes(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='feenotes')
    payment_details = models.TextField(default="Mpesa")
    amount = models.IntegerField()
    sign_off = models.TextField(default="owner")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feenote {self.id} - Customer: {self.customer.first_name} {self.customer.last_name}"
