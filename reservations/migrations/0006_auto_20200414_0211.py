# Generated by Django 2.2.5 on 2020-04-14 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_auto_20200414_0135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Reservation Status'},
        ),
    ]