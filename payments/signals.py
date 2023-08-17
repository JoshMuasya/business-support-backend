from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from customer.models import Customers

class Payments(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='payments')
    amount = models.IntegerField(blank=True, null=True)
    amount_paid = models.IntegerField()
    balance = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} - Customer: {self.customer.first_name} {self.customer.last_name}"
    
    def calculate_balance(self):
        return self.amount - self.amount_paid

@receiver(pre_save, sender=Payments)
def set_amount_from_balance(sender, instance, **kwargs):
    if instance.customer and not instance.amount:
        latest_balance = instance.customer.payments_set.latest('created_at').balance
        instance.amount = latest_balance