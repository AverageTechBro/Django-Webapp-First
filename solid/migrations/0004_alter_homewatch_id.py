# Generated by Django 4.1.4 on 2023-01-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solid', '0003_alter_homewatch_display_alter_homewatch_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homewatch',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
