# Generated by Django 3.2.4 on 2021-06-19 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=13),
        ),
    ]
