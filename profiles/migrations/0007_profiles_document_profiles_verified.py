# Generated by Django 4.2.7 on 2023-12-13 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_profiles_id_verification'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='hahhaha'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]