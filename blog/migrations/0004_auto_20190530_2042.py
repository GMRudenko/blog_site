# Generated by Django 2.2.1 on 2019-05-30 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190529_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpost',
            name='text',
            field=models.TextField(max_length=1000),
        ),
    ]
