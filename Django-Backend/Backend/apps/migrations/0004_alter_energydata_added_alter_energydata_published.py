# Generated by Django 4.2.5 on 2023-09-11 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_alter_energydata_end_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energydata',
            name='added',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='energydata',
            name='published',
            field=models.DateTimeField(),
        ),
    ]
