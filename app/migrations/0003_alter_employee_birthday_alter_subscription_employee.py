# Generated by Django 5.0.7 on 2024-07-24 01:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='app.employee'),
        ),
    ]