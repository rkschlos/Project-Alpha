# Generated by Django 4.0.3 on 2022-03-30 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]
