# Generated by Django 4.2.4 on 2023-08-28 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_details', models.TextField(default='Mpesa')),
                ('amount', models.IntegerField()),
                ('amount_paid', models.IntegerField()),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('sign_off', models.TextField(default='owner')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='customer.customers')),
            ],
        ),
    ]
