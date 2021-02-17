# Generated by Django 3.0.4 on 2020-07-16 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0012_auto_20200716_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addressandpayment',
            name='paymenttype',
        ),
        migrations.AlterField(
            model_name='addressandpayment',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='addressandpayment',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='addressandpayment',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
