# Generated by Django 4.1.4 on 2023-01-28 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solid', '0005_displayuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='displayuser',
            name='adress',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
