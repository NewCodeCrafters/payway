# Generated by Django 4.2.7 on 2023-12-02 11:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(blank=True, max_length=11, validators=[django.core.validators.MinLengthValidator(10)])),
                ('currency', models.CharField(blank=True, choices=[('USD', 'Usd'), ('CAD', 'Cad'), ('NGN', 'Ngn'), ('GBP', 'Gbp'), ('EUR', 'Eur'), ('AUD', 'Aud'), ('GHC', 'Ghc')], max_length=10)),
                ('balance', models.FloatField()),
                ('is_active', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
