# Generated by Django 3.2.4 on 2021-06-22 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
