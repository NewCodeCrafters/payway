# Generated by Django 4.2.7 on 2023-12-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_profiles_profile_pics'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='id_verification',
            field=models.CharField(blank=True, choices=[('Passport', 'Passport'), ('NIN', 'Nin'), ('BVN', 'Bvn'), ('Drivers_license', 'Drivers License')], max_length=100),
        ),
    ]