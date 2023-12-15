# Generated by Django 4.2.7 on 2023-12-15 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_profiles_doc_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
