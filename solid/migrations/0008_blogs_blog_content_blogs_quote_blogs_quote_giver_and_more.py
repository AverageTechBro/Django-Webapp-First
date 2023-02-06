# Generated by Django 4.1.4 on 2023-01-30 05:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('solid', '0007_blogs_delete_displayuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='blog_content',
            field=models.TextField(default=django.utils.timezone.now, max_length=9999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogs',
            name='quote',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogs',
            name='quote_giver',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogs',
            name='quote_last_page',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogs',
            name='quote_mid_page',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]