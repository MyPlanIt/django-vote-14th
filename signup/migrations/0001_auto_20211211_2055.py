# Generated by Django 3.0.8 on 2021-12-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', 'add_User_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255, verbose_name='Password'),
        ),
    ]
