# Generated by Django 3.2.5 on 2021-08-12 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
