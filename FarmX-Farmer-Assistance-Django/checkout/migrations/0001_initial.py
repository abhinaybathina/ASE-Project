# Generated by Django 3.0.4 on 2020-06-14 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Addressandpayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymenttype', models.CharField(choices=[('NETBANKING', 'netbanking'), ('PAYPAL', 'paypal'), ('PAYTM', 'paytm'), ('MASTERCARD', 'mastercard'), ('VISACARD', 'visacard')], max_length=20)),
                ('accountnumber', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
