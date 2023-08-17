from django.db import models
from customer.models import Customers

class Payments(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='payments')
    payment_details = models.TextField(default="Mpesa")
    amount = models.IntegerField()
    amount_paid = models.IntegerField()
    balance = models.IntegerField(blank=True, null=True)
    sign_off = models.TextField(default="owner")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} - Customer: {self.customer.first_name} {self.customer.last_name}"
    
    def calculate_balance(self):
        return self.amount - self.amount_paid

    def save(self, *args, **kwargs):
        self.balance = self.calculate_balance()
        super().save(*args, **kwargs)