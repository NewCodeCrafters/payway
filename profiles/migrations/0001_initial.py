# Generated by Django 4.2.7 on 2023-12-21 14:47

import django.core.validators
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(blank=True, max_length=11, validators=[django.core.validators.MinLengthValidator(10)])),
                ('address', models.CharField(blank=True, max_length=100)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('dob', models.DateField(blank=True, null=True)),
                ('profile_pics', models.ImageField(blank=True, upload_to='hahhaha')),
                ('currency', models.CharField(blank=True, choices=[('USD', 'Usd'), ('CAD', 'Cad'), ('NGN', 'Ngn'), ('GBP', 'Gbp'), ('EUR', 'Eur'), ('AUD', 'Aud'), ('GHC', 'Ghc')], max_length=100)),
                ('document_type', models.CharField(blank=True, choices=[('Passport', 'Passport'), ('NIN', 'Nin'), ('BVN', 'Bvn'), ('Drivers_license', 'Drivers License')], max_length=100)),
                ('doc_verified', models.BooleanField(default=False)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('document', models.FileField(blank=True, null=True, upload_to='hahhaha')),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
