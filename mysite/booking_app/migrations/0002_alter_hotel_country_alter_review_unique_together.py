# Generated by Django 5.1.4 on 2024-12-17 11:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotels', to='booking_app.country'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('user_name', 'hotel')},
        ),
    ]
