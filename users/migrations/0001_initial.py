# Generated by Django 3.2.4 on 2021-06-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contactid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=100)),
                ('phone', models.CharField(default=None, max_length=13)),
                ('email', models.EmailField(default=None, max_length=100)),
                ('msg', models.TextField(default=None, max_length=5000)),
                ('country', models.TextField(default=None, max_length=50)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]