# Generated by Django 2.2.11 on 2021-05-06 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0227_auto_20210506_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='shiftingrequest',
            name='breathlessness_level',
            field=models.IntegerField(choices=[(10, 'NOT SPECIFIED'), (20, 'MILD'), (30, 'MODERATE'), (40, 'SEVERE')], default=10),
        ),
    ]