# Generated by Django 4.2.7 on 2024-01-09 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='from_acc',
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transaction_type',
            field=models.CharField(choices=[('DEPOSIT', 'Deposit'), ('WITHDRAWAL', 'Withdrawal'), ('TRANSFER', 'Transfer')], max_length=30),
        ),
    ]
